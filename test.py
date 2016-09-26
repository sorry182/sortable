import json
from collections import OrderedDict

with open('products.txt') as products:
	with open('listings.txt') as listings:
		result = open('result.txt','w')
		for product in products:
			p=json.loads(product)
			listings.seek(0)
			list = []
			for listing in listings:
				l = json.loads(listing)
				if(p['model'] in l['title'] and p['manufacturer'] in l['manufacturer']):
					list.append(l)
			if(list):
				a = OrderedDict()
				a["product_name"]=p["product_name"]
				a["listings"]=list
				result.write(json.dumps(a))
				result.write("\n")
		result.close()