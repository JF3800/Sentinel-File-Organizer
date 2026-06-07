import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SentinelHandler(FileSystemEventHandler):
    def on_created (self, event):
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