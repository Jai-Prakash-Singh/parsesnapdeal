#!/usr/bin/python 
from selenium import webdriver
from bs4 import BeautifulSoup
from random import choice
import time
import os

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def main(direc, line):
    line_list = line.strip().split(",")
    direc = direc.strip()
    menu = line_list[0].strip()
    smenu = line_list[1].strip()
    cat = line_list[2].strip()
    link =  line_list[3].strip()
    
    directory = direc + "/" +  menu + "/" + smenu + "/" + cat 
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = directory + "/" + cat + ".csv"

    f2 = open("/home/user/Desktop/proxy_http_auth.txt")
    proxy_list = f2.read().strip().split("\n")
    f2.close()

    loop = True
    while loop is  True:

        ip_port = choice(proxy_list).strip()

        user_pass = ip_port.split("@")[0].strip()
        prox = "--proxy=%s"%ip_port.split("@")[1].strip()
        service_args = [prox, '--proxy-auth='+user_pass, '--proxy-type=http', '--load-images=no']
        driver = webdriver.PhantomJS(service_args = service_args)

        driver.get(link)

        if str(driver.current_url).strip() == "about:blank":
            loop = True

        else:
            loop = False


    height = driver.execute_script("return $(document ).height();")
     
    loop = True
    while loop is True:      
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        heightnow  = driver.execute_script("return $(document ).height();")

        logging.debug((heightnow, height))

        if height == heightnow:
            loop = False
	else:
	    height = heightnow
            loop = True

        time.sleep(1)
        


    page = driver.page_source
    
    driver.delete_all_cookies()
    driver.close()

    soup = BeautifulSoup(page)
    tag_a = soup.find_all("a", attrs={"class":"hit-ss-logger"})

    for  l in tag_a:
        
        f = open(filename, "a+")
	print >>f, str(l.get("href")).strip()
        logging.debug(str(l.get("href")).strip())
        print page
	f.close()

    
