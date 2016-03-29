#!/usr/bin/python

import sys
import json

dict = {}

for line in sys.stdin:
  data = line.strip().split(" ")
  if len(data) == 10:
    ip, tem1, tem2, tem3, tem4, method, path, protocol, status, tem6 = data
    if method == "\"GET" or method == "\"POST":
      if path.endswith(".jpg"):
        pos = path.rfind("/")
        imageName = path[pos + 1:]
        if imageName not in dict.keys():
          dict[imageName] = []
        dict[imageName].append(ip)

print(json.dumps(dict))
