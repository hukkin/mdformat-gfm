# Changelog

## 0.4.1

- Fixed
  - Stop new autolink parser from finding autolinks in link and image labels

## 0.4.0 (yanked from PyPI)

- Changed
  - Replaced `linkify-it-py` dependency with a vendored GFM compatible markdown-it-py autolink plugin.
- Fixed
  - Error on angle bracketed `linkify-it-py` links that are not CommonMark autolinks
