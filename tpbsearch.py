from bs4 import BeautifulSoup
import requests
import sys


def main(argv):
    searchurl = ""
    for idx, arg in enumerate(argv):
        if idx == 0:
            continue
        elif idx == 1:
            searchurl = arg
        else:
            searchurl = searchurl + "%20" + arg
    r  = requests.get("https://thepiratebay.org/search/"+searchurl)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    for link in soup.find_all('a'):
        l = link.get('href')
        if 'magnet' in l:
            print(l)
            return

if __name__ == "__main__":
    main(sys.argv)
