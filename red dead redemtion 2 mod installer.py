import os
import shutil

def install_mod(mod_folder, install_location):
    mod_files = os.listdir(mod_folder)
    for file in mod_files:
        shutil.copy(os.path.join(mod_folder, file), install_location)
    print("Mod installed successfully")

mod_folder = input("Enter the path to the mod folder:")
install_location = input("Enter the path to the installation location:")
install_mod(mod_folder, install_location)
