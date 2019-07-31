import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def rateget():
    target_url = 'https://vib.com.vn/wps/portal/en/tool-landing/tygia'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('table tbody tr')):
        if index == 50:
            return content       
        title = data.text
        # content += '{}\n'.format(title)
        content +='{}'.format(title)
    # 字串處理
    content = content.replace(',00','').replace('.','').split('\n')
    content = content[1:5]
    # content = content[1] +' \ '+ content[2][0:6].replace('.','') +' \ '+ content[3][0:6].replace('.','') +' \ '+ content[4][0:6].replace('.','')
    return content

if __name__ == '__main__':
    print(rateget())