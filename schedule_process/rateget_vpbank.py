import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def rateget():
    target_url = 'https://www.vpbank.com.vn/vpb-exchange-rates?target=en'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('table tbody tr td')):
        if index == 50:
            return content       
        title = data.text
        # content += '{}\n'.format(title)
        content +='{}~'.format(title)
    # 字串處理
    content = ((content.split('~')[24]).replace(',','')).replace(' ','')
    content = content[1:6]+','+content[6:11]+','+content[11::]
    content = content.split(',')
    return content

if __name__ == '__main__':
    print(rateget())