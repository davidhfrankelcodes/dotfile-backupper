# main.py
import os
import shutil
import subprocess
import yaml
from datetime import datetime

def read_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        exit(1)

def copy_files(files_list, dest_folder):
    try:
        for file_path in files_list:
            # Create destination folder if it doesn't exist
            os.makedirs(dest_folder, exist_ok=True)
            
            # Copy file to destination folder
            shutil.copy2(file_path, dest_folder)
    except Exception as e:
        print(f"Error copying files: {e}")
        exit(1)

def is_git_repository(path):
    try:
        subprocess.run(["git", "-C", path, "status"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def git_operations(path):
    try:
        # Initialize the directory as a Git repository if it isn't already
        if not is_git_repository(path):
            subprocess.run(["git", "-C", path, "init"], check=True)
        
        # Run git add
        subprocess.run(["git", "-C", path, "add", "."], check=True)
        
        # Create a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
        
        try:
            # Run git commit
            subprocess.run(["git", "-C", path, "commit", "-m", f"Automatic Push {timestamp}"], check=True)
        except subprocess.CalledProcessError as e:
            print("No changes to commit.")
        
        # Run git push
        subprocess.run(["git", "-C", path, "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operations: {e}")
        exit(1)


if __name__ == "__main__":
    # Path to the YAML file relative to this script
    script_dir = os.path.dirname(__file__)
    yaml_file_path = os.path.join(script_dir, "config.yaml")
    
    # Read YAML file to get the list of files and destination folder
    config = read_yaml(yaml_file_path)
    files_list = config.get('dotfiles', [])
    dest_folder = config.get('destination_folder', 'default/folder/path')
    
    if not files_list:
        print("No files specified for backup in the YAML file.")
        exit(1)
    
    if not dest_folder:
        print("No destination folder specified in the YAML file.")
        exit(1)
    
    # Copy files to the backup folder
    copy_files(files_list, dest_folder)
    
    # Run Git operations
    git_operations(dest_folder)
