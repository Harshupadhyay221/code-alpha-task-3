import os
import shutil

path = input("Enter Path: ").strip()  # Use strip() to remove leading/trailing whitespaces

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    
    if extension:
        destination_dir = os.path.join(path, extension[1:])
    else:
        destination_dir = os.path.join(path, "NoExtension")

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    shutil.move(os.path.join(path, file), os.path.join(destination_dir, file))
