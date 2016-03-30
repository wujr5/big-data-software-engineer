#!/usr/bin/python

import sys

for line in sys.stdin:
  data = line.strip().split(" ")
  if len(data) == 10:
    ip, tem1, tem2, tem3, tem4, method, path, protocol, status, tem6 = data
    if method == "\"GET" or method == "\"POST":
      if path.endswith(".jpg"):
        pos = path.rfind("/")
        imageName = path[pos + 1:]
        if imageName != "primary-news-1.jpg":
          print("b_"+imageName, "\t", ip)
        else:
          print("a_"+imageName, "\t", ip)
