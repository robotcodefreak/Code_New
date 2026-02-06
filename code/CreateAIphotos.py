#/home/jamie/Downloads/aiphotos
import shutil
from pathlib import Path
# Define source (Downloads/photos) and destination (VS Code project folder)
source_folder = Path.home() / "Downloads" / "aiphotos"
destination_folder = Path.home() / "Documents" / "VSCodeProject" / "images"

# Move folder
shutil.move(str(source_folder), str(destination_folder))

print(f"Moved {source_folder} to {destination_folder}")
|