# main.py

import os
import json
from monitor.file_watcher import start_watching

LOG_FILE = 'activity_log.json'
WATCH_DIR = 'sample_watch_dir'

def handle_alert(alert):
    # Print the alert details
    print("\n[!] Suspicious Activity Detected:")
    print(f"    - Path: {alert['path']}")
    print(f"    - Event: {alert['event']}")
    print(f"    - Reason: {alert.get('reason', 'Unknown')}")
    print(f"    - Severity: {alert.get('severity', 'low')}")
    print(f"    - Time: {alert['timestamp']}")

    # Load existing alerts
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, 'r') as file:
                logs = json.load(file)
        except json.JSONDecodeError:
            logs = []
    else:
        logs = []

    # Append new alert
    logs.append(alert)

    # Write updated alerts
    with open(LOG_FILE, 'w') as file:
        json.dump(logs, file, indent=4)

if __name__ == '__main__':
    print("=== Endpoint Ransomware Behavior Analysis Engine ===\n")

    # Make sure watch directory exists
    if not os.path.exists(WATCH_DIR):
        os.makedirs(WATCH_DIR)

    print(f"[+] Watching directory: {os.path.abspath(WATCH_DIR)}\n")

    # Start monitoring
    start_watching(WATCH_DIR, callback=handle_alert)
