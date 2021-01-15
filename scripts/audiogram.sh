#!/bin/bash

# adapted from https://github.com/yorkxin/amcyfm-utils/blob/master/audiogram.sh
# usage e.g. ./audiogram.sh -e 8 -m dark

set -e

SCRIPT_DIR=/Users/$USER/Documents/projects/gulugulufm.github.io/scripts
SITE_DIR=/Users/$USER/Documents/projects/gulugulufm.github.io/site

TEMP_DIR=$SCRIPT_DIR/audiogram-temp
OUTPUT_DIR=$SCRIPT_DIR/audiogram-output
RESOURCES_DIR=$SCRIPT_DIR/resources

if ! command -v ffmpeg > /dev/null 2>/dev/null ; then
  echo "Please install ffmpeg" 1>&2
  echo "ffmpeg: brew install ffmpeg" 1>&2
  exit 1
fi

function print_usage {
  echo "Usage: $(basename $0) -e episode(1 and up) -m [light|dark]" 1>&2
}

while getopts 'e:m:' opt; do
  case $opt in
    e) EPISODE=$OPTARG ;;
    m) MODE=$OPTARG ;;
    *)
      print_usage
      exit 1
    ;;
  esac
done

shift $((OPTIND -1))

if [ -z "$EPISODE" ] || [ -z "$MODE" ]; then
  print_usage
  exit 1
fi

if [ "$MODE" != "light" ] && [ "$MODE" != "dark" ]; then
  print_usage
  exit 1
fi

echo "Making dirs ..."
mkdir -p $TEMP_DIR
rm -rf $TEMP_DIR/*
mkdir -p $OUTPUT_DIR
rm -rf $OUTPUT_DIR/*

echo "Preparing files to make audiogram ..."
cd $SITE_DIR && hugo -D
python $SCRIPT_DIR/audiogram_prep.py $SITE_DIR/public/podcasts/$EPISODE/index.html $TEMP_DIR

tempfile=$TEMP_DIR/ffmpeg.config

wavecolor=0xE1DDCA
textcolor=white

if [ "$MODE" = "light" ]; then
  wavecolor=0x50595A
  textcolor=black
fi

# if light mode, change wavecolor and textcolor ...

cat <<EOF > "$tempfile"
[1:a]
showwaves=
  s=840x640:
  mode=line:
  rate=25:
  colors=$wavecolor
[waveform];
[0:v][waveform]
overlay=
  x=80:
  y=375:
  shortest=1,
drawtext=
  fontsize=100:
  fontfile=/System/Library/Fonts/Hiragino\ Sans\ GB.ttc:
  textfile='$TEMP_DIR/podcast_name.txt':
  x=(w-text_w)/2:
  y=200:
  fontcolor=$textcolor,
drawtext=
  fontsize=50:
  fontfile=/System/Library/Fonts/Hiragino\ Sans\ GB.ttc:
  textfile='$TEMP_DIR/episode_title.txt':
  x=(w-text_w)/2:
  y=375:
  fontcolor=$textcolor,
drawtext=
  fontsize=50:
  fontfile=/System/Library/Fonts/Hiragino\ Sans\ GB.ttc:
  textfile='$TEMP_DIR/episode_description.txt':
  x=(w-text_w)/2:
  y=450:
  fontcolor=$textcolor,
drawtext=
  fontsize=50:
  fontfile=/System/Library/Fonts/Supplemental/Arial.ttf:
  textfile='$TEMP_DIR/link.txt':
  x=(w-text_w)/2:
  y=850:
  fontcolor=$textcolor
[final]
EOF

echo "Making audiogram ..."
image=$RESOURCES_DIR/$MODE.png
episode=$EPISODE
if [ ${#EPISODE} -eq 1 ]; then
  episode=0$EPISODE
fi
output=$OUTPUT_DIR/$episode-trailer.mp4
audio=/Users/$USER/Documents/podcasting/$episode/$episode-trailer.mp3

# generate video
ffmpeg -loop 1 -i "$image" -i "$audio" -filter_complex_script "$tempfile" -map "[final]" -map 1:a "$output"

# take a few screenshots
ffmpeg -ss 00:00:10.000 -i "$output" -vframes 1 $output-1.jpg
ffmpeg -ss 00:00:10.500 -i "$output" -vframes 1 $output-2.jpg
ffmpeg -ss 00:00:12.000 -i "$output" -vframes 1 $output-3.jpg

echo "Cleaning up ..."
rm -r $SITE_DIR/public
rm -r $TEMP_DIR

echo "All done! Audiogram is ready at $output"
open $(dirname "$output")
open -a "quicktime player" $output
