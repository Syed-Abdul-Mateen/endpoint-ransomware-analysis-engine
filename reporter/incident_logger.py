# reporter/incident_logger.py

import os
import json
from datetime import datetime

class IncidentLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.incidents = []

    def log(self, incident):
        self.incidents.append(incident)

    def save(self):
        if not self.incidents:
            print("[-] No incidents to save.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.log_dir, f"ransomware_incidents_{timestamp}.json")

        try:
            with open(filename, "w") as f:
                json.dump(self.incidents, f, indent=4, default=str)
            print(f"[+] Incident report saved: {filename}")
        except Exception as e:
            print(f"[!] Failed to save report: {e}")
