import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def rateget():
    target_url = 'http://classic-web.tbb.com.tw/6_1_2_1.html'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('table tr td')):   
        title = data.text
        content +='{}~'.format(title)
    # 字串處理
    content = content.split('~')
    # print(type(content))
    # print(content[0],content[1])
    content=content[2:4]
    return content

if __name__ == '__main__':
    print(rateget())