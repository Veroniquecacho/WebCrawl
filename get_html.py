from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import os
import re

#base_url = 'https://clbokea.github.io/exam/'
#first_url = 'https://clbokea.github.io/exam/index.html'

def open_urls(url):
    try:
        page = urlopen(url).read().decode('utf-8')
        
    except HTTPError as err:
        if err.code == 404:
            print('404 Error')
        else:
            print('cant get page(internet connction): ' + url)
        print(err)
    except URLError as err:
        print('Download error: ' + err )
    except Exception as err:
        print(err)

    
    return page

def check_for_duplicate(pages):
      return list(dict.fromkeys(pages))

def find_links(page, tag, url):
    urls = []
    site = page.split(' ')

    for lines in site:
        if 'href' in lines:
            lines = lines.split('"')
            for words in lines:
                if (tag in words):
                    urls.append(url+words)
                    urls = check_for_duplicate(urls)
    return urls

