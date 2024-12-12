from pathlib import Path

from markdown_it import MarkdownIt
from markdown_it.utils import read_fixture_file
import pytest

from mdformat_gfm._mdit_gfm_autolink_plugin import gfm_autolink_plugin

FIXTURE_PATH = Path(__file__).parent / "data" / "gfm_autolink.md"


@pytest.mark.parametrize("line,title,md,expected_html", read_fixture_file(FIXTURE_PATH))
def test_gfm_autolink(line, title, md, expected_html):
    mdit = MarkdownIt().use(gfm_autolink_plugin)
    text = mdit.render(md)
    assert text.rstrip() == expected_html.rstrip()
