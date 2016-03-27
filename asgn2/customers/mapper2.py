#!/usr/bin/python

import sys

for line in sys.stdin:
  data = line.strip().split("\t")
  if len(data) == 3:
    count, key, name = data
    if int(count) >= 25:
      print(key, "\t", name, "\t", count)
