#! /usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse

def banner():
    print(""" 
----------------------------------------------------------------------------------------                   
                          :::       ::: :::::::::: :::::::::                             
                          :+:       :+: :+:        :+:    :+:                            
                          +:+       +:+ +:+        +:+    +:+                            
                          +#+  +:+  +#+ +#++:++#   +#++:++#+                             
                          +#+ +#+#+ +#+ +#+        +#+    +#+                            
                           #+#+# #+#+#  #+#        #+#    #+#                            
                            ###   ###   ########## #########                             
 ::::::::   ::::::::  :::::::::      :::     :::::::::  :::::::::  :::::::::: :::::::::  
:+:    :+: :+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:    :+: :+:        :+:    :+: 
+:+        +:+        +:+    +:+  +:+   +:+  +:+    +:+ +:+    +:+ +:+        +:+    +:+ 
+#++:++#++ +#+        +#++:++#:  +#++:++#++: +#++:++#+  +#++:++#+  +#++:++#   +#++:++#:  
       +#+ +#+        +#+    +#+ +#+     +#+ +#+        +#+        +#+        +#+    +#+ 
#+#    #+# #+#    #+# #+#    #+# #+#     #+# #+#        #+#        #+#        #+#    #+# 
 ########   ########  ###    ### ###     ### ###        ###        ########## ###    ###           
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------          
                    """)

def get_html(urls):
    htmls = []
    for link in urls:
        if(link.endswith('.html') or link.endswith('.htm') or link.endswith('.xhtml') or link.endswith('.shtml') or link.endswith('.shtm') or link.endswith('.jsp') or link.endswith('.aspx')):
            htmls.append(link)
    return(htmls)

def get_css(urls):
    css = []
    for link in urls:
        if(link.endswith('.css') or link.endswith('.scss') or link.endswith('.sass') or link.endswith('.less') or link.endswith('.styl') or link.endswith('.pcss')):
            css.append(link)
    return(css)

def get_image(urls):
    images = []
    for link in urls:
        if(link.endswith('.jpg') or link.endswith('.jpeg') or link.endswith('.png') or link.endswith('.gif') or link.endswith('.tiff') or link.endswith('.tif') or link.endswith('.bmp') or link.endswith('.webp') or link.endswith('.svg') or link.endswith('.ico')):
            images.append(link)
    return(images)

def get_js(urls):
    js = []
    for link in urls:
        if(link.endswith('.js') or link.endswith('.jsx') or link.endswith('.json') or link.endswith('.ts')):
            js.append(link)
    return(js)

def get_pdf(urls):
    pdfs = []
    for link in urls:
        if(link.endswith('.pdf') or link.endswith('.pdp') or link.endswith('.pdfx') or link.endswith('.pdt')):
            pdfs.append(link)
    return(pdfs)

def get_php(urls):
    phps = []
    for link in urls:
        if(link.endswith('.php') or link.endswith('.phtml') or link.endswith('.php3') or link.endswith('.php4') or link.endswith('.php5') or link.endswith('.phps') or link.endswith('.phar')):
            phps.append(link)
    return(phps)

def get_xml(urls):
    xmls = []
    for link in urls:
        if(link.endswith('.xml') or link.endswith('.xsd') or link.endswith('.xsl')):
            xmls.append(link)
    return(xmls)

