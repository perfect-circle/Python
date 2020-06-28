# 文件     
## 1. 从文件中读取数据     
* 读取整个文件     
```python     
with open('file_name') as file_object:      # with打开文件后不需要就关闭文件。open()函数打开文件，as把文件名重新命名     
    contents = file_object.read()           # .read()函数,打开文件全部内容，再把全部内容赋值给contents     
    print(contents)     
```     
* 逐行读取     
```python     
filename = 'file_name.txt'     
with open(filename) as file_object:     
    for line in file_object:     
        print(line.rstrip())    # print打印会有空行     
```     
* 创建一个包含文件各行内容的列表     
```python     
filename = 'file_name.txt'     
with open(filename) as file_object:     
    lines = file_object.readlines()     # .readlines()函数将文件各行读取每一行，并将其存储在一个列表中。lines就是一个包含整个文件行的列表     
     
for line in lines:     
    print(line.rstrip())     
```     
## 2. 使用文件内容     
* 圆周率值中包含你的生日吗     
```python     
filename = 'pi_million_digits.txt'     
     
with open(filename) as file_object:     
    lines = file_object.readlines()     
     
pi_string = ''     
for line in lines:     
    pi_string += line.strip()     
     
birthday = input('Enter your birthday: ")     
if birthday in pi_string:     
    print('Your birthday appeas in the first million digits of pi!')     
else:     
    print("Your birthday does not appear in the first million digits of pi.")     
```     
## 3. 写入文件     
* 写入空白文件     
```python     
filename = 'programming.txt'     
     
with open(filename. 'w') as file_object:    # open(filename, 'w')第二个参数告诉python，以写的方式打开文件，如果文件不存在，open将创建文件。     
    file_object.wirte("I love programming.\n")    # 写入文件的内容。     
    file_object.wirte("I love creating new games.\n")     
```     
* 附加到文件     
```python     
filename = 'programming.txt'     
with open(filename, 'a') as file_object:        # 参数'a',表示插入     
    file_object.write("I also love finding meaning in large datasets.\n")     
    file_object.write("I love creating apps that can run in a browser.\n")     
```     
## 4. 存储数据     
     
## 使用 json.dump()和 json.load()     
     
*number_writer.py*     
```python     
import json     
     
numbers = [2, 3, 5, 66]     
     
filename = 'number.json'     
with open(filename, 'w') as f_obj:     
    json.dump(numbers, f_obj)    # 将数字列表写入文件中     
```     
     
*number_reader.py*     
```python     
import json     
     
filename = 'number.json'     
with open(filename) as f_obj:     
    number = json.load(f_obj)   # 加载文件内容，并把文件内容赋值到number中     
     
print(number)     
```     
     
# 异常     
* 使用try-except模块     
*如果try代码块中的代码导致了错误，Python将查找这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同，如果try没有错误则跳过except*     
``` python     
try:     
    print(5/0)     
except ZeroDivisionError:       # 如果try中的代码块运行的错误是ZeroDivisionError，则运行except的代码。     
    print("You can't divide by zero!")     
```     
* else代码块     
```python     
print("Give me two mubers, and I'll divide them.“)     
print("Enter 'q' to quit.")     
     
whiel True:     
    first_number = input("\nFirst number: ")     
    if first_number == 'q':     
        break     
    second_number = input("\nSecond number: ")     
     
    try:     
        answer = int(first_number / second_number)     
    except ZeroDivisionError:       # 出现错误后，执行except的代码块，继续循环     
        print("You can't ddivide by zero!")     
    else:       # 没有错误，继续循环     
        print(answer)     
```     
* 分析文本     
```python     
filename = 'alice.txt'     
try:     
    with open(filename) as f_obj:     
        contents = f_obj.read()     
except FileNotFoundError:       # 没有这个文件则执行，代码块中的代码     
    pritn("Sorry, the file " + filename + " does not exist.")     
else:     
    words = contents.split()    # 将文件内的单词转换为列表     
    words_number = len(words)     
    print("The file " + filename + " has about " + str(words_number) + "words.")     
```     
* 失败时一声不吭     
```python     
def count_words(filename):     
    try:     
        with open(filename) as file_object:     
            contens = file_object.read()     
    except FileNotFoundError:   # 失败时不会有traceback，也不会有输出。     
        pass     
    else:     
        words = contens.split()     
        num_words = len(words)     
        print(filename + " has " + str(num_words) + "words.")     
     
filenames = ['text.txt','alice.txt']     
for filename in filenames:     
    count_words(filename)     
```     
* 文本出现具体单词的单词数     
```python     
line = "Row, row, row your boat."     
line.count('row')     
> 2     
line.lower().count('row')     
> 3     
```     
* 存储读取文件     
```python     
import json      
filename = 'username.json'     
     
try:     
    with open(filename) as f_obj:     
        username = json.load(f_obj)     
except FileNotFoundError:       # 没有这个文件则创建文件     
    username = input("Please enter your name: ")     
    with open(filename, 'w') as f_obj     
        json.dump(username, f_obj)     
        print("We'll remember uou when you come back, " + username + '!')     
else:     
    print("Welcome back, " + username + "!")     
```     