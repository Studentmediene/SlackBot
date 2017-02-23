#! python3
from urllib.request import urlopen
import random
from json import loads

from rtmbot.core import Plugin

url = "http://api.icndb.com/jokes/random"


class ChuckFactsPlugin(Plugin):
    def process_message(self, data):
        data["text"] = data["text"].strip()
        if data["text"] == ".chuck":
            info = loads(urlopen(url).read().decode())
            self.outputs.append([data["channel"], info["value"]["joke"]])
        elif data["text"].startswith(".chuck "):
            arr = data["text"].split()
            if len(arr) > 1:
                url2 = url + "?limitTo="
                for a in arr[1:]:
                    url2 += "," + a
                info = urlopen(url2).read().decode()
                try:
                    info = loads(info)
                except:
                    self.outputs.append([data["channel"],
                                    str(arr[1:]) + " are not valid categories."])
                else:
                    self.outputs.append([data["channel"], info["value"]["joke"]])
