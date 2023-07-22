import  requests
if __name__ == "__main__":
    #第一步：指定url
    url = 'https://sogou.com/'
    #第二步：发起请求,发起的是一个get请求
    #get方法会返回一个响应对象，使用response接收get方法的返回值
    response = requests.get(url=url)
    #第三步：获取响应数据(返回的字符串：搜狗页面的源码数据)，text返回的字符串形式的响应数据
    page_text = response.text
    print(page_text)
    #第四步：持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write((page_text))
    print('爬取数据结束！')