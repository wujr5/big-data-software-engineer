#!/usr/bin/python

import sys

for line in sys.stdin:
  data = line.strip().split(" ")
  if len(data) == 10:
    ip, hyphen1, hyphen2, date, number1, request, path, http, status, number2 = data
    if (float(status) == 404):
      print ip, "\t", status
