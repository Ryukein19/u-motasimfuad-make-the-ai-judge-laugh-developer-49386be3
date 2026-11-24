import os
# One-liner entry (107 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "The outage is not a bug. It is the system finally expressing how it feels about being deployed on a Friday."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
