import time
import json
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SentinelHandler(FileSystemEventHandler):
    def on_created (self, event):
        file = Path(event.src_path)
        with open("/home/anoynmous/Documents/Sentinel-File-Organizer/config.json", "r") as f:
            rules = json.load(f)
            for rule in rules:
                if file.suffix == rule["file_type"]:
                    destination = Path(rule["destination"])
                    destination.mkdir(parents = True, exist_ok = True)
                    shutil.move(file, destination)
        print(event.src_path)

handler = SentinelHandler()
observer = Observer()

observer.schedule(handler, "/home/anoynmous/Downloads" , recursive = False)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()