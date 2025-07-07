# monitor/file_watcher.py

import os
import time
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RansomwareFileWatcher(FileSystemEventHandler):
    def __init__(self, watch_dir, suspicious_extensions=None, callback=None):
        self.watch_dir = watch_dir
        self.callback = callback
        self.suspicious_extensions = suspicious_extensions or ['.locked', '.enc', '.crypto']
        self.file_hashes = {}

    def on_modified(self, event):
        if event.is_directory:
            return
        self.detect_change(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            return
        self.detect_change(event.src_path)

    def on_moved(self, event):
        if event.is_directory:
            return
        # Detect suspicious file renaming
        if self.is_suspicious_extension(event.dest_path):
            alert = {
                "event": "Suspicious rename",
                "path": event.dest_path,
                "timestamp": time.ctime()
            }
            if self.callback:
                self.callback(alert)

    def is_suspicious_extension(self, file_path):
        _, ext = os.path.splitext(file_path)
        return ext.lower() in self.suspicious_extensions

    def detect_change(self, file_path):
        try:
            if not os.path.isfile(file_path):
                return
            with open(file_path, 'rb') as f:
                content = f.read()
                new_hash = hashlib.md5(content).hexdigest()

            old_hash = self.file_hashes.get(file_path)
            if old_hash and old_hash != new_hash:
                # Content modified
                alert = {
                    "event": "File content modified",
                    "path": file_path,
                    "timestamp": time.ctime()
                }
                if self.callback:
                    self.callback(alert)
            self.file_hashes[file_path] = new_hash
        except Exception as e:
            print(f"[!] Error watching file: {e}")

def start_watching(directory, callback=None):
    event_handler = RansomwareFileWatcher(directory, callback=callback)
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=True)
    observer.start()
    print(f"[+] Monitoring directory: {directory}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
