#!/bin/bash

for i in *.MXF; do
	if [ -e "$i" ]; then
		file=`basename "$i" .MXF`
		ffmpeg -i "$i" -map 0:1 -acodec libmp3lame "$file.mp3"
	fi
done
