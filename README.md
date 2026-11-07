# Folder File List to CSV

An educational project: a Python console application that generates a CSV table containing the names and sizes of files in a selected folder.

## What the Program Does

1. Prompts the user to enter a folder path.
2. Retrieves the list of files (subfolders are skipped).
3. Gets the name and size of each file in bytes and displays them in the console.
4. Saves the table as a CSV file named `<folder_name>.csv` in the current working directory and displays the file path.


## How to Run

### From Source Code

Python 3.14 is required. No third-party libraries are needed.

```bash
python file_list.py
```

On macOS and Linux:

```bash
python3 file_list.py
```

### Pre-built Executable (Windows)

Download `file_list.exe` from the Releases section and launch it by double-clicking. No Python installation is required.

## Example Output

```text
Enter folder path: C:\Users\NoName\Documents

Files found: 3

report.docx                                          24576 bytes
notes.txt                                             1024 bytes
photo.jpg                                          2097152 bytes

File saved: C:\Users\NoName\Desktop\Documents.csv
```

CSV file contents:

```csv
Name;Size
report.docx;24576
notes.txt;1024
photo.jpg;2097152
```

## Project Structure

- `file_list.py` — application source code
- `file_list.exe` — compiled Windows executable

## About the Project

An educational assignment completed as part of a work placement.