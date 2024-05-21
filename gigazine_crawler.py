import requests
from bs4 import BeautifulSoup
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
import time
import random

url = 'https://gigazine.net/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
article_a_tag = soup.select('div.thumb a')
auto_abstractor = AutoAbstractor()
auto_abstractor.tokenizable_doc = MeCabTokenizer()
auto_abstractor.delimiter_list = ["。", "\n"]
abstractable_doc = TopNRankAbstractor()
for a in article_a_tag:
    time.sleep(random.randint(1, 3))
    res = requests.get(a.get('href'))
    soup = BeautifulSoup(res.content, 'html.parser')
    text = soup.select_one('div.cntimage')
    result_dict = auto_abstractor.summarize(text.get_text(), abstractable_doc)
    for sentence in result_dict["summarize_result"]:
        print(sentence)
    print('---------------------------------------------------')
