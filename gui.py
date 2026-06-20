import sys
import time
import json
import shutil
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt6.QtCore import pyqtSignal, QObject
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SentinelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sentinel_File_Organizer")
        self.setMinimumSize(800,600)
        self.activity_feed = QListWidget(self)
        
    #Layout, Right Side 
        self.Rlayout = QWidget()
        self.Llayout = QWidget()
        self.M_Layout = QHBoxLayout()
        self.R_panel = QWidget()
        self.L_Layout = QVBoxLayout()
        self.R_Layout = QVBoxLayout()
        self.label = QLabel("Status")
        self.widget = QListWidget()
        self.feed_label = QLabel("Activity Feed")
        self.undo = QPushButton("Undo")
        self.L_Layout.addWidget(self.feed_label)
        self.L_Layout.addWidget(self.activity_feed)
        self.R_Layout.addWidget(self.label)
        self.R_Layout.addWidget(self.widget)
        self.R_Layout.addWidget(self.undo)
        self.Llayout.setLayout(self.L_Layout)
        self.R_panel.setLayout(self.R_Layout)
        self.M_Layout.addWidget(self.Llayout)
        self.M_Layout.addWidget(self.R_panel)
        self.Rlayout.setLayout(self.M_Layout)   
        self.setCentralWidget(self.Rlayout)

        self.watcher = SentinelWatcher()
        self.observer = Observer()

        self.observer.schedule(self.watcher, "/home/anoynmous/Downloads" , recursive=False)
        self.observer.start()

        self.watcher.file_detected.connect(self.add_to_feed)
    def add_to_feed(self, file_path):
        self.activity_feed.addItem(file_path)
            


class SentinelWatcher(QObject, FileSystemEventHandler):
    file_detected = pyqtSignal(str)
    def __init__(self):
        super().__init__()
    def on_created (self, event):
        self.file_detected.emit(event.src_path)
        



app = QApplication(sys.argv)
window = SentinelWindow()
window.show()
sys.exit(app.exec())