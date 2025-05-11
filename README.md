# Webpage Status Monitor

This Python script monitors the status of a specified webpage by pinging it every 3 minutes. The status (UP or DOWN) along with a timestamp is logged into a file named `webpage_status.log`. The script runs for 24 hours.

## Prerequisites

- Python 3.x
- Access to the command line/terminal to run the script.
- The `ping` command must be available in your system's PATH. The script currently uses the Windows version of ping (`ping -n 1`). For Linux or macOS, you would need to modify the ping command to `ping -c 1`.

## How to Run

1.  **Clone the repository or download the script.**
2.  **Open a terminal or command prompt.**
3.  **Navigate to the directory where `webpage.py` is located.**
    ```bash
    cd path/to/your/script
    ```
4.  **Run the script:**
    ```bash
    python webpage.py
    ```

The script will start monitoring `www.amazon.com` (by default) and create/append to `webpage_status.log` in the same directory.

## Configuration

-   **Webpage to Monitor**: You can change the webpage to monitor by modifying the `webpage` variable in `webpage.py`:
    ```python
    webpage = "www.yourtargetwebpage.com"
    ```
-   **Log File Name**: The log file name can be changed by modifying the `log_file_path` variable:
    ```python
    log_file_path = "my_custom_log_name.log"
    ```
-   **Monitoring Interval and Duration**:
    -   The script checks the webpage every 3 minutes (`time.sleep(180)`).
    -   It runs for 24 hours (480 iterations).
    -   These can be adjusted by changing the `time.sleep()` duration and the `range(480)` in the main loop.

## Log File

The log file (`webpage_status.log` by default) will contain entries in the following format:

```
YYYY-MM-DD HH:MM:SS - <webpage_url> status is <STATUS>
```

Example:

```
2025-10-27 10:00:00 - www.amazon.com status is UP!
2025-10-27 10:03:00 - www.amazon.com status is UP!
2025-10-27 10:06:00 - www.amazon.com status is DOWN!
```

## Operating System Compatibility

The current ping command `ping -n 1 {webpage}` is for **Windows**.

-   For **Linux or macOS**, change line 12 in `webpage.py` to:
    ```python
    response = os.system(f"ping -c 1 {webpage}")
    ```
