import os
from os.path import join
import subprocess
import pathlib
from bhl_born_digital_utils.config import get_config_setting

def clean_count(directory):
    """ Identify the MP4s and write to TXT """

    def topDir(listpath):
        count = 0 # Old, but it keeps the script from breaking. Fix later =/

        """ Run CMD from TXT """
        readlist = open(listpath,'r')
        print(readlist.read())
        print("-----------")

        ffmpeg_path = get_config_setting("ffmpeg", default="ffmpeg") # < Critical, need path to FFMPEG on your machine

        cmd = [
            ffmpeg_path,
            '-f', 'concat',
            '-safe', '0',
            '-i', abs_listpath,
            '-c', 'copy',
            out_file
        ]
        exit_code = subprocess.call(cmd)

        # deleting temporary input text file
        #os.remove(abs_listpath) # Not in the right spot, deletes before execution is finished
        
        return count
        
    """ END OF topDir """

    """ clean_count() ACTIONS """
    for paths in os.listdir(directory):
            media = []
            listpath = join(directory, 'list.txt')
            barcode = join(directory, paths) #Barcode folder paths
            filePath = barcode.lower()
    
    with open(listpath,'a') as f:
        for paths in os.listdir(directory):
            media = []
            barcode = join(directory, paths)
            filePath = barcode # Same thing, but not risking it right now =]
            if filePath.endswith('.mp4'):
                # Doesn't order properly if -10 or higher, ATM fix that manually
                f.write("file '"+filePath +"'\n")
            else:
                pass

    topDir(listpath)
    return paths
    """ END OF clean_count """

coll_input = input("Enter Package FOLDER Path: ")
directory = os.path.normpath(coll_input.strip('"\' '))
d = os.path.split(directory)
dname = d[-1] #package name
print(dname)
outmp4 = dname+".mp4" #out file name
out_file = join(directory,outmp4) #out file path

vid_list = 'list.txt'
listpath = join(directory, vid_list)
abs_listpath = os.path.abspath(listpath) # FFMPEG WILL NOT WORK WITHOUT THIS!!!


clean_count(directory)
