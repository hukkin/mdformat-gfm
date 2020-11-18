[![Build Status](https://github.com/hukkinj1/mdformat-gfm/workflows/Tests/badge.svg?branch=master)](https://github.com/hukkinj1/mdformat-gfm/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)
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

## Install

```sh
pip install mdformat-gfm
```

## Usage

```sh
mdformat <filename>
```

## Limitations

This plugin does currently not implement any special handling for the GFM
[autolink extension](https://github.github.com/gfm/#autolinks-extension-).
Please file a bug report for cases where an autolink breaks formatting.
