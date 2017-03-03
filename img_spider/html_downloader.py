# coding:utf8
import requests

class HtmlDownloader(object):
    def __init__(self):
        pass
    def download(self,url):
        if url is None:
            return None
        # headers = {
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        #     "Accept-Encoding": "gzip, deflate, sdch",
        #     "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        #     "Cache-Control": "max-age=0",
        #     "Connection": "keep-alive",
        #     "Cookie": "tvfe_boss_uuid=6ab825d1f5be76ee; ptcz=2e0762c0199210f370fbe861c078fdfe63de194b7eda01a59fc1cea1334d029e; pt2gguin=o0919644575; pac_uid=1_919644575; ad_play_index=26; ptag=www_qq_com|; pgv_info=ssid=s4872494908; ts_refer=www.qq.com/; pgv_pvid=7535855420; o_cookie=919644575; ts_uid=7071702184",
        #     "Host": "news.qq.com",
        #     "Referer": "http://www.qq.com/",
        #     "Upgrade-Insecure-Requests": "1",
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        # }
        #

        response = requests.get(url)
        response.encoding = 'gb2312'

        return response.text