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
	'BDR/BDRVM': 'http://www.jugements.qc.ca/php/decision.php?liste=62533504&doc=A68512BA3A95A54A9C723D3709F8E129C5460438F6E13DA926781C2C9F3F9249&page=1',
	'CDP': 'http://www.jugements.qc.ca/php/decision.php?liste=62532357&doc=C39921412C5BE88629D664BE01D980E72673584C08F80C35F4C5B2E37CCE826A&page=1',
	'CDCSF': 'http://www.jugements.qc.ca/php/decision.php?liste=62533510&doc=23EABA2FB26DB3E36FEF30BB5EF851F51F08F3E2BBC609DA7AFC27784B32AD4B&page=1',
	'CPTAQ': 'http://www.jugements.qc.ca/php/decision.php?liste=62533576&doc=D2E10F8AFA92A7C3A4252D970B4CF60D6E7FB62CA43609E8B7CD1416A01B3C9D&page=1',
	'CSE': 'http://www.jugements.qc.ca/php/decision.php?liste=62533583&doc=13E61225837EA7E45216EAF0FCA275E81D7A4ED5391A1464E730B44D5E6617A8&page=1',
	'RBQ': 'http://www.jugements.qc.ca/php/decision.php?liste=62533532&doc=F95F7EA8E4ECA628C50F4AD4F726E2961E53EBBC256D5F635A90B990DEDB9385&page=1',
	'TAQ': 'http://www.jugements.qc.ca/php/decision.php?liste=62533515&doc=1F6AD491AECE81C1451C5B97C7FDE56C1B84A43E67C7FA694A307438B384285E&page=1',
}

