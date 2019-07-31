import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def rateget():
    target_url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('.rate-content-cash.text-right.print_hide')):
        if index == 50:
            return content       
        title = data.text
        # content += '{}\n'.format(title)
        content +='{}~'.format(title)
    # 字串處理
    # content = content.replace(',00','').replace('.','').split('\n')
    # content = content.split('~')[0],content.split('~')[1]
    content = content.split('~')[0:2]
    return content

if __name__ == '__main__':
    print('美金,',rateget())