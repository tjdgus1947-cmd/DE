import time
import sys

log_path = "/log/app.log"

with open(log_path, "r") as f:
    f.seek(0, 2)
    print("Started watching the log file...")
    while True:
        line = f.readline()
        if line:
            print("[LOG] " + line.strip())
            sys.stdout.flush()  
        else:
            time.sleep(1)