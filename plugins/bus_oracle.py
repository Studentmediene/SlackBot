from urllib.request import urlopen, quote

outputs = []
channels = ["C08R9TE2F"] # radioteknisk

api = "http://m.atb.no/xmlhttprequest.php?service=routeplannerOracle.getOracleAnswer&question="

def process_message(data):
	if data["channel"] in channels:
		if data["text"].startswith(".bus "):
			info = data["text"][5:]
			if len(info) < 1:
				return
			outputs.append([data["channel"], urlopen(api + quote(info)).read().decode()])