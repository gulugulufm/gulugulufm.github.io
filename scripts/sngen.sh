#!/bin/zsh

# usage: ./sngen.sh episode_slug anchor|ximalaya
# e.g. ./sngen.sh 5 anchor

set -e
setopt null_glob

SCRIPT_DIR=/Users/$USER/Documents/projects/gulugulufm.github.io/scripts
SITE_DIR=/Users/$USER/Documents/projects/gulugulufm.github.io/site

OUTPUT_DIR=$SCRIPT_DIR/sngen-output

echo "Generating show notes for podcast episode $1 for platform $2 ..."

echo "Starting step 1: checking environment (virtualenv)"
if [[ "$VIRTUAL_ENV" = "" ]]
then
  echo "Please activate virtualenv -- exiting."
  exit 1
fi

echo "Starting step 2: removing files that are not part of this current episode: $1"
mkdir -p $OUTPUT_DIR
output=$OUTPUT_DIR/$1-$2
for filename in $OUTPUT_DIR/*; do 
    [ -f "$filename" ] || continue
    case $(basename "$filename") in
        $1-*) : ;;
        *) rm $filename ;;
    esac
done

#echo "Starting step 3: generating formatted show notes"
#cd $SITE_DIR && hugo -D
#python $SCRIPT_DIR/$2.py $SITE_DIR/public/podcasts/$1/index.html | tee $output

#rm -r $SITE_DIR/public

#echo "\nOutput file is ready at $output"