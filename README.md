# make1dip.py
Merges multiple MP4 files for a single package.

Currently, if there are more than 10 files to be merged, and if the file names include integers that indicate the order, leading zeros must be included inorder to retain the original order.

For example: 
- FILE_NAME-001.mp4 
- FILE_NAME-002.mp4 
- FILE_NAME-003.mp4 
- FILE_NAME-004.mp4 
- FILE_NAME-005.mp4 
- FILE_NAME-006.mp4 
- FILE_NAME-007.mp4 
- FILE_NAME-008.mp4 
- FILE_NAME-009.mp4 
- FILE_NAME-010.mp4 

Once the script has finished executing, delete the 'list.txt' file from the directory.
