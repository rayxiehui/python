# coding:utf8

from img_spider import url_manager,html_outputer,html_downloader,html_parser

class SiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                html_cont = self.downloader.download(new_url)

                new_urls = self.parser.parse(new_url,html_cont)

                self.urls.add_new_urls(new_urls)

                # self.outputer.collect_data(new_data)

                count=count+1
                if count > 10:
                    break
            except :
                print "fail"
        self.outputer.output_html()
if __name__ == "__main__":
    root_url = "http://photo.sina.com.cn/"
    obj_spider = SiderMain()
    obj_spider.craw(root_url)