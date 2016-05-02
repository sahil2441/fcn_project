
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
	
    file = ["www.fc2.com",
                "www.netflix.com",
                "www.360.cn",
                "www.googleadservices.com",
                "www.stackoverflow.com",
                "www.amazon.de",
                "www.craigslist.org",
                "www.google.ca",
                "www.ok.ru",
                "www.adcash.com",
                "www.google.com.mx",
                "www.diply.com",
                "www.tianya.cn",
                "www.google.com.hk",
                "www.pornhub.com",
                "www.alibaba.com",
                "www.rakuten.co.jp",
                "www.naver.com",
                "www.amazon.co.uk",
                "www.google.com.tr",
                "www.adobe.com",
                "www.xinhuanet.com",
                "www.gmail.com",
                "www.outbrain.com",
                "www.xhamster.com"
            ]
    # 10 iterations
    for i in range(1):
        for line in file:
            website = line.strip()
            output_file = website + str(i) + '.txt'
            os.system("/home/sahil/Desktop/Release/chrome "+website+" 2> " + output_file)
            

if __name__ == '__main__':
    analyze()
