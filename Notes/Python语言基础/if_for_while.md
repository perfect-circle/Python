# if语句    
## 1. 如何判断            
```pythoN    
IF 条件：    
    代码        # 判断条件为True,执行代码，否则不执行。    
```    
## 2. 检查多个条件    
```python    
if age_1 > 21 and age_2 > 21:    
    print("pass“)       # and两个条件要同时满足.or只满足一个就执行代码。    
```    
## 3. 检查特定值是否在列表中    
```python    
if 'value' in list_1:    
    print(value + "in list.")    
```    
## 4. if-elif-else结构    
只执行一个代码块用if-elif-else结构，执行多个代码块用一系列if语句。    
```python    
age = input("Please your age: ")    
if age <= 6:    
    print("free")    
elif age <= 18:    
    print("$1")    
elif age <= 65:    
    print("$2")    
else:    
    print("free")    
```        
# for循环（针对集合中每个元素）    
## 1. 循环列表       
```python    
mgicinas = ['alice','david','carolina']    
for mgicina in mgicinas:    # 把mgicinas列表的元素赋值给变量mgicina    
    print(mgicina)          # 打印变量mgicina    
```       
for循环要注意缩进，没有缩进则表示此行代码没有在循环内。        
## 2. 创建数字列表    
```python    
test_lists = []    
for value in range(1,5):       
    test_list =  value ** 2    
    test_lists.append(test_list)    
print(test_lists)    
           
[1,2,3,4]    
```    
## 3. 列表解析       
```python    
squares = [value**2 for value in range(1,5)]        # 没有冒号        
print(squares)      # 不需要缩进        
    
[1,4,9,16]    
```       
## 4. 循环字典    
```python    
user_0 = {'username':'efermi','first':'enrico','last':'fermi'}    
for key, value in user_0:    
    print("/nKey: " + key)    
    print("Value: " + value)    
```    
## 5. 遍历字典所有的键    
```python    
for key in user_0.keys():    
    print(key.title())    
```        
## 6. 按顺序遍历字典所有键    
#### 获取字典元素时，获取顺序是不可预测的    
```python    
for name in sorted(user_0.keys()):    
    print(name)    
```       
## 7. 获取字典的值并去重    
```python    
for value in set(user_0.values()):    
    print(value)    
```    
# while循环（循环一直运行直到条件不满足）    
## 1. 使用标志    
```python    
active = True    
while active:
    message = input("Please enter your input")        
    if message == 'quit':    
        active = False    
    else:    
        print(message)      # 打印你所输入的内容，输入quit结束循环    
```        
## 2.使用break退出循环    
```python    
while True:    
    message = input("Please enter your input")    
    if message == 'quit':    
        break    
    else:    
        print(message)      # 输入quit退出循环    
```        
## 3. 使用continue跳过循环    
```python    
corrent_number = 0         
while corrent_number < 10:        
    corrent_number += 1         
    if corrent_number % 2 == 0:        
        continue         
    print(corrent_number)   # 输出为1,3，5,7,9         
```    
## 4. 使用while循环来处理列表    
```python        
unconfirmed_users = ['tom','xiaoming','tom','marry']         
confirmed_users = []         
while unconfirmed_users:        
    user = unconfirmed_users.pop()        
    print("Verifying user: " + user)        
    confirmed_users.append(user)        
    
print("The following users have been confirmed:")        
for user in confirmed_users:        
    print(user)         # 把unconfirmed_users列表的元素转到了confirmed_user中    
```        
    
```python    
while 'tom' in unconfirmed_users:    
    unconfirmed_users.remove('tom')         # 删除列表unconfirmed_users中的元素'tom'    
```    
    
## 5. 使用while循环处理字典    
```python    
users = {}
active = True    
while active:    
    name = input("Please enter your name: ")    
    age = input("Please enter your age: ")    
    users[name] = age    
    a = input("Do you want to continue: yes/no")    
    if a.lower() == 'no':    
        active = False    
print(users)        # 创建一个由用户输入的字典            