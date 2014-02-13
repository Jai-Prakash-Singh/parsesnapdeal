# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

import urll_proxy 
from bs4 import BeautifulSoup 
import phan_proxy
import re 
import req_proxy
import os 



def main():
    link = "http://www.snapdeal.com/"

    page = phan_proxy.main(link)
    #page = req_proxy.main(link)

    f = open("code1_sourcebody.txt", "a+")
    print >>f, page.encode("ascii", "ignore")
    f.close()
    

    soup = BeautifulSoup(page)

    tag_nav = soup.find_all("li",  attrs={"class":"navlink"})
    
    menu_list = {}

    for l in tag_nav:
        menu =  str(l.a.get_text()).strip()

        menu_list[menu] = {}

        tag_a = l.find_all("a", attrs={"class":"somn-track"})

        for l2 in tag_a:
            sub_menu = str(l2.get_text()).strip()
            sub_menulink = str(l2.get("href")).strip()
            menu_list[menu][sub_menu] = sub_menulink
            
    f = open("code1_menu_sub_menu_link.txt", "w+")
    print >>f,  menu_list
    f.close()

    menu_list.clear()
    print menu_list
    del menu_list
        #tag_a =  l.find_all("a")
        #urls = re.findall(r'href=[\'"]?([^\'" >]+)', str(tag_a).strip("()"))      
        #urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(tag_a).strip("()"))
        #print urls




if __name__=="__main__":
    main()
       
