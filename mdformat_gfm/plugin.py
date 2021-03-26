import re
from typing import Any, Mapping, MutableMapping

from markdown_it import MarkdownIt
import mdformat.plugins
from mdformat.renderer import DEFAULT_RENDERER_FUNCS, RenderTreeNode
import mdformat.renderer._default_renderers
from mdformat.renderer.typing import RendererFunc
from mdit_py_plugins.tasklists import tasklists_plugin


# Make a nasty monkey patch to private API. Make this change upstream instead.
def _monkeypatch_is_text_inside_autolink(node: "RenderTreeNode") -> bool:
    assert node.type == "text"
    return (
        node.parent  # type: ignore
        and node.parent.type == "link"
        and node.parent.info == "auto"
    )


mdformat.renderer._default_renderers.is_text_inside_autolink = (
    _monkeypatch_is_text_inside_autolink
)


def update_mdit(mdit: MarkdownIt) -> None:
    # Enable linkify-it-py (for GFM autolink extension)
    mdit.options["linkify"] = True
    mdit.enable("linkify")

    # Enable mdformat-tables plugin
    tables_plugin = mdformat.plugins.PARSER_EXTENSIONS["tables"]
    if tables_plugin not in mdit.options["parser_extension"]:
        mdit.options["parser_extension"].append(tables_plugin)
        tables_plugin.update_mdit(mdit)

    # Enable strikethrough markdown-it extension
    mdit.enable("strikethrough")

    # Enable tasklist markdown-it extension
    mdit.use(tasklists_plugin)


def _link_renderer(
    node: RenderTreeNode,
    renderer_funcs: Mapping[str, RendererFunc],
    options: Mapping[str, Any],
    env: MutableMapping,
) -> str:
    """Extend the default link renderer to handle linkify links."""
    if node.markup == "linkify":
        return "".join(
            child.render(renderer_funcs, options, env) for child in node.children
        )
    return DEFAULT_RENDERER_FUNCS["link"](node, renderer_funcs, options, env)


def _strikethrough_renderer(
    node: RenderTreeNode,
    renderer_funcs: Mapping[str, RendererFunc],
    options: Mapping[str, Any],
    env: MutableMapping,
) -> str:
    content = "".join(
        child.render(renderer_funcs, options, env) for child in node.children
    )
    return "~~" + content + "~~"


def _list_item_renderer(
    node: RenderTreeNode,
    renderer_funcs: Mapping[str, RendererFunc],
    options: Mapping[str, Any],
    env: MutableMapping,
) -> str:
    classes = node.attrs.get("class")
    if classes is None or "task-list-item" not in classes:
        return DEFAULT_RENDERER_FUNCS["list_item"](node, renderer_funcs, options, env)

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

    text = DEFAULT_RENDERER_FUNCS["list_item"](node, renderer_funcs, options, env)
    # Strip leading space chars (numeric representations)
    text = re.sub(r"^(&#32;)+", "", text)
    return f"[{checkmark}] {text}"


RENDERER_FUNCS = {
    "s": _strikethrough_renderer,
    "list_item": _list_item_renderer,
    "link": _link_renderer,
}
