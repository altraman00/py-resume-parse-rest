import urllib
from _curses import error

from bs4 import BeautifulSoup
from flask import Flask

import html_parse

app = Flask(__name__)


@app.route('/')
def hello_world():
    url = "https://baike.baidu.com/item/Python/407313"
    htmlParse = html_parse.HtmlParse()

    # 解析html成document
    soup = htmlParse.parse_baike(url)

    # 获取html中的数据
    res_data = htmlParse.get_html_data(url, soup)
    res_data_url = res_data['url']
    res_data_title = res_data['title']
    res_data_summary = res_data['summary']
    print('url:%s\ntitle:%s\nsummary:%s' % (res_data_url, res_data_title, res_data_summary))

    return res_data_summary


if __name__ == '__main__':
    app.run()
