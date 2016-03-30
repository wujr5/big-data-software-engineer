#!/usr/bin/python

import sys

pn1_list = []
temp_list = []

oldName = None

for line in sys.stdin:
  data = line.strip().split("\t")
  if len(data) != 2:
    continue
  imageName, ip = data

  if imageName[0:2] == "a_":
    pn1_list.append(ip)
    continue

  if oldName != None and oldName != imageName:
    intersection = [val for val in temp_list if val in pn1_list]
    print(oldName[2:], float(len(intersection)) / float(len(temp_list)))
    temp_list = []

  temp_list.append(ip)
  oldName = imageName

if oldName is not None:
  intersection = list(set(pn1_list) & set(temp_list))
  print(oldName[2:], float(len(intersection)) / float(len(temp_list)))
