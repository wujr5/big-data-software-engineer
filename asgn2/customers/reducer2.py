#!/usr/bin/python

import sys

for line in sys.stdin:
  data = line.strip().split("\t")
  count, key, name = data
  print(key, "\t", name, "\t", count)
