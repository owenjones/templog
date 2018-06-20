#!/bin/bash
TEMP=$(cat /sys/bus/w1/devices/28-0516a7bd22ff/w1_slave | grep -Eo 't=[0-9]+' | sed 's/t=//g')
echo $(echo "scale=3;$TEMP / 1000" | bc -l)
