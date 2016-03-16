#!/usr/bin/python

import sys

error_404_total = 0
oldIP = None

for line in sys.stdin:
  data_mapped = line.strip().split("\t")

  # print(len(data_mapped))

  if len(data_mapped) != 2:
    continue

  thisIP, thisStatus = data_mapped

  if oldIP and oldIP != thisIP:
    print oldIP, "\t", error_404_total
    oldIP = thisIP
    error_404_total = 0

  oldIP = thisIP
  error_404_total += 1

if oldIP != None:
  print oldIP, "\t", error_404_total
