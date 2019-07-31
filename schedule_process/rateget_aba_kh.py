import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def rateget():
    target_url = 'https://www.ababank.com/forex-exchange/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('table.contenttable tbody tr')):
        if index == 50:
            return content       
        title = data.text
        content += '{}\n'.format(title)
        # content +='{}'.format(title)
    # 字串處理
    content1 = content.split('\n')[-15].replace('USD / VND','')[0:9]
    content2 = content.split('\n')[-15][18:]
    content = 'USD~'+content1.replace(',','')[0:5] +' ~ '+ content2.replace(',','')[0:5]
    content = content.split('~')
    return content

if __name__ == '__main__':
    print(rateget())
