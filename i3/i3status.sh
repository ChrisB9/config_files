#!/bin/sh
# shell script to prepend i3status with more stuff

py3status -d -l ~/.config/i3/py3log -c ~/.config/i3/i3status.conf | while :
do
        read line
        music=`python  ~/.config/i3/currentplaymusicsong.py`
        echo "$music $line" || exit 1
done