def write_output(url, urls, out, depth):
    if(out != None):
        if(not os.path.exists(out)):
            os.mkdir(out)
        with open(out+'/custom_output.txt', 'a') as file:
            recursion_level = options.t - (depth - 1)
            if(recursion_level != 1):
                file.write('='*120+'\n')
            file.write(f'At recursion level {recursion_level}\t--\tUrl: {url}\nTotal Links found: {len(urls)}\n')

            # Writing category wise
            htmls = get_html(urls)
            if(htmls):
                file.write(f'\nHtml: {len(htmls)}\n')
                for link in htmls:
                    file.write(link+'\n')
            
            css = get_css(urls)
            if(css):
                file.write(f'\nCss: {len(css)}\n')
                for link in css:
                    file.write(link+'\n')

            images = get_image(urls)
            if(images):
                file.write(f'\nImage: {len(images)}\n')
                for link in images:
                    file.write(link+'\n')

            js = get_js(urls)
            if(js):
                file.write(f'\nJs: {len(js)}\n')
                for link in js:
                    file.write(link+'\n')

            pdfs = get_pdf(urls)
            if(pdfs):
                file.write(f'\nPdf: {len(pdfs)}\n')
                for link in pdfs:
                    file.write(link+'\n')

            phps = get_php(urls)
            if(phps):
                file.write(f'\nPhp: {len(phps)}\n')
                for link in phps:
                    file.write(link+'\n')

            xmls = get_xml(urls)
            if(xmls):
                file.write(f'\nXml: {len(xmls)}\n')
                for link in xmls:
                    file.write(link+'\n')

            others = []
            for link in urls:
                if((link not in htmls) and (link not in css) and (link not in images) and (link not in js) and (link not in pdfs) and (link not in phps) and (link not in xmls)):
                    others.append(link)
            if(others):
                file.write(f'\nOther Links: {len(others)}\n')
                for link in others:
                    file.write(link+'\n')
    else:
        recursion_level = options.t - (depth -1)
        if(recursion_level != 1):
            print('='*120)
        print(f'At recursion level {recursion_level}\t--\tUrl: {url}\nTotal Links found: {len(urls)}')

        # Printing category wise
        htmls = get_html(urls)
        if(htmls):
            print(f'\nHtml: {len(htmls)}')
            for link in htmls:
                print(link)
        
        css = get_css(urls)
        if(css):
            print(f'\nCss: {len(css)}')
            for link in css:
                print(link)
        
        images = get_image(urls)
        if(images):
            print(f'\nImage: {len(images)}')
            for link in images:
                print(link)
        
        js = get_js(urls)
        if(js):
            print(f'\nJs: {len(js)}')
            for link in js:
                print(link)

        pdfs = get_pdf(urls)
        if(pdfs):
            print(f'\nPdf: {len(pdfs)}')
            for link in pdfs:
                print(link)

        phps = get_php(urls)
        if(phps):
            print(f'\nPhp: {len(phps)}')
            for link in phps:
                print(link)

        xmls = get_xml(urls)
        if(xmls):
            print(f'\nXml: {len(xmls)}')
            for link in xmls:
                print(link)

        others = []
        for link in urls:
            if((link not in htmls) and (link not in css) and (link not in images) and (link not in js) and (link not in pdfs) and (link not in phps) and (link not in xmls)):
                others.append(link)
        if(others):
            print(f'\nOther Links: {len(others)}')
            for link in others:
                print(link)

def find_link(url, depth, out):
    links=[]
    # Crawling Webpage
    s = requests.Session()
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    try:
        r = s.get(url, headers=header)
    except requests.exceptions.RequestException as e:
        raise SystemError(e)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    s.close()
    
    # Getting URL's from 'src' & 'href' attributes
    src_values = [x.get('src') for x in soup.find_all(src=True)]
    href_values = [x.get('href') for x in soup.find_all(href=True)]

    for i in (href_values+src_values):
        if(i.startswith('http://') or i.startswith('https://')):
            links.append(i)
        elif(i.startswith("//")):
            links.append('https:'+i)
        elif((not i.startswith('#')) and (not i.startswith('javascript:$'))):
            links.append(url+i)
    
    # Getting URL's by finding 'http://' & 'https://' strings
    https_strings = re.findall(r'https://[^\s"]+', str(soup))
    http_strings = re.findall(r'http://[^\s"]+', str(soup))
    
    for i in (http_strings+https_strings):
        if(i not in links):
            links.append(i)
    
    # Removing duplicate links
    uniq_links = []
    for i in links:
        if(i not in uniq_links):
            uniq_links.append(i)

    write_output(url, uniq_links, out, depth)

    while(depth > 1):
        depth -= 1
        for link in uniq_links:
            if((urlparse(url).netloc in link) and ((link != url) and (link != 'https://www.'+urlparse(url).netloc))):
                uniq_links = uniq_links + find_link(link, depth, out)

    return(uniq_links)

banner()

# Command line Arguments
args = argparse.ArgumentParser(description='Web Page Crawler that navigates and find links recursively !!')
args.add_argument('-u', '--url', required=True, help='Url of Target website \'https://example.com\'')
args.add_argument('-t', default=1, type=int, help='Depth for recursive crawling')
args.add_argument('-o', '--output', default=None, help='Output Folder')
options = args.parse_args()

if(options.t > 0):
    if(options.output != None):
        if(os.path.exists(options.output+'/custom_output.txt')):
            os.remove(options.output+'/custom_output.txt')
        if(os.path.exists(options.output+'/raw_output.txt')):
            os.remove(options.output+'/raw_output.txt')
    if(options.url.endswith('/')):
        options.url = options.url[:-1]
    # links = rec_fun(options.url, options.t, options.output)
    links = find_link(options.url, options.t, options.output)

    # Removing duplicate links
    final_links = []
    for i in links:
        if(i not in final_links):
            final_links.append(i)

    # Writing all Url's to raw_output.txt file
    if(options.output != None):
        with open(options.output+'/raw_output.txt', 'w') as file:
            for link in final_links:
                file.write(link+'\n')
        
        print(f"\nResult Stored in folder '{options.output}'")
        print('-'*50)
        size = os.path.getsize(options.output+'/custom_output.txt')
        print(f"File '{options.output}/custom_output.txt'\t\t-->\tSize: {size}")
        size = os.path.getsize(options.output+'/raw_output.txt')
        print(f"File '{options.output}/raw_output.txt'\t\t-->\tSize: {size}")

    # print(links)
else:
    raise argparse.ArgumentTypeError(f"{options.t} is an invalid positive int value")
