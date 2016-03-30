#!/usr/bin/python

import sys

tableLine = ""
concatenate = False

for line in sys.stdin:
  if line[0:2] == "id":
    continue

  data = None
  if concatenate:
    tableLine = tableLine + line
    data = tableLine.strip().split("\t")
  else:
    data = line.strip().split("\t")

  if len(data) < 19:
    tableLine = tableLine + line
    concatenate = True
    continue
  elif len(data) == 19:
    tableLine = ""
    concatenate = False
    id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
    print(author_id, added_at)
