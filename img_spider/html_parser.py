# coding:utf8

from bs4 import BeautifulSoup
from img_spider import downimg
import re

class HtmlParser(object):
    def __init__(self):
        self.down = downimg.Downimg()
        self.number = 0

    def _get_new_urls(self, soup):

        new_urls = set()

        links = soup.find_all('a',class_='pic_img')

        for link in links:
            new_url = link['href']
            if new_url not in ['javascript:void(0)','javascript:;','#']:
                new_urls.add(new_url)
        print new_urls
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = {}
        res_data['url'] = page_url
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        return res_data

    def _save_img(self,soup,page_url):

        new_urls = []
        links = soup.find_all('img',src = re.compile(r"jpg$"))
        link_more = soup.find_all('dd',text = re.compile(r"jpg$"))

        for link in links:
            new_url = link['src']
            new_urls.append(new_url)

        for link in link_more:
            new_url = link['text']
            new_urls.append(new_url)

        self.down.down(self.number , new_urls)
        self.number = self.number + 1

    def parse(self,page_url,html_cont):

        if page_url is None or html_cont is None:

            return
        soup = BeautifulSoup(html_cont, 'lxml')
        new_urls = self._get_new_urls( soup)

        self._save_img(soup,page_url)
        # new_data = self._get_new_data(page_url, soup)
        return new_urls
