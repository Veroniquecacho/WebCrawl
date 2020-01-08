from change_html import*
from get_html import*
import sys


def start(first_url):
    index =  open_urls(first_url)
    handel_html(first_url)
    htmls = find_links(index, '.html', base_url)
    html_one = htmls[1]
    html_two = htmls[2]
    html_three = htmls[3]
    html_four = htmls[4]
    handel_html(html_one)
    handel_html(html_two)
    handel_html(html_three)
    handel_html(html_four)

def main():
    print(yellow('        --------------------------------'))
    print(yellow('        * Web Scraping program strated *','bold'))
    print(yellow('        --------------------------------\n'))
    print(green('         Saved: ', 'bold'))
    try:
        first_url = sys.argv[1]
        start(first_url)
        
    except URLError as err:
        print('Download error: ' + err )
    except Exception as err:
        print('exception: ', err)
    finally:
        print('\n')
        print(blue('         ------------------------------'))
        print(blue('         * Web Scraping program ended *','bold'))
        print(blue('         ------------------------------\n'))
    

if __name__ == '__main__':
    main()
    