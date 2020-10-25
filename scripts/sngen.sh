#!/usr/bin/env bash

# usage: ./sngen.sh episode_slug anchor|ximalaya
# e.g. ./sngen.sh 5 anchor

SCRIPT_DIR=/Users/$USER/GoogleDrive/projects/gulugulufm.github.io/scripts
SITE_DIR=/Users/$USER/GoogleDrive/projects/gulugulufm.github.io/site

echo "Generating show notes for podcast episode $1 for platform $2 ..."

echo "Starting step 1: checking environment (docker container)"

if [ $(docker ps -f name=python -f status=running | wc -l) = 2 ];
then
    echo ok
else
    echo 'No running container named python. Exiting.'
    exit 1
fi

docker exec python sh -c 'rm -rf /home/*'
docker cp $SCRIPT_DIR/. python:/home

echo "Starting step 2: generating formatted show notes"
cd $SITE_DIR && hugo -D
docker cp $SITE_DIR/public/podcasts/$1/index.html python:/home
docker exec python python /home/$2.py
rm -r $SITE_DIR/public