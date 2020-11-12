from typing import Any, Mapping, Optional, Sequence, Tuple

from markdown_it import MarkdownIt
from markdown_it.token import Token
import mdformat.plugins
from mdformat.renderer import MDRenderer


def update_mdit(mdit: MarkdownIt) -> None:
    # Enable mdformat-tables plugin
    tables_plugin = mdformat.plugins.PARSER_EXTENSIONS["tables"]
    if tables_plugin not in mdit.options["parser_extension"]:
        mdit.options["parser_extension"].append(tables_plugin)
        tables_plugin.update_mdit(mdit)

    # Enable strikethrough markdown-it extension
    mdit.enable("strikethrough")


def render_token(
    renderer: MDRenderer,
    tokens: Sequence[Token],
    index: int,
    options: Mapping[str, Any],
    env: dict,
) -> Optional[Tuple[str, int]]:
    token = tokens[index]
    if token.type == "s_open":
        closing_index = _index_closing_token(tokens, index)
        text = renderer.render(
            tokens[index + 1 : closing_index], options, env, finalize=False
        )
        text = "~~" + text + "~~"
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
