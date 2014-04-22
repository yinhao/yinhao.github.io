# -*- coding:utf-8 -*- 
import json
import math

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

def gen_json(start, end):
	date_list = []

	for i in range(start,end+1):
		s = '0'*(4-int(math.log(i,10)))+str(i)
		url = 'http://pics.dmm.co.jp/digital/video/beb{}/beb{}pl.jpg'.format(s, s)
		element = {'startDate': str(1900 + i)+',1,1' , 'endDate': str(1900 + i)+',12,31', 'headline': 'BEB'+'0'*(2-int(math.log(i,10)))+str(i), 
								'text': 'for Fun', 'asset': {'media': url} }
		print element
		date_list.append(element)

	timeline = {'timeline': {'headline':'', 'type':'default', 'text':'', 'startDate':'', 'date': date_list}}
	timeline['timeline']['headline'] = 'Test'
	timeline['timeline']['startDate'] = '0'
	timeline['timeline']['text'] = 'Haha！'
	return json.dumps(timeline,ensure_ascii=False)

f1 = open('beb_cover.json', 'w+')
f1.write(gen_json(1,150))

# output2 = output.encode('utf-8')
# f1.write(output)


