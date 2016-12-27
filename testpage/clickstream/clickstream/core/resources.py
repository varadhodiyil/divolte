import json
import os


def getChartData():
	path=os.path.dirname((__file__))
	with open(path+'/data/data.json') as h:    
		data = json.load(h)
	return data