# -*- coding:utf-8 -*- 
import json

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

def gen_json(filename):
	f = open(filename)
	date_list = []

	for line in f.readlines():
		line = line.strip()
		# print line
		if not len(line) or line.startswith('startDate'):
			continue
		field = line.split('\t')
		pic_url = 'http://img3.douban.com/view/photo/photo/public/p' + field[4] + '.jpg'
		element = {'startDate': field[0], 'endDate': field[1], 'headline': field[2], 
								'text': field[3], 'asset': {'media': pic_url} }
		print element
		date_list.append(element)

	timeline = {'timeline': {'headline':'', 'type':'default', 'text':'', 'startDate':'', 'date': date_list}}
	timeline['timeline']['headline'] = 'Vietname'
	timeline['timeline']['startDate'] = '2013,04'
	timeline['timeline']['text'] = '一路向南！'
	return json.dumps(timeline,ensure_ascii=False)

f1 = open('output.json', 'w+')
output = gen_json('raw_data.txt')


# output2 = output.encode('utf-8')

f1.write(output)