import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def rateget():
    target_url = 'https://www.cathaybk.com.tw/cathaybk/personal/exchange/product/currency-billboard/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('table.table-rate.text-left tr')):   
        title = data.text
        content +='{}~'.format(title)
    # 字串處理
    content = content.split('\n')
    # print(type(content))
    # print(content[0],content[1])
    content=content[12:14]
    return content

if __name__ == '__main__':
    print(rateget())