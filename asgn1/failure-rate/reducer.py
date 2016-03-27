#!/usr/bin/python

import sys

request_total = 0
error_request_total = 0
oldURL = None

for line in sys.stdin:
  data_mapped = line.strip().split("\t")

  if len(data_mapped) != 2:
    continue

  thisURL, thisStatus = data_mapped

  if oldURL and oldURL != thisURL:
    if error_request_total > 0:
      print oldURL, "\t", error_request_total, "\t", request_total
    request_total = 0
    error_request_total = 0

  oldURL = thisURL
  request_total += 1
  if len(thisStatus) == 3 and (thisStatus[0] == "4" or thisStatus[0] == "5"):
    error_request_total += 1

if oldURL != None and error_request_total > 0:
  print oldURL, "\t", error_request_total, "\t", request_total
