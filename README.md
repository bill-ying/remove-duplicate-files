The program exams the source folder and target folder, and removes duplicate files.  If the same file in the target folder is found in the source folder, and all the following conditions are met, the file in target folder will be removed:

- fila names are the same
- file sizes are the same
- file contents are the same (by comparing SHA256 checksum)

The timestamp is not compared.

Example:

- python duplicate_file_remover.py <source_folder> <target_folder>

