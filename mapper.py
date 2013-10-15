#!/usr/bin/env python

import sys

###########################################################################
# find the url with sitetype:6
##########################################################################


if __name__=="__main__":
    
    while True:
        
        line=sys.stdin.readline()

        if len(line)<=0:
            break
        line=line.strip()

        ## necessary fields 
        site_type = line.find("SiteType:6")
        if site_type == -1 :
            continue
       
        page_type_start = line.find("PageType:")
        if page_type_start == -1 :
            continue
        page_type_end = line[page_type_start:].find(" ")


        s_url_start = line.find("Surl:http://")
        if s_url_start == -1 :
            continue
        s_url_end = line[s_url_start:].find("Curl")

        s_url_value = line[s_url_start + 12 : s_url_start + s_url_end].strip()
        page_type_value = line[page_type_start + 9 : page_type_start + page_type_end].strip()

        if len(s_url_value) <= 0:
            continue
        if len(page_type_value) <= 0:
            continue

        res_str =  page_type_value + ":" + s_url_value

        print "%s"%(res_str)
