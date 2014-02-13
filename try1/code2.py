#!/usr/bin/env python 
import req_proxy
import re 
from urlparse import urlparse
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )


def main():
    f = open("code1_menu_sub_menu_link.txt")
    menu_smenu_link = eval(f.read().strip())
    f.close()

    for menu, smenu_dict in menu_smenu_link.items():
        for smenu, link in smenu_dict.items():

            if str(smenu).strip().find("View All") != -1:
                pass

            else:
                link = str(link).strip()

	        if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link):
	            #req_proxy.main(link)
                    parsed = urlparse(link)
                   
                    cat = filter(None, parsed.path.split("/")) 
                    try:
                        f = open("code2_menu_smenu_cat_slink.csv", "a+")
                        cat = cat[-1].strip().replace(",", "-xx-")
                        menu = menu.replace(",", "-xx-")
                        smenu = smenu.replace(",", "-xx-")
                        
                        print>>f,  ','.join([menu, cat, smenu, link])
                        f.close()
                        logging.debug([menu, cat, smenu, link])
                    except:
                        pass
                     


if __name__=="__main__":
    main()
