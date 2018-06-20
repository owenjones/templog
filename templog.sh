#!/bin/bash
MAXSIZE=2048000
SIZE=$(du -b /home/owen/temp.log | tr -s '\t' ' ' | cut -d' ' -f1)

#if [ $SIZE -gt $MAXSIZE ]; then
#savelog -c 10 /home/owen/temp.log
#fi

TIME=$(date +%s)
TEMP=$(/home/owen/bin/temp)

$(echo "[$TIME] $TEMP" >> /home/owen/temp.log)
