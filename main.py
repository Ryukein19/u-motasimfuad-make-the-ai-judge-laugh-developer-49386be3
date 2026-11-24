import os
# One-liner entry: the line below is the whole submission.
LINE = "The outage is not a bug. It is the system finally expressing how it feels about being deployed on a Friday."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
