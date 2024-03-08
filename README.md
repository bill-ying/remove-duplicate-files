The program exams two folders, one source folder and one target folder, and removes duplicate files from the target folder if the same files are found in the source folder.

Following criteria are used to determine whether two files are identical:

- file names are the same
- file sizes are the same
- file contents are the same (by comparing SHA256 checksum)

Please note the timestamp is not compared.

The program depends on following package:
- Send2Trash

Usage:
- python duplicate_file_remover.py <source_folder> <target_folder>

Example:
- python duplicate_file_remover.py ~/source ~/target
