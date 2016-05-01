
import json
import sys
import os
import time


#input_path = '/Users/sahiljain/Google_Drive/SBU/Academics/Spring_16/CSE534/FCN_Project/git_code_self'
input_path = '~/Desktop/git_code/fcn_project'
input_file = 'websites_all.txt'

def analyze():
    file = input_path + '/' + input_file
#    f=open(file)

    # Go to Resource directory
    os.chdir('/home/sahil/Desktop/git_code/fcn_project')
	
    # file = ['www.google.com']
    # 10 iterations
    for i in range(1):
        for line in file:
            website = line.strip()
            output_file = website + '.txt'
            os.system("/home/sahil/Desktop/Release/chrome "+website+" 2> " + output_file)
    	    time.sleep(3)
            os.system("pkill chromium")
	    # exit()

if __name__ == '__main__':
    analyze()
