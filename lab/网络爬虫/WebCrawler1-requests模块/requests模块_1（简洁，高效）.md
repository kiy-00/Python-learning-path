## requests模块（简洁，高效）

python中原生的一款基于网络请求的模块，功能非常强大，简单便捷，效率高

作用：模拟浏览器发请求。



### 使用（requests模块的编码流程）

* 指定url（在地址栏中输入一个具体的网址）
* 发起请求（按回车后，发起请求）
* 获取响应数据（返回一个网络页面）
* 持久化存储，存储的是响应数据

#### 

### 环境安装

pip install requests



### 编码

* 需求：爬取搜狗首页的页面数据

* ```python
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
  ```

* <img src="C:\Users\yi'k\AppData\Roaming\Typora\typora-user-images\image-20230721165631462.png" alt="image-20230721165631462" style="zoom: 50%;" />

![image-20230721165704577](C:\Users\yi'k\AppData\Roaming\Typora\typora-user-images\image-20230721165704577.png)

* 成功运行：<img src="C:\Users\yi'k\AppData\Roaming\Typora\typora-user-images\image-20230721170337562.png" alt="image-20230721170337562" style="zoom:50%;" />

* 打开爬取到的页面后发现样式丢失了，但我们需要的数据没有丢失：
  * <img src="C:\Users\yi'k\AppData\Roaming\Typora\typora-user-images\image-20230721170711064.png" alt="image-20230721170711064" style="zoom:50%;" />