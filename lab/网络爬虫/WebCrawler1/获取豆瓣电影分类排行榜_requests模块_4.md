## 获取豆瓣电影分类排行榜



<img src="C:\Users\yi'k\AppData\Roaming\Typora\typora-user-images\image-20230722113259706.png" alt="image-20230722113259706" style="zoom:50%;" />

获取参数

<img src="C:\Users\yi'k\AppData\Roaming\Typora\typora-user-images\image-20230722113825575.png" alt="image-20230722113825575" style="zoom:50%;" />

```python
import requests
import json

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"
    param={
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',#从库中的第几部电影去取
        'limit': '20',#一起请求取出的个数
    }
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response=requests.get(url=url,params=param,headers=headers)
    list_data = response.json()

    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('over!!!')
```

