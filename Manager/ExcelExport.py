#coding:utf-8
import xlwt
import django


class ExprotToFile(object):
	def __init__(self, query, filename):		
		self.query = query
		self.filename = filename
		if isinstance(self.query, list):
			self.parserList()
		else:
			self.parserQuerySet()


	def parserList(self):
		table = xlwt.Workbook(encoding="utf-8", style_compression=0)
		sheet = table.add_sheet("记录", cell_overwrite_ok=True)
		row = 0
		for element in self.query:
			low = 0
			for key in element:
				sheet.write(row, low, element[key].decode("utf-8"))
				low += 1			
			row += 1 
		table.save(self.filename)


	def parserQuerySet(self):
		pass

if __name__ == "__main__":

	ExprotToFile([{"ds":"1", "sd":"2"}, {"ds":"3", "sd":"4"}], "sds.xls")