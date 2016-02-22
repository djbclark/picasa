#!/usr/bin/env python2

# Import the os module, for the os.walk function
import os

# Import Regexp module
import re

#Import JSON module
import json

# Set the directory you want to start from
rootDir = '/Users/djbclark/Stuff/Photos'
datalist = list()
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname=="Picasa.ini" or fname==".picasa.ini": 
            fullfname = dirName+'/'+fname
            foldername = dirName
            #print('processing foldername: %s' % (foldername, ))
            print('processing: %s' % (fullfname, ))
            fhand = open(fullfname)
            header = ''
            for line in fhand:
                line = line.strip()
                if len(line) ==0 : continue
                if line.startswith('[') : 
                    header = line.strip('[] ')
                else : 
                    datarow = dict()
                    action = line
                    datarow['folder'] = foldername
                    datarow['header'] = header
                    datarow['action'] = action
                    datarow['file'] = fullfname
                    datalist.append(datarow)



with open('picasa.ini.json', 'w') as outfile:
    json.dump(datalist, outfile)



# Now get faces info from the files themselves. This is an
# option in Picasa preferences, and once you turn it on you'll
# never have full state in either place again. Note there
# are an abundance of python exif modules, none of which work
# well, hence just have exiftool installed and in PATH and...

print "Now running exiftool, this could take a while..."
cmd = "exiftool -ignoreMinorErrors -duplicates -json -xmp:regionname -r \"" + rootDir + "\" > exiftool.json 2>/dev/null"
os.system(cmd)