""" 
Author: Celia M. Pacheco
Date: Feb 7th 2017
Assignment: HW 1
Brief: This script creates the files needed for grading 107
created on Feb 7th 2017 by Celia Pacheco
Todo: parse file better to account for lines that are only new line
"""
#!/usr/bin/env python3
import sys
import os
from shutil import copy2

def usage(test_case):
    """ usage of script 
    test_case: a test parameter 
    """
    print("Usage: graderlist.txt rubric.odt")
    print("graderlist.txt should be a file of the students and assigned graders")
    print("Create this by first running pdftotext -layout graderlist.pdf ")

def main():
    """ main function"""
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        rubric = sys.argv[2]
        sfiles = [] #student file names
        with open(filename, "r") as f:
            #used to get past first few empty lines
            f.readline()
            f.readline()
            f.readline()
            row = f.readlines()
            for col in range(0, 20): #this should be fixed later to parse correctly
                tmp = row[col].split()
                #this should be changed to work with any user 
                if tmp[2] == "Celia":
                    sfiles.append(tmp[0])
            for name in sfiles:
                os.mkdir(name) #create file
                dst = "{}/{}_{}".format(name, name, rubric)
                copy2(rubric, dst) #copy rubric to file
        sys.exit(0)
    else:
        usage()
        sys.exit(1)
if __name__ == "__main__":
    main()
