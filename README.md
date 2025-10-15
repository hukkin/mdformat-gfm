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

Mdformat-gfm adds a `--compact-tables` CLI option and a corresponding `compact_tables` TOML boolean.
Turning this on will strip extra spaces from GFM tables that are otherwise used to align table columns.

To use the option on the command line, do

```sh
mdformat --compact-tables <filename>
```

Alternatively add the following in a `.mdformat.toml` configuration file

```toml
[plugin.tables]
compact_tables = true
```
