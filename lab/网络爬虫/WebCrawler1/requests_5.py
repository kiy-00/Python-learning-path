import requests
import json

if __name__ == "__main__":
    url='http://www.kfc.com.cn/kfccda/ashx/Get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    city = input('请输入要查找的城市')
    param={
        'cname':'',
        'pid':'',
        'keyword': city,
        'pageIndex': 1,
        'pageSize': 10,
    }

    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text

    fileName = city + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！')