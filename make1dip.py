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


        # with open(listpath,'r') as f:
            # f.readlines()
            # print(f.readlines())
            # print(f.read())
            # print(f.readline())
            # print("-----------")

        # for x in media:
        #     count +=1

        """ my attmempt below """
        ##https://github.com/bentley-historical-library/bhl_born_digital_utils/blob/f5e1ea8aa253bedef65412f21efbec4e449e879a/bhl_born_digital_utils/make_dips.py#L44

        # ffmpeg_path = get_config_setting("ffmpeg", default="ffmpeg")

        #https://github.com/kkroening/ffmpeg-python/issues/251#issuecomment-623913956

        #.run(cmd='/path_to/ffmpeg',capture_stdout=True)
        #https://github.com/kkroening/ffmpeg-python/issues/251#issuecomment-623913956

        # ffmpeg_path = pathlib.Path().resolve("ffmpeg")

        #PermissionError: [Errno 13] Permission denied: PosixPath('/Users/maryse/Desktop')
        # print(ffmpeg_path)

        #https://stackoverflow.com/questions/65836756/python-ffmpeg-wont-accept-path-why
        # (
        # ffmpeg
        # .concat(input_video, merged_audio, v=1, a=1)
        # .output("mix_delayed_audio.mp4")
        # .run(overwrite_output=True, cmd=r'c:\FFmpeg\bin\ffmpeg.exe')
        # )


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

        #"list.txt": No such file or directory
        #https://github.com/bramp/ffmpeg-cli-wrapper/issues/147


        """ BHL baroque example """
        #https://github.com/bentley-historical-library/baroque/blob/1325e4a7270be9e929325505a550c553692111a7/baroque/wav_bext_chunk_validation.py#L42

        # cmd = [bwfmetaedit_path, "--out-core", path_to_wav]
        # bwfmetaedit_csv = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        #
        # subprocess.call('ffmpeg.exe -f concat -i list.txt -c copy outcome.mp4')

        """ EXAMPLE """
        ## https://stackoverflow.com/questions/56920546/combine-mp4-files-by-order-based-on-number-from-filenames-in-python/56931581


        # return count
        return results
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
