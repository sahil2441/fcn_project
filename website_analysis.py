
import json
import sys
import os, signal
import time
import psutil

PROCNAME = "chrome"

#input_path = '/Users/sahiljain/Google_Drive/SBU/Academics/Spring_16/CSE534/FCN_Project/git_code_self'
input_path = '~/Desktop/git_code/fcn_project'
input_file = 'websites_10.txt'



def analyze():
    # file = input_path + '/' + input_file
    # f=open(file)

    # Go to Resource directory
    os.chdir('/home/sahil/Desktop/git_code/fcn_project')
    os.system("sudo chmod -R 777 .")
	
    file = ['www.google.com', 'www.wikipedia.com']
    # 10 iterations
    for i in range(1):
        for line in file:
            website = line.strip()
            output_file = website + '.txt'
            os.system("/home/sahil/Desktop/Release/chrome "+website+" 2> " + output_file)
    	    time.sleep(2)
            for proc in psutil.process_iter():
   			  # check whether the process name matches
  			   if proc.name() == PROCNAME:
                    proc.kill()

    	# time.sleep(2)
	    print i
	    #exit()

if __name__ == '__main__':
    analyze()
