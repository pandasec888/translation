#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse
import json
import time

banner = """

,-.----.                                ,---,              
\    /  \                   ,---,     ,---.'|              
|   :    |              ,-+-. /  |    |   | :              
|   | .\ :  ,--.--.    ,--.'|'   |    |   | |   ,--.--.    
.   : |: | /       \  |   |  ,"' |  ,--.__| |  /       \   
|   |  \ :.--.  .-. | |   | /  | | /   ,'   | .--.  .-. |  
|   : .  | \__\/: . . |   | |  | |.   '  /  |  \__\/: . .  
:     |`-' ," .--.; | |   | |  |/ '   ; |:  |  ," .--.; |  
:   : :   /  /  ,.  | |   | |--'  |   | '/  ' /  /  ,.  |  
|   | :  ;  :   .'   \|   |/      |   :    :|;  :   .'   \ 
`---'.|  |  ,     .-./'---'        \   \  /  |  ,     .-./ 
  `---`   `--`---'                  `----'    `--`---'  
  
"""
print(banner)

while True:
	content = input("请输入需要翻译的内容(输入'!!'退出程序):")
	if content == '!!':
	  break
              

	url = "http://fanyi.youdao.com/translate?	smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link"
	head = {}
	head['user-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
	data = {}
	data['type'] = 'AUTO'
	data['i'] = content
	data['doctype'] = 'json'
	data['xmlversion'] = '1.6'
	data['keyfrom'] = 'fanyi.web'
	data['ue'] = 'UTF-8'
	data['typoResult'] = 'true'
	data = urllib.parse.urlencode(data).encode('utf-8')

	req = urllib.request.Request(url,data,head)
	response = urllib.request.urlopen(req)
	html = response.read().decode('utf-8')

	target = json.loads(html)
	target = target['translateResult'][0][0]['tgt']
	print(target)
	time.sleep(1)