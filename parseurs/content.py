import requests

BASE = "http://www.jugements.qc.ca/php/decision.php?liste=62532673&doc=05E36D8E32CEFE8BD9BEC482AA9BD1413EE35E4EAD6308CD646FFE4EA1892678&page=1"

EQUITE_SALARIALE = "http://ln-s.net/$eeF"

content = {}
def get_content(url):
	if url not in content:
		content[url] = requests.get(url).content
	return content[url]

EXAMPLE_PAR_TRIBUNAL = {
	"CAI": "http://www.jugements.qc.ca/php/decision.php?liste=62533357&doc=945C7D8974493AC125F803F02C2C4F8F597FF03D17BD49B0D8671181934B01F2&page=1",
	"CSST": "http://www.jugements.qc.ca/php/decision.php?liste=62532673&doc=05E36D8E32CEFE8BD9BEC482AA9BD1413EE35E4EAD6308CD646FFE4EA1892678&page=1",
	"CES": "http://ln-s.net/$eeF",
	'CDP': "http://www.jugements.qc.ca/php/decision.php?liste=62532357&doc=C39921412C5BE88629D664BE01D980E72673584C08F80C35F4C5B2E37CCE826A&page=1",
}

