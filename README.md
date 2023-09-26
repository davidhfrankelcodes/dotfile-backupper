# Dotfile Backupper

## Overview

`Dotfile Backupper` is a Python script designed to automate the backup of your dotfiles to a Git repository. The script copies a list of dotfiles specified in a YAML configuration file to a destination folder and then performs `git add`, `git commit`, and `git push` operations.

## Features

- Copy dotfiles to a specified backup folder
- Initialize a Git repository in the backup folder if it doesn't exist
- Add all files to staging
- Commit changes with a timestamp
- Push changes to a remote repository

## Prerequisites

- Python 3.x and PyYAML (Install with `pip install PyYAML`)
- Git

## Installation

1. Clone this repository or download the script.
2. Place the `config.yaml` file in the same directory as the script, or update the script to point to your custom `config.yaml` file location.
3. Make sure Git is installed and accessible from the command line.

## Configuration

To specify which files to back up and where to place them, edit the `config.yaml` file.

Example:

```yaml
dotfiles:
  - /home/user/.bashrc
  - /home/user/.vimrc
  - /home/user/.gitconfig
destination_folder: /path/to/your/backup/folder
```

## Usage

Run the script using Python:

```bash
python main.py
```

Alternatively, make the script executable and run it:

```bash
chmod +x main.py
./main.py
```

## Error Handling

The script has built-in error handling for:

- Reading the YAML configuration file
- Copying files to the destination folder
- Running Git operations

If any of these steps fail, the script will output an error message and terminate.
