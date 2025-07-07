# analyzer/behavior_analyzer.py

import time
from collections import defaultdict

class BehaviorAnalyzer:
    def __init__(self):
        self.events = defaultdict(list)

    def analyze(self, alert):
        path = alert["path"]
        event_type = alert["event"]
        timestamp = time.time()

        self.events[path].append((event_type, timestamp))

        # Basic detection rules
        if self.is_suspicious_activity(path):
            return {
                "path": path,
                "event": event_type,
                "timestamp": alert["timestamp"],
                "severity": "high",
                "reason": "Multiple rapid changes detected (possible ransomware)"
            }
        elif event_type == "Suspicious rename":
            return {
                "path": path,
                "event": event_type,
                "timestamp": alert["timestamp"],
                "severity": "medium",
                "reason": "File renamed to suspicious extension"
            }
        elif event_type == "File content modified":
            return {
                "path": path,
                "event": event_type,
                "timestamp": alert["timestamp"],
                "severity": "low",
                "reason": "File content was changed"
            }

        return None

    def is_suspicious_activity(self, path):
        timestamps = self.events[path]
        if len(timestamps) < 3:
            return False
        # Check if 3+ events occurred within 5 seconds
        recent = [ts for event, ts in timestamps[-5:] if time.time() - ts < 5]
        return len(recent) >= 3
