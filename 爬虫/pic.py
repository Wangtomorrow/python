#爬一张图片

#response.geturl()    response.info()   response.getcode()
import urllib.request
req = urllib.request.Request('http://ue1.17173cdn.com/a/dnf/index/2014v2/img/logo-dnf.png')
response = urllib.request.urlopen(req)
#response = urllib.request.urlopen("http://ue1.17173cdn.com/a/dnf/index/2014v2/img/logo-dnf.png")
back_pic = response.read()
print(response.geturl())   #返回真实的url
print(response.info())     #打印出远程服务器返回的header信息
print(response.getcode())   #打印出来http的状态.200表示ok
with open('back_pic.jpg','wb') as f:
    f.write(back_pic)