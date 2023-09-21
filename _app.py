from urllib.request import urlopen
import json

from googleplay.regex import Regex
import googleplay.getitem as getitem

class App:
    def __init__(self, _):
        self.name, self.created_at, self.downloads, self.purchases = getitem.name(_), getitem.created_at(_), getitem.downloads(_), getitem.purchases(_)
        self.rating, self.reviews, self.website, self.email = getitem.rating(_), getitem.reviews(_), getitem.website(_), getitem.email(_)
        self.address, self.description, self.id, self.screenshots = getitem.address(_), getitem.description(_), getitem.id(_), getitem.screenshots(_)
        self.category, self.icon, self.banner, self.version = getitem.category(_), getitem.icon(_), getitem.banner(_), getitem.version(_)

def app(id_: str, lang="ua", country="us"):
    html = urlopen(f"https://play.google.com/store/apps/details?id={id_}&hl={lang}&gl={country}").read().decode("UTF-8")
    data = {}
    scripts = Regex.SCRIPT.findall(html)

    for script in scripts:
        key = Regex.KEY.findall(script)
        value = Regex.VALUE.findall(script)

        if key and value:
            data[key[0]] = json.loads(value[0])

    data = [el for el in data["ds:5"][1][2] if el]

    app = App(data)

    return app