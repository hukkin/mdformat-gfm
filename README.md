[![Build Status](https://github.com/hukkin/mdformat-gfm/actions/workflows/tests.yaml/badge.svg?branch=master)](https://github.com/hukkin/mdformat-gfm/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)
[![PyPI version](https://img.shields.io/pypi/v/mdformat-gfm)](https://pypi.org/project/mdformat-gfm)

# mdformat-gfm

> Mdformat plugin for GitHub Flavored Markdown compatibility

## Description

[Mdformat](https://github.com/executablebooks/mdformat) is a formatter for
[CommonMark](https://spec.commonmark.org/current/)
compliant Markdown.

Mdformat-gfm is an mdformat plugin that changes the target specification to
[GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/),
making the tool able to format the following syntax extensions:

- [tables](https://github.github.com/gfm/#tables-extension-)
- [task list items](https://github.github.com/gfm/#task-list-items-extension-)
- [strikethroughs](https://github.github.com/gfm/#strikethrough-extension-)
- [autolinks](https://github.github.com/gfm/#autolinks-extension-)
- [disallowed raw HTML](https://github.github.com/gfm/#disallowed-raw-html-extension-)
  (note that no changes are required from a formatter to support this extension)

## Install

```sh
pipx install mdformat
pipx inject mdformat mdformat-gfm
```

## Usage

```sh
mdformat <filename>
```

## Configuration

Mdformat-gfm distribution includes two plugins identified as `gfm` and `tables`.
The `gfm` plugin adds support for all GFM syntax (including tables).
Enabling `tables` only adds tables support.

By default, table columns are padded to align cells. Use `--compact-tables` to
remove padding, or `--column-widths` to retain separator markers while
formatting table contents (useful for maintaining column width since pandoc
formats tables in its output based on column widths).

Separator spacing is normalized without changing dashes or alignment markers.

```sh
mdformat --compact-tables <filename>
```

Alternatively, configure either option in `.mdformat.toml`:

```toml
[plugin.tables]
compact_tables = true
# Or: col_widths = true
```

`--compact-tables` takes precedence over `--column-widths`.
