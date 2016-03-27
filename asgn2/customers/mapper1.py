#!/usr/bin/python

import sys
import time

t1 = time.strptime('1996-01-01', "%Y-%m-%d")
keyNumDict = {}
keyNameDict = {}

for line in sys.stdin:
  data = line.strip().split("|")
  if len(data) == 4:
    key, name, phone, date = data
    t2 = time.strptime(date, "%Y-%m-%d")
    if t2 < t1:
      print(key, "\t", name)
