import requests

BASE = "http://www.jugements.qc.ca/php/decision.php?liste=62532673&doc=05E36D8E32CEFE8BD9BEC482AA9BD1413EE35E4EAD6308CD646FFE4EA1892678&page=1"

EQUITE_SALARIALE = "http://ln-s.net/$eeF"

content = {}
def get_content(url):
	if url not in content:
		content[url] = requests.get(url).content
	return content[url]

example_page = get_content(BASE)