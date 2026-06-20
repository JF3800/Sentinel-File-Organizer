from pathlib import Path
import shutil

source = Path("/home/anoynmous/Downloads/Certificate #1 (Python)")
destination = Path("/home/anoynmous/Documents/Certificates")
destination.mkdir(parents = True, exist_ok = True)

shutil.move(source , destination)