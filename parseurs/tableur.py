# encoding: utf8
import csv
import argparse

import requests

from parser import QuebecParser

def show_common_fields(urls):
	header = ["Tribunal", "URL"]
	body = []
	fields = []
	for (name, url) in urls:
		print "URL", url
		qp = QuebecParser(requests.get(url).content)
		line = [name, url]

		matched = qp.match_lbl_to_dat()
		for field_name in matched.keys():
			if field_name not in fields:
				fields.append(field_name)

		field_values = [""] * len(fields)
		for field_name, data in matched.items():
			field_values[fields.index(field_name)] = data.get('dat', '')

		line += field_values
		body.append(line)

	yield header + fields
	for n in body:
		yield n

def encode_me_harder(row):
	return [n.encode('utf8') for n in row]

def parser():
	ap = argparse.ArgumentParser(description="Génère un tableur de tout les champs relevé des pages de différent tribunaux.")
	ap.add_argument('outfile', help='Ou mettre le tableur csv', type=argparse.FileType('w'))
	return ap

if __name__ == "__main__":
	urls = [
		("CAI", "http://www.jugements.qc.ca/php/decision.php?liste=62533357&doc=945C7D8974493AC125F803F02C2C4F8F597FF03D17BD49B0D8671181934B01F2&page=1"),
		("CSST", "http://www.jugements.qc.ca/php/decision.php?liste=62532673&doc=05E36D8E32CEFE8BD9BEC482AA9BD1413EE35E4EAD6308CD646FFE4EA1892678&page=1"),
		("CES", "http://ln-s.net/$eeF"),
		('CDP', "http://www.jugements.qc.ca/php/decision.php?liste=62532357&doc=C39921412C5BE88629D664BE01D980E72673584C08F80C35F4C5B2E37CCE826A&page=1"),
	]

	args = parser().parse_args()
	outwriter = csv.writer(args.outfile)
	for row in show_common_fields(urls):
		outwriter.writerow(encode_me_harder(row))