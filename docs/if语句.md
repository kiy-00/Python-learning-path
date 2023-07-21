## if语句



```python
if condition:
    # 如果条件为真，执行这段代码
else:
    # 如果条件为假，执行这段代码

```



```python
if condition:
    # 如果条件为真，执行这段代码
```



```python
if condition1:
    # 如果condition1为真，执行这段代码
elif condition2:
    # 如果condition1为假，但是condition2为真，执行这段代码
else:
    # 如果condition1和condition2都为假，执行这段代码
```



```python
x = 10

if x > 0:
    print("x是正数")
else:
    print("x是非正数")
```



```python
if condition1:
    # 如果condition1为真，执行这段代码
    if condition2:
        # 如果condition2也为真，执行这段代码
    else:
        # 如果condition2为假，执行这段代码
else:
    # 如果condition1为假，执行这段代码

```



```python
x = 10
y = 5

if x > 0 and y > 0:
    print("x和y都是正数")
elif x > 0 or y > 0:
    print("x或y是正数")
else:
    print("x和y都不是正数")

```

