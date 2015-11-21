import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

matplotlib.rc('font', family='cwTex Q Yuan')

url = ('https://zh.wikipedia.org/wiki/2016'
       '%E5%B9%B4%E4%B8%AD%E8%8F%AF%E6%B0%91'
       '%E5%9C%8B%E7%B8%BD%E7%B5%B1%E9%81%B8'
       '%E8%88%89')

with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf8')

soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')
raw_data = list(filter(lambda x: x.text.strip().startswith(
        '2016年中華民國總統選舉候選人支持度'
    ), tables))[0]

data = []

for tr in raw_data.find_all('tr'):
    tds = list(tr.find_all('td'))

    if not tds: 
        continue

    ls = list(map(lambda x: x.text, tds))
    date = datetime.strptime(ls[1], '%Y年%m月%d日').date()
    vals = list(map(lambda x: x[:-1], ls[2:]))
    data.append((date, vals))

data.sort(key=lambda x: x[0])
x, _ys = zip(*data)
ys = zip(*_ys)

lb = ['蔡', '朱', '宋', '未']
for i, y in enumerate(ys):
    y = savgol_filter(np.array(y), 9, 2)
    plt.plot(x, y, label=lb[i])

plt.legend()
plt.show()

