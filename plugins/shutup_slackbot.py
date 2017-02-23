from rtmbot.core import Plugin


class ShutupSlackbotPlugin(Plugin):
    def process_message(self, data):
        if data["text"] in ["Bpye Berg Nyberg"]:
            self.outputs.append([data["channel"], "Hold kjeft, slackbot..."])
