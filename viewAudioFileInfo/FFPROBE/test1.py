#!/usr/bin/python3
import pandas as pd
import csv
import os, fnmatch
import subprocess as SP
import warnings
import re
warnings.filterwarnings("ignore", category=DeprecationWarning)

dirIn ="/home/jmajor/Music/Vangelis/Portraits (So Long Ago, So Clear)/"

streamList = "codec_name,sample_rate,duration,bit_rate"
streamTAGList = "" #"ARTIST,track,TITLE"
formatList = "" # "duration,size"

List = "File" + "," + streamList 
#+ "," + streamTAGList + \
#        "," + formatList
DFColumns = List.split(",")
if "" in DFColumns :
    DFColumns.remove("")

cmd="ffprobe -v error -show_streams "
cmd += re.escape(dirIn)
cmd += re.escape("07 I'll Find My Way Home.wma")
cmd = cmd.replace("'","\\'")
print(cmd)
SP.run(cmd, shell = True, executable="/bin/bash")

'''
df = pd.DataFrame(columns=DFColumns)
# show multiple values in packets with csv
commandPrefix = "ffprobe -v error -show_entries " 
#        "stream=codec_name,sample_rate,duration,bit_rate " + \
commandSuffix = "-print_format csv=item_sep=,:print_section=0 " 

pattern="*.*"

# List all files in dirIn folder
for filename in os.listdir(dirIn):
    f = os.path.join(dirIn, filename)
    # list only files with the proper match
    if fnmatch.fnmatch(filename,pattern):
        masterList =[filename]
        print(filename)
        if len(streamList) > 0 :
            # create the command for each file
            #cmd = commandPrefix + " stream=" + streamList + " " + \
            #    commandSuffix  + " '" + f + "'" 
            cmd = [commandPrefix,'stream='+streamList,\
                commandSuffix,f] 
            print(cmd)
           
            result = SP.run(cmd, capture_output = True,
                text=True,shell=True,executable="/bin/bash")
            masterList += result.stdout.strip().split(",")
            print(masterList)

        if len(streamTAGList) > 0 :
            # create the command for each file
            cmd = commandPrefix + " stream_tags=" + \
                streamTAGList + " " + \
                commandSuffix  + " '" + f + "'" 
            result = SP.run(cmd, capture_output = True,
                text=True,shell=True,executable="/bin/bash")
            masterList += result.stdout.strip().split(",")

        if len(formatList) > 0 :
            # create the command for each file
            cmd = commandPrefix + " format=" + \
                formatList + " " + \
                commandSuffix  + " '" + f + "'" 
            result = SP.run(cmd, capture_output = True,
                text=True,shell=True,executable="/bin/bash")
            masterList += result.stdout.strip().split(",")


        df.loc[len(df)] = masterList
       
print(df)
'''
