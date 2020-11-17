[![Build Status](https://github.com/hukkinj1/mdformat-gfm/workflows/Tests/badge.svg?branch=master)](https://github.com/hukkinj1/mdformat-gfm/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)
[![PyPI version](https://img.shields.io/pypi/v/mdformat-gfm)](https://pypi.org/project/mdformat-gfm)

# mdformat-gfm

> Mdformat plugin for GitHub Flavored Markdown compatibility

## Description

By default, [mdformat](https://github.com/executablebooks/mdformat) is [CommonMark](https://spec.commonmark.org/current/) compliant.
Mdformat-gfm is an mdformat plugin that changes the target specification to [GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/).

## Development status

This plugin is not feature complete with the GFM spec yet.

**Done:**

- ✔ Tables
- ✔ Strikethrough
- ✔ Task list items

**To do:**

- ❌ Extended autolinks
- ❌ Disallowed raw HTML

## Install

```sh
pip install mdformat-gfm
```

## Usage

```sh
mdformat <filename>
```
