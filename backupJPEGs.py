#!/usr/bin/env python3

#required modules
import os
import shutil
import argparse


#defines a path within the argument parser
#also ensures the path exists
def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

def copyAllFiles(inFile, outFile):
    #gets all individual files within input folder
    files = os.listdir(inFile)

    #if folder contains subfolders
    try:
        #if no subfolders this will break the try
        for file in files:
            allImgs = os.listdir(inFile + '\\' + file)

            #if subfolder does not exist within output folder create it
            if  not os.path.exists(outFile + '\\' + file):
                os.mkdir(outFile + '\\' + file)

            #copies each file which ends with .jpg
            for image in allImgs:
                if image.endswith('.JPG'):
                    shutil.copy(inFile + '\\' + file + '\\' + image, outFile + '\\' + file)
                    print('image copied: ' + image)

    #if no subfolders
    except:
        for image in files:
            if image.endswith('.JPG'):
                shutil.copy(inFile + '\\' +  image, outFile + '\\' + image)
                print('image copied: ' + image)

#creates argument parser
parser = argparse.ArgumentParser()
parser.add_argument("inputFile", type=dir_path, help="file containing both JPEGs and other files")
parser.add_argument("outputDest", type=dir_path, help="destination file which will be filled with JPEGs from input file")
#captures arguments
args = parser.parse_args()


#creates a list of files within the input directory



copyAllFiles(args.inputFile, args.outputDest)


#debugging outputs
#print(os.path.exists(args.inputFile))
#print(os.path.exists(args.outputDest))

#print(args.inputFile)
#print(args.outputDest)
