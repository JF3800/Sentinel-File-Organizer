import sys
import json
import shutil
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget
from PyQt6.QtCore import pyqtSignal, QObject
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SentinelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sentinel_File_Organizer")
        self.setMinimumSize(800,600)
        self.activity_feed = QListWidget(self)
        self.setCentralWidget(self.activity_feed)

file_detected = pyqtSignal(str)

class SentinelWatcher(QObject, FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        def on_created (self, event):
            self.file_detected.emit(event.src_path)
        



app = QApplication(sys.argv)
window = SentinelWindow()
window.show()
sys.exit(app.exec())