#模拟浏览器使用有道词典翻译
import urllib.request
import urllib.parse
import json

content = input('请输入要翻译的内容：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}       #创建一个data字典
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1517230973125'
data['sign'] = 'f5afb6d7ef70a115d9f63dbe35984eda'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)

html = response.read().decode('utf-8')

# print(json.loads(html))
target = json.loads(html)
#print(target)
print('翻译结果为：%s'%(target['translateResult'][0][0]['tgt']))
