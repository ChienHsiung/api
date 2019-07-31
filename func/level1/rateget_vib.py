import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

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
        content +='{}"~"'.format(title)
    content = content.split('\n')[1] +' \ '+ content.split('\n')[2] +' \ '+ content.split('\n')[3] +' \ '+ content.split('\n')[4]
    return content

print(rateget())