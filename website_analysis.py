
import json
import sys
import os


input_path = '/Users/sahiljain/Google_Drive/SBU/Academics/Spring_16/CSE534/FCN_Project/git_code_self'
input_file = 'mixed2.txt'

def analyze():
    file = input_path + '/' + input_file
    f=open(file)

    # Go to Resource directory
    os.system("cd ~/Desktop/Resource")

    for line in f:
        website = line.strip()
        output_file = website + '.txt'
        os.system("./chrome "+website+" > " + output_file)
        # os.system("pkill chrome")

    f.close()

if __name__ == '__main__':
    analyze()