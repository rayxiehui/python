# coding:utf8
import requests
import os
class Downimg(object):
    def __init__(self):
        pass
    def down (self, imgname, urls):
        for i, url in enumerate(urls):
            try:
                if i > 3:
                    break
                if not os.path.exists('./img/{0}'.format(imgname)):
                    os.mkdir('./img/{0}'.format(imgname))
                res = requests.get(url).content
                with open('./img/{0}/{1}.jpg'.format(imgname, i), 'wb') as file:
                    file.write(res)
            except:
                print 'err'