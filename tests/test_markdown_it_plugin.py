from markdown_it import MarkdownIt

from mdformat_gfm._mdit_gfm_autolink_plugin import gfm_autolink_plugin


def test_gfm_autolink():
    mdit = MarkdownIt()
    mdit.use(gfm_autolink_plugin)
    text = "GFM autolink www.commonmark.org"
    html = mdit.render(text)
    assert (
        html
        == '<p>GFM autolink <a href="http://www.commonmark.org">www.commonmark.org</a></p>\n'  # noqa: E501
    )
