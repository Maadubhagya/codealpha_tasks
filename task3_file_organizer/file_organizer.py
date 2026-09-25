import os
import shutil
source_folder="sources"
destination_folder="jpg_images"
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path=os.path.join(source_folder,file)
        destination_path=os.path.join(destination_folder,file) 
        shutil.move(source_path,destination_path)
print("All JPG files moved successfully")
        
       