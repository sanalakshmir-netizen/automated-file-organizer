# Automated File Organizer

A Python-based file organizer that automatically sorts files into folders based on their file extensions.

## Features

- Organizes images, documents, videos, audio files, spreadsheets, and archives
- Automatically creates category folders
- Prevents duplicate files from being overwritten
- Handles permission and operating system errors
- Skips unknown file types
- Displays a summary after organizing files

## File Categories

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp` |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov` |
| Audio | `.mp3`, `.wav`, `.aac` |
| Spreadsheets | `.xls`, `.xlsx`, `.csv` |
| Archives | `.zip`, `.rar`, `.7z` |

## Requirements

- Python 3.x
- No external Python packages required

## How to Run

1. Open the project folder in a terminal.
2. Make sure the folder you want to organize is named `Downloads`.
3. Run:

```bash
python organizer.py
