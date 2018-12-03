from urllib.request import Request, urlopen
import argparse
from bs4 import BeautifulSoup

def getCode(url):

    q = Request(url)
    q.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')

    raw = urlopen(q).read()
    code = raw.decode()
    soup = BeautifulSoup(raw, 'html.parser')
    print(soup.prettify)
    ''' lists = soup.find_all("div",class_="wpsl-store-location")
    for store in lists:
        print(store)

    #print(code)'''



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Hostname")
    parser.add_argument("--url",action="store",dest="url",required=True)
    args = parser.parse_args()
    url = args.url
    getCode(url)