
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
	
    file = ["www.google.com",
        "www.facebook.com",
        "www.youtube.com",
        "www.baidu.com",
        "www.yahoo.com",
        "www.amazon.com",
        "www.wikipedia.org",
        "www.qq.com",
        "www.taobao.com",
        "www.twitter.com",
        "www.google.co.in",
        "www.live.com",
        "www.sina.com.cn",
        "www.linkedin.com",
        "www.weibo.com",
        "www.yahoo.co.jp",
        "www.google.co.jp",
        # "www.ebay.com",
        # "www.yandex.ru",
        # "www.vk.com",
        # "www.blogspot.com",
        # "www.tmall.com",
        # "www.google.de",
        # "www.hao123.com",
        # "www.t.co",
        # "www.msn.com",
        # "www.instagram.com",
        # "www.google.co.uk",
        # "www.bing.com",
        # "www.amazon.co.jp",
        # "www.reddit.com",
        # "www.google.com.br",
        # "www.google.fr",
        # "www.sohu.com",
        # "www.aliexpress.com",
        # "www.ask.com",
        # "www.mail.ru",
        # "www.google.ru",
        # "www.onclickads.net",
        # "www.pinterest.com",
        # "www.wordpress.com",
        # "www.tumblr.com",
        # "www.paypal.com",
        # "www.imgur.com",
        # "www.xvideos.com",
        # "www.google.it",
        # "www.apple.com",
        # "www.microsoft.com",
        # "www.imdb.com",
        # "www.google.es",
        # "www.fc2.com",
        # "www.netflix.com",
        # "www.360.cn",
        # "www.googleadservices.com",
        # "www.stackoverflow.com",
        # "www.amazon.de",
        # "www.craigslist.org",
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
        "www.xhamster.com",
        "www.detail.tmall.com",
        "www.soso.com",
        "www.google.co.id",
        "www.ebay.de",
        "www.kat.cr",
        "www.people.com.cn",
        "www.google.pl",
        "www.jd.com",
        "www.cntv.cn",
        "www.gmw.cn",
        "www.google.com.au",
        "www.go.com",
        "www.nicovideo.jp",
        "www.flipkart.com",
        "www.cnn.com",
        "www.dailymotion.com",
        "www.bbc.co.uk",
        "www.booking.com",
        "www.github.com",
        "www.googleusercontent.com",
        "www.pixnet.net",
        "www.dropbox.com",
        "www.wikia.com",
        "www.163.com",
        "www.chinadaily.com.cn"
        ]

    # 15 iterations
    for i in range(15):
        for line in file:
            website = line.strip()
            output_file = website + str(i) + '.txt'
            os.system("/home/sahil/Desktop/Release/chrome "+website+" 2> " + output_file)
            

if __name__ == '__main__':
    analyze()
