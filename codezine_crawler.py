import requests
from bs4 import BeautifulSoup
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
import time
import datetime

url = 'https://codezine.jp/news'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
article_a_tag = soup.select('p.c-articleindex_item_heading a')
auto_abstractor = AutoAbstractor()
auto_abstractor.tokenizable_doc = MeCabTokenizer()
auto_abstractor.delimiter_list = ["。", "\n"]
abstractable_doc = TopNRankAbstractor()
now = datetime.datetime.now()
filepath = 'summaries/codezine/' + now.strftime('%m%d') + '.txt'
f = open(filepath, 'w')
for a in article_a_tag:
    time.sleep(1)
    url = 'https://codezine.jp/' + a.get('href')
    f.write(url + "\n")
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    text = soup.select_one('div.detailBlock')
    result_dict = auto_abstractor.summarize(text.get_text(), abstractable_doc)
    for sentence in result_dict["summarize_result"]:
        f.write(sentence + "\n")
    f.write('---------------------------------------------------\n')