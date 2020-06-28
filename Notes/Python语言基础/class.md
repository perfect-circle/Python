# 类          
## 1. 创建类     
```python     
class Dog():     
    def __init__(self,name,age):    # 当你根据Dog类创建新实例时，Python都会自动运行他。形参self必不可少，Python调用__init__()方法创建实例时，将自动传入实参self。每个与类相关的方法都会自动传递实参self，他是一个指向实例本身的引用，让实例能够访问类中的属性和方法。     
        self.name = name    # 以self为前缀的变量都可供类中的所有方法使用，将实参name传递给self.name,然后该变量被关联到当前创建的实例     
        self.age = age     
     
    def sit(self):      # 在类中，函数贝被称为方法     
        print(self.name.title() + " is now sitting.")     
     
    def roll_over(self):     
        print(self.name.title() + " rolled over!"     
```     
     
## 2. 根据类创建实例     
```python     
my_dog = Dog('willie', 6)   # 创建实例     
your_dog = Dog('tom', 7)     
     
my_dog.sit()    # 调用方法     
your_dog.roll_over()     
     
print("My dog's name is " + my_dog.name.title() + ".")  # 访问属性     
print("Your dog's name is " + your_dog.name.title() + ".")     
```     
     
## 3. 给属性指定默认值     
```python     
class Car():     
    def __init__(self, make, model, year):     
        self.make = make     
        self.model = model     
        self.year = year     
        self.odometer_reading = 0   # 设定默认值为0     
     
    def get_descriptive_name(self):     
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model     
        return long_name     
     
    def read_odometer(self):     
        print("This car has " + str(self.odometer_reading) + " miles on it.")     
     
my_new_car = Car('audi', 'a4', 2016)     
print(my_new_car.get_descriptive_name)     
my_new_car.read_odometer()     
```     
     
* 修改默认值     
     
1. 直接修改属性的值：     
  ```python     
  my_new_car.odometer_reading = 23     
  my_new_car.read_odometer()     
  ```     
     
2. 通过方法修改属性的值：     
  ```python     
  class Car():     
    --snip--     
     
    def updata_odometer(self, mileage):     
        self.odometer_reading = mileage     
     
  my_new_car = Car('audi', 'a4', 2016)     
  my_new_car.read_odometer()    # 更新前     
     
  my_new_car.updata_odometer(23)     
  my_new_car.read_odometer()   # 更新后     
  ```     
     
* 禁止将数往回调     
```python     
class Car():     
    --snip--     
     
    def updata_odometer(self,mileage):     
        if mileage >= self.odometer_reading:     
            self.odometer_reading = mileage     
        else:     
            print("You can't roll back an odometer！")     
```     
## 4. 继承     
*编写类时，并非总是从空白开始的。如果你要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承了另一个类时，它将自动获得另为一个类的所有方法和属性;原有的类称为父类，而新的类称为子类。子类继承其父类的所有属性和方法还可以定义自己的属性和方法*         
     
* 如何继承     
```python     
class Car():     
    --snip--        # 创建子类时父类必须包含在当前文件中     
     
class ElectricCar(Car):     # 创建子类时，必须在括号内指定父类的名称     
    """电动汽车的独特之处"""     
    def __init__(self. make, model, year):     # 方法__init__(),接受创建Car实例的信息     
        super().__init__(make, model, year)    # 让子类实例包含父类的所有属性     
     
my_tesla = ElectricCar('tesla', 'model s', 2016)     
print(my_tesla.get_descriptive_name())     
```     
     
* 给子类定义属性和方法     
```python     
class Car():     
    --snip--     
     
class ElectricCar(Car):     
    def __init__(self, make, model, year):     
        super.__init__(make, model, year)     
        self.battery_size = 70      # 电动车的特有属性     
     
    def describe_battery(self):     
        print("This car has a " + str(self.battery_size) + "-KWh battery.")     
     
my_tesla = ElectricCar('tesla', 'model', 2016)     
my_tesla.describe_battery()     
```     
     
## 5. 重写父类的方法     
*对于父类的方法，只要它不符合子类的模拟的实物的行为，都可以对其进行重写。为此可以在子类中定义一个与父类相同的方法，这样python将只考虑父类的方法而不考虑子类的方法。*     
```python     
class ElectricCar(Car):     
    --snip--     
     
    def fill_gas_tank(self):    # 父类中有的方法，子类中有。朋友python则只运行子类的     
        print("This car doesn't need a gas tank!")     
```     
     
## 6. 将实例用作属性     
```python     
class Car():     
    --snip--     
     
class Battery():        # 编写一个电池描述类，可以将有关点池的方法都放在这个类中     
    def __init__(self, battery_size):     
        self.battery_size = battery_size     
     
    def describe_battery(self):     
        print("Your car has a " + str(self.battery_size) + "-KWh battery.")     
     
class ElectricCar(Car):     
    def __init__(self, make, model, year):     
        super.__init__(make, model, year)     
        self.battery = Battery()     
     
my_tesla = ElectricCar('tesla', 'model s', 2016)     
print(my_tesla.get_dexcriptive_name())     
my_tesla.battery.describe_battery()     
```     
     
## 7. 导入类     
*导入类，要将包含类的模块放在要导入类文件的同一文件夹内，否则用绝对路径，以.py为后缀命名。*     
* 导入单个类     
  ```python     
  from car import Car     
     
  my_new_car = Car('audi', 'a4' 2016)     
  print(my_new_car.get_descriptice_name())     
  ```     
     
* 模块内有多个类     
  ```python     
  from car import ElectricCar     
     
  my_tesla = ElectricCar('tesla', 'model s' ,2016)      
  my_tesla.battery.describe_battery()       # 因为类是Car类的子类，所以不用导入Car类，Battery类是ElectricCar类的属性，所以也不用导入Battery类     
  ```     
     
* 从模块类导入多个类     
  ```python     
  from car import Car, ElectricCar     
     
  my_beetle = Car('volkswagen', 'beetle', 2016)     
  print(my_beetle.get_descriptive_name)     
     
  my_tesla = ElectricCar('tesla', 'roadster', 2016)     
  print(my_tesla.get_descriptive_name())     
  ```     
* 导入整个模块     
  ```python     
  import car     
  my_beetle = car.Car('valkswagen', 'beetle', 2016)     
  print(my_beetle.get_descriptive_name())     
  ```     
     
* 在一个模块中导入另一个模块      
           
**electric_car.py**     
```python     
from car import Car     
class Battery():     
    --snip--     
     
class ElectricCar(Car):     
    --snip__     
```     
     
**car.py**     
```python     
class Car():     
    --snip--     
```     
     
**my_cars.py**     
```python     
from electric_car.py import ElectricCar     
     
my_tesla = ElectricCar('tesla', 'roadster', 2016)     