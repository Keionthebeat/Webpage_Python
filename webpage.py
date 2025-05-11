# How to check is a webpage is responding every 3 minutes and store the results for the past 24 hours in a log file. 

import os
import time
from datetime import datetime

webpage = "www.amazon.com"
log_file_path = "webpage_status.log"  # Define the log file name as a variable

for i in range(480):   # 24 * 60 / 3 = 480
    # Assuming Windows OS for the ping command. For Linux/macOS, use -c 1
    response = os.system(f"ping -n 1 {webpage}") 
    
    if response == 0:
        print(f"{webpage} is UP!")
        status = "UP!"
    else:
        print(f"{webpage} is DOWN!")
        status = "DOWN!"

    # Get current timestamp for each log entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    with open(log_file_path, "a") as log:  # Use the variable here
        log.write(f"{timestamp} - {webpage} status is {status}\n")
    
    if i < 479: # Don't sleep on the very last iteration
        time.sleep(180) # Wait for 3 minutes (180 seconds) before the next check
print("Monitoring complete after 24 hours.")