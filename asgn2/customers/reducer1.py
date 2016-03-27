#!/usr/bin/python

import sys

oldKey = None
oldName = None
count = 0

for line in sys.stdin:
  data_mapped = line.strip().split("\t")

  if len(data_mapped) != 2:
    continue

  key, name = data_mapped

  if oldKey is not None and oldKey != key:
    print(count, "\t", oldKey, "\t", oldName)
    count = 0

  count += 1
  oldKey = key
  oldName = name

if oldKey is not None:
  print(count, "\t", oldKey, "\t", oldName)
