from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
from googleplay._app import app

def search(q: str, getinfo: bool = False):
    html = urlopen(f"https://play.google.com/store/search?q={q.replace(' ', '%20')}&c=apps&hl=uk").read()
    data = BeautifulSoup(html, 'lxml')
    ids = data.find_all("div", class_="VfPpkd-aGsRMb")

    for id_ in ids:
        ids[ids.index(id_)] = str(id_).split('href="')[1].split('"')[0].split("=")[1]

    if not getinfo:
        return ids

    apps = []
    for id_ in ids:
        apps.append(app(id_))
    return apps