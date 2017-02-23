from rtmbot.core import Plugin


class NoUserSearchPlugin(Plugin):
    def process_message(self, data):
        if data["text"].startswith(".finn"):
            self.outputs.append([data["channel"], "`.finn` støttes ikke lenger. Søk heller i medlemsoversikten!"])
