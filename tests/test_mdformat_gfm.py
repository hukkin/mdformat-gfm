from pathlib import Path

from markdown_it.utils import read_fixture_file
import mdformat
import mdformat._cli
import pytest

DEFAULT_STYLE_CASES = read_fixture_file(
    Path(__file__).parent / "data" / "default_style.md"
)
WRAP_WIDTH_50_CASES = read_fixture_file(
    Path(__file__).parent / "data" / "wrap_width_50.md"
)


@pytest.mark.parametrize(
    "line,title,text,expected",
    DEFAULT_STYLE_CASES,
    ids=[f[1] for f in DEFAULT_STYLE_CASES],
)
def test_default_style__api(line, title, text, expected):
    """Test fixtures in tests/data/default_style.md."""
    md_new = mdformat.text(text, extensions={"gfm"})
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected


@pytest.mark.parametrize(
    "line,title,text,expected",
    DEFAULT_STYLE_CASES,
    ids=[f[1] for f in DEFAULT_STYLE_CASES],
)
def test_default_style__cli(line, title, text, expected, tmp_path):
    """Test fixtures in tests/data/default_style.md."""
    file_path = tmp_path / "test_markdown.md"
    file_path.write_text(text)
    assert mdformat._cli.run([str(file_path)]) == 0
    md_new = file_path.read_text()
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected


@pytest.mark.parametrize(
    "line,title,text,expected",
    WRAP_WIDTH_50_CASES,
    ids=[f[1] for f in WRAP_WIDTH_50_CASES],
)
def test_wrap_width_50__cli(line, title, text, expected, tmp_path):
    """Test fixtures in tests/data/wrap_width_50.md."""
    file_path = tmp_path / "test_markdown.md"
    file_path.write_text(text)
    assert mdformat._cli.run([str(file_path), "--wrap=50"]) == 0
    md_new = file_path.read_text()
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected
