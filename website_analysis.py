
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
    os.chdir('/home/sahil/Desktop/git_code/fcn_project/apache_tomcat')
    os.system("sudo chmod -R 777 .")
	
    # file = [
    #     'www.cabotransfers.com',
    #     'www.ntz-holding.ru',
    #     'www.mathgameonline.net',
    #     'www.nanonano.me',
    #     'www.okcmar.org',
    #     'www.foodandseek.com.au',
    #     'www.yogateca.com',
    #     'www.mtaani.com',
    #     'www.romafamilywelcome.org',
    #     'www.magno-pulse.com',
    #     ]

    # 15 iterations
    # file = [
    #     'www.huffingtonpost.com',
    #     'www.thedailybeast.com',
    #     'www.lifehacker.com',
    #     'www.gawker.com',
    #     'www.techcrunch.com',
    #     'www.engadget.com',
    #     'www.cheezburger.com'
    # ]

    file = [
            '172.24.17.204:8080/accu',
            '172.24.17.204:8080/youtube',
            '172.24.17.204:8080/images'
    ]

    for i in range(25):
        for line in file:
            website = line.strip()
            file_name = website.translate(None, ':/')
            output_file = file_name + str(i) + '.txt'
            os.system("/home/sahil/Desktop/Release/chrome "+website+" 2> " + output_file)
            

if __name__ == '__main__':
    analyze()
