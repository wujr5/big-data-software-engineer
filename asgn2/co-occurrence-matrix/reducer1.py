#!/usr/bin/python

import sys
import json

dict = None

for line in sys.stdin:
  dict = json.loads(line)
  break

PN1_LIST = dict["primary-news-1.jpg"]

for key in dict:
  if key == "primary-news-1.jpg":
    continue
  imgList = dict[key]
  intersection = list(set(imgList) & set(PN1_LIST))
  print(key, float(len(intersection)) / float(len(imgList)))
