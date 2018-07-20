# 隐藏
# 修改header特征  1.通过Request的headers参数修改   2.通过Request.add_header()方法修改
# 延迟提交时间  time.sleep()
# 使用代理
# 1.参数是一个字典{'类型'： '代理IP：端口号'}
# proxy_support = urllib.request.ProxyHandler({})
# 2.定制、创建一个opener
# opener = urllib.request.build_opener(proxy_support)
# 3a.安装opener
# urllib.request.install_opener(opener)
# 3b.调用opener
# opener.open(url)
import urllib.request
import urllib.parse
import json
import time
while True:
    content = input('请输入要翻译的内容（输入"q！"退出程序）：')
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    # head = {}
    # head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

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
    #response = urllib.request.urlopen(url, data)
    #req = urllib.request.Request(url, data, head)
    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    # print(json.loads(html))
    target = json.loads(html)
    #print(target)
    print('翻译结果为：%s'%(target['translateResult'][0][0]['tgt']))
    print(req.headers)
    time.sleep(5)