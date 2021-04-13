import re

from markdown_it import MarkdownIt
import mdformat.plugins
from mdformat.renderer import DEFAULT_RENDERERS, RenderContext, RenderTreeNode
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


def _strikethrough_renderer(node: RenderTreeNode, context: RenderContext) -> str:
    content = "".join(child.render(context) for child in node.children)
    return "~~" + content + "~~"


def _render_with_default_renderer(node: RenderTreeNode, context: RenderContext) -> str:
    """Render the node using default renderer instead of the one in `context`.

    We don't use `RenderContext.with_default_renderer_for` because that
    changes the default renderer in context, where it's applied
    recursively to render functions of children.
    """
    syntax_type = node.type
    text = DEFAULT_RENDERERS[syntax_type](node, context)
    for postprocessor in context.postprocessors.get(syntax_type, ()):
        text = postprocessor(text, node, context)
    return text


def _list_item_renderer(node: RenderTreeNode, context: RenderContext) -> str:
    classes = node.attrs.get("class")
    if classes is None or "task-list-item" not in classes:
        return _render_with_default_renderer(node, context)

    # Tasklists extension makes a bit weird token stream where
    # tasks are annotated by html. We need to remove the HTML.
    paragraph_node = node.children[0]
    inline_node = paragraph_node.children[0]
    assert inline_node.type == "inline"
    assert inline_node.children, "inline token must have children"
    html_inline_node = inline_node.children[0]
    assert 'class="task-list-item-checkbox"' in html_inline_node.content

    # This is naughty, shouldn't mutate and rely on `.remove` here
    inline_node.children.remove(html_inline_node)

    checkmark = "x" if 'checked="checked"' in html_inline_node.content else " "

    text = _render_with_default_renderer(node, context)
    # Strip leading space chars (numeric representations)
    text = re.sub(r"^(&#32;)+", "", text)
    return f"[{checkmark}] {text}"


def _escape_text(text: str, node: RenderTreeNode, context: RenderContext) -> str:
    # Escape strikethroughs
    text = text.replace("~~", "\\~~")

    return text


RENDERERS = {"s": _strikethrough_renderer, "list_item": _list_item_renderer}
POSTPROCESSORS = {"text": _escape_text}
