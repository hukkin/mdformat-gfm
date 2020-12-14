import re
from typing import Any, Mapping, Optional, Sequence, Tuple

from markdown_it import MarkdownIt
from markdown_it.token import Token
import mdformat.plugins
from mdformat.renderer import MARKERS, MDRenderer
from mdit_py_plugins.tasklists import tasklists_plugin


def update_mdit(mdit: MarkdownIt) -> None:
    # Enable mdformat-tables plugin
    tables_plugin = mdformat.plugins.PARSER_EXTENSIONS["tables"]
    if tables_plugin not in mdit.options["parser_extension"]:
        mdit.options["parser_extension"].append(tables_plugin)
        tables_plugin.update_mdit(mdit)

    # Enable strikethrough markdown-it extension
    mdit.enable("strikethrough")

    # Enable tasklist markdown-it extension
    mdit.use(tasklists_plugin)


def render_token(
    renderer: MDRenderer,
    tokens: Sequence[Token],
    index: int,
    options: Mapping[str, Any],
    env: dict,
) -> Optional[Tuple[str, int]]:
    token = tokens[index]

    # Prevent endless recursion. Make sure this plugin never processes
    # a token more than once.
    if "mdformat-gfm-processed-tokens" not in env:
        env["mdformat-gfm-processed-tokens"] = set()
    if id(token) in env["mdformat-gfm-processed-tokens"]:
        return None
    env["mdformat-gfm-processed-tokens"].add(id(token))

    # Render strikethroughs
    if token.type == "s_open":
        closing_index = _index_closing_token(tokens, index)
        text = renderer.render(
            tokens, options, env, start=index + 1, stop=closing_index, finalize=False
        )
        text = "~~" + text + "~~"
        return text, closing_index

    # Render task lists items
    if token.type == "list_item_open":
        classes = token.attrGet("class")
        if classes is None or "task-list-item" not in classes:
            return None
        closing_index = _index_closing_token(tokens, index)

        # Tasklists extension makes a bit weird token stream where
        # tasks are annotated by html. We need to remove the HTML.
        inline_token = tokens[index + 2]
        assert inline_token.type == "inline"
        html_inline = inline_token.children[0]
        assert 'class="task-list-item-checkbox"' in html_inline.content
        inline_token.children.remove(html_inline)
        checkmark = "x" if 'checked="checked"' in html_inline.content else " "

        text = renderer.render(
            tokens, options, env, start=index, stop=closing_index + 1, finalize=False
        )

        text = re.sub(fr"{MARKERS.LIST_INDENT_FIRST_LINE}\s+", f" [{checkmark}] ", text)
        return text, closing_index

    return None


def _index_closing_token(tokens: Sequence[Token], opening_index: int) -> int:
    opening_token = tokens[opening_index]
    assert opening_token.nesting == 1, "Cant find closing token for non opening token"
    for i in range(opening_index + 1, len(tokens)):
        closing_candidate = tokens[i]
        if closing_candidate.level == opening_token.level:
            return i
    raise ValueError("Invalid token list. Closing token not found.")
