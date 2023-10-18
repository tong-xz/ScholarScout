

import requests
from bs4 import BeautifulSoup

class SimpleWebCrawler:
    def __init__(self, start_url):
        self.start_url = start_url

    def fetch_content(self, url):
        """
        获取指定 URL 的内容
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
            return None

    def parse_content(self, content):
        """
        解析网页内容，提取所需信息
        """
        soup = BeautifulSoup(content, 'html.parser')
        # 根据需求进行解析，例如提取所有的链接
        schools = soup.find_all(id="success")
        return schools

    def crawl(self):
        """
        开始爬取
        """
        content = self.fetch_content(self.start_url)
        print(content)

if __name__ == "__main__":
    crawler = SimpleWebCrawler("https://csrankings.org/#/index?ai&vision&mlmining&nlp&inforet&us")
    index_html = crawler.crawl()
    crawler.parse_content(index_html)






