from pathlib import Path

from markdown_it.utils import read_fixture_file
import mdformat
import mdformat._cli
import pytest

TEST_CASES = read_fixture_file(Path(__file__).parent / "data" / "fixtures.md")


@pytest.mark.parametrize(
    "line,title,text,expected", TEST_CASES, ids=[f[1] for f in TEST_CASES]
)
def test_fixtures__api(line, title, text, expected):
    """Test fixtures in tests/data/fixtures.md."""
    md_new = mdformat.text(text, extensions={"gfm"})
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected


@pytest.mark.parametrize(
    "line,title,text,expected", TEST_CASES, ids=[f[1] for f in TEST_CASES]
)
def test_fixtures__cli(line, title, text, expected, tmp_path):
    """Test fixtures in tests/data/fixtures.md."""
    file_path = tmp_path / "test_markdown.md"
    file_path.write_text(text)
    assert mdformat._cli.run([str(file_path)]) == 0
    md_new = file_path.read_text()
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected
