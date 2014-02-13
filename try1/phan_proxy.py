from selenium import webdriver
from random import choice
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def main2(link):
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

    return driver


def main(link):
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

        logging.debug(driver.current_url)

        if str(driver.current_url).strip() == "about:blank":
            loop = True

        else:
            loop = False

    page = driver.page_source
    driver.delete_all_cookies()
    driver.close()
    return page

    
