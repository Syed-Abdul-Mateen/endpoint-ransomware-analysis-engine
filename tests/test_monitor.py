# tests/test_monitor.py

import os
import time
import shutil
import unittest
from threading import Thread
from monitor.file_watcher import start_watching

class TestFileWatcher(unittest.TestCase):
    def setUp(self):
        self.test_dir = "tests/temp_watch"
        os.makedirs(self.test_dir, exist_ok=True)
        self.detected = []

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_file_modification_detection(self):
        def fake_callback(alert):
            self.detected.append(alert)

        # Start watcher in a separate thread
        watcher_thread = Thread(target=start_watching, args=(self.test_dir, fake_callback), daemon=True)
        watcher_thread.start()

        test_file = os.path.join(self.test_dir, "test.txt")

        # Create and modify file
        with open(test_file, "w") as f:
            f.write("initial content")

        time.sleep(1)

        with open(test_file, "w") as f:
            f.write("modified content")

        time.sleep(2)  # Let the watcher detect

        self.assertTrue(any("modified" in alert["event"].lower() for alert in self.detected))

if __name__ == "__main__":
    unittest.main()
