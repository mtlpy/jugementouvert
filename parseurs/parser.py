import bs4
import re

class Parser(object):
	def __init__(self, content):
		self.bs = bs4.BeautifulSoup(content)
		
	def allClassNames(self):
		for tag in self.bs.findAll():
			for atr_n, atr in tag.attrs:
				if atr_n == 'class':
					yield atr, tag

	def match_lbl_to_dat(self):
		tags = self.bs.findAll(class_=re.compile(self.class_prefix + '.*'))
		all_classes = {}
		for tag in tags:
			all_classes[tag.get('class')[0]] = tag

		codefied = {}
		for cls, tag in all_classes.items():
			suffix = cls[len(self.class_prefix) + 3:]
			codefied.setdefault(suffix, []).append((cls, tag))

		res = {}
		for suffix, tags in codefied.items():
			res[suffix] = {}
			for cls, tag in tags:
				middle = cls[len(self.class_prefix):][:3]				
				res[suffix][middle] = tag.text

		return res

class QuebecParser(Parser):
	class_prefix = "zSoquij"

class CSSTParser(QuebecParser):
	def titre(self):
		return self.bs.find("p", self.class_prefix + "Repertorie").text

	def demandeur(self):
		return self.bs.find("p", self.class_prefix + "NomPartieDem").text

	def defendeur(self):
		return self.bs.find("p", self.class_prefix + "NomPartieDef").text