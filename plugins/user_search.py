from urllib.request import urlopen, quote
from json import loads

from rtmbot.core import Plugin

URL = 'https://bruker.smint.no/search/index.php'


class UserSearchPlugin(Plugin):
    def process_message(self, data):
        if data['text'].startswith('.finn '):
            term = data['text'][6:]
            if len(term) < 1:
                return
            result = loads(urlopen(URL + '?s=' + quote(term)).read().decode())[:7]
            for person in result:
                name = person['cn'] if person['cn'] is not None else 'ukjent navn'
                username = person['uid']
                phone = person['tlf'] if person['tlf'] is not None else 'ukjent tlf.'
                mail = person['mail'] if person['mail'] is not None else 'ukjent mail'
                self.outputs.append([data['channel'], name + ' (' + username + '): ' + phone + ' // ' + mail])
