#!/bin/zsh

# Master script for laying out all resources needed to publish an episode.
# usage: ./assets.sh episode_slug
# e.g. ./assets.sh 9

set -e

SCRIPT_DIR=/Users/$USER/Documents/projects/gulugulufm.github.io/scripts
SITE_DIR=/Users/$USER/Documents/projects/gulugulufm.github.io/site

$SCRIPT_DIR/sngen.sh $1 anchor
$SCRIPT_DIR/sngen.sh $1 ximalaya

if [ $(($1 % 2)) -eq 0 ]; then
    $SCRIPT_DIR/audiogram.sh -e $1 -m dark;
else
    $SCRIPT_DIR/audiogram.sh -e $1 -m light;
fi

cd $SITE_DIR && hugo -D
python $SCRIPT_DIR/snsgen.py $1
rm -r $SITE_DIR/public
