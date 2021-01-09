#!/usr/bin/env bash

# usage: ./sngen.sh episode_slug anchor|ximalaya
# e.g. ./sngen.sh 5 anchor

SCRIPT_DIR=/Users/$USER/Documents/projects/gulugulufm.github.io/scripts
SITE_DIR=/Users/$USER/Documents/projects/gulugulufm.github.io/site

echo "Generating show notes for podcast episode $1 for platform $2 ..."

echo "Starting step 1: checking environment (virtualenv)"

workon podcast

echo "Starting step 2: generating formatted show notes"
cd $SITE_DIR && hugo -D
python $SCRIPT_DIR/$2.py $SITE_DIR/public/podcasts/$1/index.html
rm -r $SITE_DIR/public