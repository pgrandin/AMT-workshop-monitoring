#!/bin/bash

w=`xwininfo -id $(xdotool getactivewindow)|grep Width:`
if [[ "$w" != "  Width: 1920" ]]; then
	xdotool key F11
fi
