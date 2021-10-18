# https://pythonprogramming.altervista.org/join-all-mp4-with-python-and-ffmpeg/
#https://python-forum.io/thread-7009.html
### https://kkroening.github.io/ffmpeg-python/

import os
from os.path import join
import subprocess
import pathlib
# pathlib.Path(_file_).parent.resolve()
# pathlib.Path().resolve()

# def clean_count(directory):
def clean_count(directory):
    """ Identify the MP4s and write to TXT """

    def topDir(listpath):
        total_size = 0 # individual sizes
        count = 0

        """ Run CMD from TXT """
        readlist = open(listpath,'r')
        print(readlist.read())
        print("-----------")


        # for x in media:
        #     count +=1

        """ my attmempt below """


        # cmd = [
        #     ffmpeg_path,
        #     '-f', 'concat',
        #     '-safe', '0',
        #     '-i', tmp_list,
        #     '-c', 'copy',
        #     out_filepath
        # ]
        #exit_code = subprocess.call(cmd)

        # cmd = ["ffmpeg", "-f", "concat", "-i", "%s" % vid_list, "-c", "copy", "%s" % out_file]
        ffmpeg_path = "PATH|TO|FFMPEG\"
        cmd = [
            ffmpeg_path,
            '-f', 'concat',
            '-safe', '0',
            '-i', "%s" % vid_list,
            "-c", "copy",
            "%s" % out_file
        ]
        exit_code = subprocess.run(cmd)
        # os.remove(vid_list)
        results = [barcode,exit_code]

        
        return count
        #return results
    """ END OF topDir """


    """ clean_count() ACTIONS """

    """ Don't alter below """
    with open(listpath,'a') as f:
        for paths in os.listdir(directory):
            media = []
            barcode = join(directory, paths) #Barcode folder paths
            # filePath = barcode.lower()
            filePath = barcode
            if filePath.endswith('.mp4'):
                f.write(filePath +'\n')
            else:
                pass
        """ Don't alter above"""
        # print(filePath)
    # print("Loading list.txt file")
    # time.sleep(10)

    topDir(listpath) #KEEP!!!



    return paths
    """ END OF clean_count """

""" GLOBAL VARS """
# path = input("Enter the Directory: ")

directory = 'PATH\TO\COLL'
d = os.path.split(directory)
dname = d[-1] #out_file name
out_file = dname+".mp4"

vid_list = 'list.txt'
listpath = join(directory, vid_list)

# print(dname)
# path = r'WINDOWS\PATH\'
# coll_input = input("Enter Collection Number: ")
# collnum = str(coll_input)
# coll = "R_"+collnum
#directory = join(path,coll)

clean_count(directory)
