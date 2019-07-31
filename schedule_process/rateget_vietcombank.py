import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def rateget():
    target_url = 'https://www.vietcombank.com.vn/ExchangeRates/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('table.tbl-01')):
        if index == 50:
            return content       
        title = data.text
        content +='{}'.format(title)
    # 字串處理
    # print(content)
    content = str(str(content.replace(',','').split('\r\n')).
              replace('\n\n','').replace(' ','')).split('\\n\\n')[-2]
    content = content.split("','")
    # content = content[0] + content[1][0:-2]
    return content

if __name__ == '__main__':
    print(rateget())