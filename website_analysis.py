
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
	
    file = [
        'http://www.cabotransfers.com',
        'http://www.ntz-holding.ru',
        'http://www.mathgameonline.net',
        'http://www.nanonano.me',
        'http://www.okcmar.org',
        'http://www.foodandseek.com.au',
        'http://www.yogateca.com',
        'http://www.mtaani.com',
        'http://www.romafamilywelcome.org',
        'http://www.magno-pulse.com'
        ]

    # 15 iterations
    for i in range(10):
        for line in file:
            website = line.strip()
            output_file = website + str(i) + '.txt'
            os.system("/home/sahil/Desktop/Release/chrome "+website+" 2> " + output_file)
            

if __name__ == '__main__':
    analyze()
