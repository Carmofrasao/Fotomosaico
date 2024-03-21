#!/usr/bin/env python3
from colorthief import ColorThief
import os
import sys

caract = open('caract.txt', 'w')

for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        color_thief = ColorThief(sys.argv[1]+file)
        dominant_color = color_thief.get_color(quality=1)
        caract.write(file+": "+str(dominant_color)+"\n")
