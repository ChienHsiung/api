import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def rateget():
    target_url = 'https://www.sacombank.com.vn/en/company/Pages/exchange-rate.aspx'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('table tr td')):  
        title = data.text
        content +='{}~'.format(title)
    # 字串處理
    content = str(content.split('~'))
    content = content.replace(',','').replace(' ','').replace('[','').replace(']','').split("'")
    content = content[11:20][0]+','+content[11:20][2]+','+content[11:20][4]+','+content[11:20][6]+','+content[11:20][8]
    content = content.split(',')
    return content

if __name__ == '__main__':
    print(rateget())