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
COMPACT_TABLES_CASES = read_fixture_file(
    Path(__file__).parent / "data" / "compact_tables.md"
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
    file_path.write_text(text, encoding="utf-8")
    assert mdformat._cli.run([str(file_path)]) == 0
    md_new = file_path.read_text(encoding="utf-8")
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
    file_path.write_text(text, encoding="utf-8")
    assert mdformat._cli.run([str(file_path), "--wrap=50"]) == 0
    md_new = file_path.read_text(encoding="utf-8")
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected


@pytest.mark.parametrize(
    "line,title,text,expected",
    COMPACT_TABLES_CASES,
    ids=[f[1] for f in COMPACT_TABLES_CASES],
)
def test_compact_tables__cli(line, title, text, expected, tmp_path):
    """Test fixtures in tests/data/compact_tables.md."""
    file_path = tmp_path / "test_markdown.md"
    file_path.write_text(text, encoding="utf-8")
    assert mdformat._cli.run([str(file_path), "--compact-tables"]) == 0
    md_new = file_path.read_text(encoding="utf-8")
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected


def test_compact_tables__toml(tmp_path):
    aligned_table = """\
| a      |      b |   c    |
| :----- | -----: | :----: |
| 1      |      2 |   3    |
| xxxxxx | yyyyyy | zzzzzz |
"""
    compact_table = """\
| a | b | c |
| :- | -: | :-: |
| 1 | 2 | 3 |
| xxxxxx | yyyyyy | zzzzzz |
"""
    conf_path = tmp_path / ".mdformat.toml"
    conf_path.write_text("[plugin.tables]\ncompact_tables=true", encoding="utf-8")
    file_path = tmp_path / "test_markdown.md"
    file_path.write_text(aligned_table, encoding="utf-8")
    assert mdformat._cli.run([str(file_path)]) == 0
    md_new = file_path.read_text(encoding="utf-8")
    assert md_new == compact_table
