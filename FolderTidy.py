import os
import shutil
from pathlib import Path

class FileSorter:
    def __init__(self):
        self.folders = {
            "Pics": [".jpg", ".png", ".gif"],
            "Docs": [".pdf", ".doc", ".txt"],
            "Zips": [".zip", ".rar"],
            "Music": [".mp3", ".wav"],
            "Vids": [".mp4", ".mov"],
            "Apps": [".exe", ".msi"],
            "Code": [".py", ".js"]
        }
        
    def clean_up(self, folder_path="~/Downloads"):
        try:
            target = Path(folder_path).expanduser().absolute()
            
            print(f"\nSorting stuff in: {target}")
            
            for folder_name in self.folders:
                os.makedirs(target / folder_name, exist_ok=True)
            
            os.makedirs(target / "Misc", exist_ok=True)
            
            moved_count = 0
            
            for thing in target.iterdir():
                if thing.is_file():
                    ext = thing.suffix.lower()
                    found_home = False
                    
                    for folder_name, extensions in self.folders.items():
                        if ext in extensions:
                            new_path = target / folder_name / thing.name
                            shutil.move(str(thing), str(new_path))
                            moved_count += 1
                            found_home = True
                            break
                    
                    if not found_home:
                        new_path = target / "Misc" / thing.name
                        shutil.move(str(thing), str(new_path))
                        moved_count += 1
            
            print(f"\nSorted {moved_count} files.")
            print("Made these folders:")
            for folder_name in self.folders:
                print(f"- {folder_name}")
            print("- Misc")
            
        except Exception as e:
            print(f"\nOops! {str(e)}")

def run_sorter():
    print("\n=== Messy Folder Fixer ===")
    print("I'll organize your messy folder\n")
    
    sorter = FileSorter()
    
    while True:
        print("\nPick:")
        print("1. Clean Downloads")
        print("2. Pick another folder")
        print("3. Quit")
        
        choice = input("\nWhat you want? (1-3): ")
        
        if choice == "1":
            sorter.clean_up()
        elif choice == "2":
            custom_path = input("Folder path: ")
            sorter.clean_up(custom_path)
        elif choice == "3":
            print("\nLater! Your files are neat now.")
            break
        else:
            print("\nHuh? Try 1, 2 or 3")

if __name__ == "__main__":
    run_sorter()