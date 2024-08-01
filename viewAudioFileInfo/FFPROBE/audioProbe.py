#!/usr/bin/python3
import pandas as pd
import csv
import os, fnmatch
import subprocess as SP
import xml.etree.ElementTree as ET
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


df = pd.DataFrame(columns=["file","codec_name","sample_rate",\
        "duration","bit_rate"])
tree = ET.parse('../config.xml')
root = tree.getroot()
dirIn = "/home/jmajor/gitHub/pyQt6Test/viewAudioFileInfo/" + \
        str(tree.find("dirIn").text)
dirOut = "/home/jmajor/gitHub/pyQt6Test/viewAudioFileInfo/" + \
        str(tree.find("dirOut").text)

dirIn ="/home/jmajor/Music/Boy2"
command = "ls " + dirIn
command = "ls " + dirOut

#SP.run(command, shell = True,executable="/bin/bash")

# iterate over files in
# that directory

## show one value in frame
'''
command = "ffprobe -v error -show_entries " + \
        "format=size " + \
        "-print_format " + \
        "default=noprint_wrappers=1:nokey=1"
'''
'''
# show multiple values in frame with csv
command = "ffprobe -v error -show_entries " + \
        "format=size,bit_rate " + \
        "-print_format csv=item_sep=,:print_section=0 " 
'''


# show multiple values in packets with csv
command = "ffprobe -v error -show_entries " + \
        "stream=codec_name,sample_rate,duration,bit_rate " + \
        "-print_format csv=item_sep=,:print_section=0 " 

pattern="*.ogg"

for filename in os.listdir(dirIn):
   f = os.path.join(dirIn, filename)
   if fnmatch.fnmatch(filename,pattern):
        cmd = command + " '" + f + "'" 
        result = SP.run(
                cmd, 
                capture_output = True,
                text=True,
                shell=True,
                executable="/bin/bash")
        listResult = result.stdout.strip().split(",")
        listResult.insert(0,filename)
        df.loc[len(df)] = listResult
        #print(filename," - ",result.stdout.strip())
       
print(df)
