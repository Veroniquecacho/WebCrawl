import re
import os
from get_html import*
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError
from simple_colors import*

base_url = 'https://clbokea.github.io/exam/'


def get_photos(pic_url, pic_name):
    
    try:
        file = open(pic_name, 'wb')
        file.write(urlretrieve(pic_url, pic_name))
    except TypeError as err:
        pass
    except IOError:
        print(red('unable to create:'+ pic_name))
  

def handel_html(file):
    html = open_urls(file)
    change_tags(html, file)
    
def change_tags(html, file_name):
    file = open (file_name[31:-5]+'.md', 'w+')
    make_md = ' '.join(html.split())
    relevant_tags =  '<h1>.*?</h1>|<h2>.*?</h2>|<p>.*?</p>|<ul>.*?</ul>|<li>.*?</li>|<a>.*?</a>|<pre>.*?</pre>|<img\s+src=\".*?>|<p\s+class=\"lead\">.*?</p>'
    #one_tag = '<article\s+class=\"container\">.*?</article>'
    tags = re.findall(relevant_tags, make_md)
    #print(tags)
    for lines in tags:
        
        if '<h1>' in lines:
            lines = lines.replace('<h1>', '\n#')
            lines = lines.replace('</h1>', '\n')
            file.write(lines) 
        elif '<h2>' in lines:
            lines = lines.replace('<h2>', '\n##')
            lines = lines.replace('</h2>', '\n')
            file.write(lines) 
        elif 'img' in lines:
            if 'logo_python.png' not in lines:
                line = lines.split()
                for word in line:
                    if 'src' in word:
                        os.chdir('src')
                        word = word.replace('src="','![Web Scraping](' )
                        word = word.replace('"', '')
                        get_photos(base_url+'src'+word[19:], word[20:])
                        print(green('         Pic - '+word[20:]))
                        lines = word+ ')\n'
                        os.chdir('..')
                        file.write(lines) 
            else:
                lines = lines.replace(lines, '')
                file.write(lines) 
        elif 'p>' in lines:
            lines = lines.replace('<p>', '')
            lines = lines.replace('</p>', '')
            lines = lines.replace('<p class="lead">', '> ')
            if '<a' in lines:
                line = lines.split('<a ')
                a_tag = line[1]
                link = a_tag.split('>')
                link_end = link[0]
                link_start = link[1]
                link_end = link_end.replace('href="', '(')
                link_end = link_end.replace('"', ')\n')
                link_start = link_start.replace('</a', ']')
                lines = line[0]+'['+link_start+link_end
            file.write(lines)
        elif '<li>' in lines:
            lines = lines.replace('<ul> <li>', '*')
            lines = lines.replace('<li>', '*')
            lines = lines.replace('</li>', '\n')
            lines = lines.replace('</ul>', '')
            file.write(lines) 
        elif 'pre' in lines:
            lines = lines.replace('<pre>','\n```\n')
            lines = lines.replace('<code>','')
            lines = lines.replace('</pre>','\n```\n')
            lines = lines.replace('</code>','')
            lines = lines.replace('&lt;', '<')
            lines = lines.replace('&gt;', '>\n')
            lines = lines.replace('*', '\n*')
            lines = lines.replace('#', '\n#')
            file.write(lines)    
    
    print(green('         File - ' +file.name))
    file.close()
        
     
        
           
             
    
    
