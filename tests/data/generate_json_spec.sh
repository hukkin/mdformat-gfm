#!/bin/bash
# A script to generate JSON file with all the examples in the
# GFM spec. Update `gfmcommit` commit hash value to generate an
# updated JSON. Run this script in `tests/data/` directory to write
# a file in `tests/data/gfm_spec.commit-{commit-hash}.json`.

git clone https://github.com/github/cmark-gfm.git

gfmcommit=85d895289c5ab67f988ca659493a64abb5fec7b4
cd cmark-gfm/ \
&& git reset --hard $gfmcommit \
&& cd ..

python3 cmark-gfm/test/spec_tests.py --dump-tests --spec=cmark-gfm/test/spec.txt > gfm_spec.commit-${gfmcommit}.json
