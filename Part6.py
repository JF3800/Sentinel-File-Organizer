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
            config = json.load(f)
            rules = config["rules"]
            for rule in rules:
                if file.suffix == rule["file_type"]:
                    destination = Path(rule["destination"])
                    destination.mkdir(parents = True, exist_ok = True)
                    shutil.move(file, destination)
                    config["history"].append({"source": str(file), "destination":str(destination)})
                    with open("/home/anoynmous/Documents/Sentinel-File-Organizer/config.json", "w") as f:
                        json.dump(config, f)
                    
        print(event.src_path)

def undo_last ():
    with open("/home/anoynmous/Documents/Sentinel-File-Organizer/config.json", "r") as f:
        config = json.load(f)
        if len(config["history"]) == 0:
            print("Nothing To Undo")
            return
        last_move = config["history"][-1]
        shutil.move(Path(last_move["destination"])/ Path(last_move["source"]).name, last_move["source"])
        config["history"].pop(-1)
        with open("/home/anoynmous/Documents/Sentinel-File-Organizer/config.json", "w") as f:
            json.dump(config, f)

handler = SentinelHandler()
observer = Observer()

observer.schedule(handler, "/home/anoynmous/Downloads" , recursive = False)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()