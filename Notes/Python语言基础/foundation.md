# Python基础

## 1. 字符串

* 把变量name中的字符串全转化为大写
  ```python
  print(name.upper())
  ```   

* 把变量name中的字符串全转换为小写
  ```python
  print(name.lower())
  ```

* 首字母大写

  ```python
  print(name.title())
  ```

* 合并字符串
  ```python
  "character_string_1" + " " + "character_string_2"
  ```

* 删除空白
  ```python
  print(name.rstrip())  # 删除末尾空白
  print(name.lstrip())  # 删除前面空白
  print(name.strip())   # 删除全部空白
  ``` 

* 数字与字符串的转换（不同数据类型不能运算）
  ```python
  age = 21
  str(age)  # 数字转为字符串
  int(age)  # 字符串转为数字
  ```

## 2. 列表

* 什么是列表：
  列表由一系列特定顺序排列的元素组成，列表通常包含多个元素，列表名称多为复数。
  ```python
  bicycles = ['trek','cannondale','redlin','specialized']
  ```

* 列表的对元素的操作
  ```python
  print(bicycles[0])              # 打印第一个元素
  bicycles[0] = 'honda'           # 修改第一个元素
  bicycles.append('ducati')       # 在列表末尾添加一个新元素
  bicycles.insert(0,'ducati')     # 在列表第一位插入新元素
  del bicycles[0]                 # 删除列表第一位元素
  bicycle = bicycle.pop()         # 弹出列表最后一个元素，赋值给变量
  bicycle.remove('trek')          # 删除指定元素

* 列表的排序
  ```python
  bicycles.sort()   # 永久性按字a-z母排序
  bicycles.sort(reverse=True)   # 永久性按反字母排序
  bicycles.sortde()  # 临时排序
  bicycles.reverse() # 永久按列表反排序

* 统计列表
  ```python
  len(bicycles)     # 返回列表元素个数
  min(bicycles)     # 返回数字列表的最小值
  max(bicycles)     # 返回数字列表的最大值
  sum(bicycles)     # 返回数字列表的总和
  ```
* 列表切片
  ```python
  bicycles[0:3]     # 列表的第一个到第三个
  bicycles[:4]      # 列表的开头到第四个
  bicycles[-3:]     # 列表的最后三个
  bicycles_copy = bicycles[:]   # 创建一个副本列表，两个列表的元素现在相同，可以各自更改自己的列表，而不会建立联系。
  ```

## 3. 元组
* 什么是元组
  元素不可更改的列表,其他操作和列表一样。
  ```python
  dimensions = (200,30,30)
  ```

* 修改元组变量
  ```python
  dimensions = (200,300)    # 可以重新定义变量
  ```

## 4. 字典
* 什么是字典
  字典是一系列键值对，每一个键都与一个值关联。
  ```python
  alien_1 = {'color':'green','points':'5'}
  ```

* 访问字典里的值
  ```python
  print(alien_1['color'])
  green
  ```

* 操作字典里的键值对
  ```python
  alien_1['x_position'] = 0     # 添加一对新的键值对
  alien_1['color'] = 'yellow'   # 修改字典里的值
  del alien_1['points']         # 删除键，就可以删除键值对了

* 嵌套
1. 列表嵌套字典
   ```python
   alien_0 = {'color':'green','points':5}
   alien_1 = {'color':'yellow','points':10}
   alien_2 = {'color':'red','points':15}
   aliens = [alien_0,alien_1,alien_2]

2. 字典嵌套列表
    ```python
    pizza = {
        'crust':'thick',
        'toppings':['mushrooms','extra']
    }
   ```

3. 字典嵌套字典
   ```python
   user = {
       'aeinstenin':{
           'first':'albert',
           'last':'einstein',
           'location':'princeton',
       },
       
        'mcurie':{
            'first':'marie',
            'last':'curie',
            'location':'paris',
        },
   }
  