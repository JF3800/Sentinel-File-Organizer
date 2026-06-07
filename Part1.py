from pathlib import Path
import shutil
folder = Path("/home/anoynmous/Downloads")

for item in folder.iterdir():
    if item.is_file():
        print(f"{item.name} | {item.suffix} | {item.stat().st_size}")

