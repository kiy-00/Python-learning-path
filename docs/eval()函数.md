## eval()函数



### 语法

* eval(s)函数将去掉字符串s最外侧的引号，并按照Python语句方式执行去掉引号后的字符串
* 语法格式
  * 变量=eval(字符串)
* 经常和input()函数一起使用，用来获取用户输入的数值型



```python
s='3.14+3'
print(s,type(s))
x=eval(s)

#x=6.14

age=eval(input('请输入您的年龄：'))	
#将字符串类型转成了int类型，相当于int(age)操作
print(age,type(age))
#输出 18 <class 'int'>

height=eval(input('请输入您的身高：'))
#将字符串类型转换成了float型，相当于float(height)操作
print(height,type(height))
#输出 162.0 <class 'float'>
```



### 会报错的使用方法

```python
print(eval('hello'))
#会报错，因为去掉引号后相当于print(hello)，hello变成了一个变量，但是它在前面并没有被声明过
```

