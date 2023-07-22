#反爬机制介绍

#UA：User-Agent()：请求载体的身份标识

#UA检测：门户网站的服务器会检测或监测对应请求的载体身份标识，
# 如果检测到的载体身份标识为某一款浏览器，
#说明该请求是一个正常的请求（一个用户通过浏览器发起的一个请求）
#但是，如果检测到请求的载体身份标识不是基于某一款浏览器的，
# 则表示该请求为不正常的请求（爬虫），则服务器端就很有可能拒绝该次请求

#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器


import  requests
if __name__ == "__main__":
    #UA伪装：将对应的USer-Agent封装到一个字典中
    #伪装成了谷歌浏览器
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    url='https://sogou.com/web'
    #处理url携带的参数：封装到字典中
    keyword=input('请输入搜索关键词：')
    param={
        'query':keyword
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    #在域名的后面动态拼接了参数
    response = requests.get(url=url,params=param,headers=headers)
    page_text=response.text

    fileName=keyword+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！')