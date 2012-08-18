# encoding: utf8
import csv
import requests
from parser import QuebecParser

def show_common_fields(urls):
	header = ["Tribunal", "URL"]
	body = []
	fields = []
	for (name, url) in urls:
		print "URL ", url
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
	for n in row:
		print n
		yield n.encode('utf8')

if __name__ == "__main__":
	urls = [
		("CSST", "http://www.jugements.qc.ca/php/decision.php?liste=62532673&doc=05E36D8E32CEFE8BD9BEC482AA9BD1413EE35E4EAD6308CD646FFE4EA1892678&page=1"),
		("Equite Salariale", "http://ln-s.net/$eeF")
	]

	with open('champs.csv', 'w') as outfile:
		outwriter = csv.writer(outfile)
		for row in show_common_fields(urls):
			outwriter.writerow(list(encode_me_harder(row)))