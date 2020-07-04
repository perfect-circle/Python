# 函数      

## 1. 定义函数      
``` python      
def greet_user(username):      
    print("Hello " + username.title() + "!")      
      
greet_user('jesse')         # username为形参，jesse为实参。greet_user将实参jesse传递给函数greet_user(),这个值被存储在username中。      
```      
      
## 2. 传递实参      
```python      
def describe_pet(animal_type,pet_name):      
    print("\nI have a " + animal_type + ".")      
    print("My " + amimal_type + "'s name is " + pet_name.title() + '.')      
      
describe_pet("hamster", "harry")        # 位置实参，实参位置与形参对应。      
describe_pet(animal_type='hamster',pet_name='harry')        # 关键字实参。      
```      
      
### 默认值      
```python      
def describe_pet(animal_type="hamster",pet_name)      
    print("\nI have a " + animal_type + ".")      
    print("My " + amimal_type + "'s name is " + pet_name.title() + '.')      
      
describe_pet("harry")       # 默认animal_type="hamster"      
describe_pet("dog","tom")   # 传递实参为animal_type="dog"      
```      
### 实参可选      
```python      
def get_formatted_name(first_name,last_name,middle_name=''):      
    if middle_name:      
        full_name = first_name + ' ' + middle_name + ' ' + last_name      
    else:      
        full_name = first_name + ' ' + last_name      
    return full_name.title()      
      
musician = get_formatted_name('jimi', 'hendrix')      
print(musician)      
      
musician = get_formatted_name('john', 'hooker', 'lee')      
print(musician)      
```      
      
## 3. 返回值      
``` python      
def get_formatted_name(first_name,last_name):      
    full_name = first_name + ' ' + last_name      
    return full_name.title()    # 将值返回到调用函数的代码行，没有return，调用此函数将返回None，因为没有返回值。      
      
musician = get_formatted_name('huo', 'hao')     # 将返回值储存在变量musician中      
print(musician)      
```      
      
## 4. 返回字典      
```python      
def build_person(first_name, last_name, age)      
    person = {'first':first_name, 'last':last_name}      
    if age:      
        person['age'] = age         # 有age则加入字典，没有则不加入字典。      
      
mesician = build_person('jimi', 'hendrix', age=27)      
print(mesician)      
```      
## 5. 在函数中修改列表      
```python      
def print_models(unprinted_designs, completed_models):      
    while unprinted_designs:      
        completed_model = unprinted_designs.pop()      
        print("Printing model: " + completed_model)      
      
        completed_models.append(completed_model)      
      
def show_completed_models(completed_models):      
    print("\nThe following models have been printed:")      
    for completed_model in completed_models:      
            print(completed_model)      
      
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']      
completed_models = []      
      
print_models(unprinter_designs,completed_models)      
show_completed_modes(completed_models)      
```      
      
### 禁止函数修改列表      
```python      
function_name(list_name[:])     # 创建一个列表副本      
def print_models(unprinted_designs[:], completed_models):       # 除非有充分理由需要传递副本，否则还是将原始列表传递给函数。因为创建副本需要时间和内存，大型列表尤其明显。      
```      
      
## 6. 传递任意数量的实参      
```python      
def make_pizza(*toppings):      
    print("\nMakeing a pizza with the following toppings:")      
    for topping in toppings:      
        print(topping)      
      
make_pizza('peperoni')      
make_pizza('peperoni', 'green peperes', 'extra cheese')     # 运行3个实参      
```      
      
## 7. 使用任意数量的关键字实参      
```python      
def make_car(manufacturer, model, **car_info):      
    car_attribute ={}      
    car_attribute['manufacturer'] = manufacturer      
    car_attribute['model'] = model      
      
    for key, value in car_info.items():      
            car_attribute[key] = value      
    return car_attribute      
      
car = make_car('subaru', 'outback', color='blue', tow_package=True)     # 可以添加任意数量的键值对      
print(car)      
```      
## 8. 将函数存储在模块中      
**他可以将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解的多。**      
*模块在本文件夹内，名称为model_name.py*      
      
* 导入整个模块      
  ```python      
  import model_name      
  model_name.function_name(parameter)      
  ```      
      
* 导入特定函数      
  ```python      
  from model_name import function_name_0, function_name_1      
  function_name_0(parameter)      
  ```      
      
* 给函数/模块指定别名      
  ```python      
  import model_name as mn      
  mn.function_name_0(parameter)          
      
  from model_name import function_name_0 as fn      
  fn(parameter)      
  ```      
      
* 导入模块中的所有函数      
  ```python      
  from model import *      
  function_name(parameter)      # 和导入整个模块比较，不用点句表示法      
  ```      

## 9. 递归函数
