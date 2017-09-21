from bs4 import BeautifulSoup
import requests
import sys


def searchtpb(argv):
    searchurl = ""
    for idx, arg in enumerate(argv):
        if idx == 0:
            continue
        elif idx == 1:
            searchurl = arg
        else:
            searchurl = searchurl + "%20" + arg

    return "https://thepiratebay.org/search/"+searchurl


def findmagnet(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    for link in soup.find_all('a'):
        l = link.get('href')
        if 'magnet' in l:
            return l
    return ""


def main(argv):

    if len(argv) < 2:
        return

    url = searchtpb(argv)

    if not url:
        return

    magneturl = findmagnet(url)
    print magneturl


if __name__ == "__main__":
    main(sys.argv)
