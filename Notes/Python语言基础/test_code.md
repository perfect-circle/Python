# 测试代码       
## 1. unittest Module中的断言方法       
| 方法 | 用途 |            
|:----:|:----:|       
| assertEqual(a,b) | 核实a == b |       
| assertNoEqual(a,b) | 核实a != b |       
| assertTrue(x) | 核实x为True |       
| assertFalse(x) | 核实x为False |       
| assertIn(item, list) | 核实item在list中 |       
| assertNotIn(item, list) | 核实item不在list中 |       
       
## 2. 测试函数       
name_function.py       
```python       
def get_formatted_name(first, last):       
    fun_name = first + ' ' + last       
    return fun_name.title()       
```       
       
test_name_function.py       
```python       
import unittest     # 导入测试模块       
from name_function import get_formatted_name       
       
class NameTestCase(unittest.TestCase):      # 创建测试类以unittest.TestCase为父类，并以驼峰法命名       
    def test_first_last_name(self):     # 这个方法必须以test开头，这样python才会自动运行这个方法       
        formatted_name = get_formatted_name('janis', 'joplin')  # 把函数的运行结果赋值到formatted_name中       
        self.assertEqual(formatted_name, 'Janis Joplin')    # 将函数的运行结果与'Janis Joplin'比较是否相同       
       
unittest.main()     # 让Python运行这个文件中的测试       
```       
       
## 3. 测试类       
       
survey.py       
```python       
class AnonymousSurvey():       
    def __init__(self, question):       
        self.question = question       
        self.responses = []       
       
    def show_question(self):       
        print(self.question)       
       
    def store_response(self, new_response):       
        self.responses.append(new_response)       
       
    def show_results(self):       
        print("Surver results: ")       
        for response in self.responses:       
            print(response)       
```       
       
test_survey.py       
```python       
import unittest       
from survey import AnonymousSurvey       
       
class TestAnonymousSurvey(unittest.TestCase):       
    def test_store_single_response(self):       
        question = "What language did you first learn to speak?"       
        my_survey = AnonymousSurvey(question)       
        my_survey.store_response('English')       
       
        self.assertIn('English', my_survey.responses)       
       
    def test_store_three_responses(self):       
        """测试三个答案会被妥善保存吗"""       
        question = "What language did you first lenarn to speak?"       
        my_survey = AnonymousSurvey(question)       
        responses = ['English', 'Spanish', 'Mardarin']       
        for response in responses:      # 把问题都加入responses列表       
            my_survey.store_response(response)       
        for response in responses:      # 循环依次测试问题是否都在列表my_survey.responses中       
            self.assertIn(response, my_survey.responses)       
       
unittest.main()       
```       
       
* 方法 setUp()       
*在前面的test_survey.py中，我们在每个测试方法中都创建了一个AnonymousSurvey实例，并在每个方法中都创建了答案。在unittest.TestCase类包含的方法setUp()中，让我们只需要创建这些对象一次，并在每个测试方法中使用他们。如果你在TestCase类中包含了方法setUp(),Python将先运行它，再运行各个以test_打头的方法。这样，在你编写的每一个测试方法中都可以使用在方法setUp()中创建的对象了。*       
```python       
import unittest       
from survey import AnonymousSurvey       
       
class TsetAnonymousSurvey(unittest.TestCase):       
    def setUp(self):       
        """创建一个调查对象和一组答案，供使用的测试方法使用"""       
        question = "What language did you first learn to speak?"       
        self.my_survey = AnonmousSurvey(question)       
        self.responses = ['English', 'Spanish', 'Mandarin']       
       
    def test_store_single_response(self):       
        """测试单个答案会不会妥善的存储"""       
        self.my_survey.store_response(self.responses[0])       
        self.assertIn(responses[0], self.my_survey.responses)       
       
    def test_store_three_responses(self):       
        """测试三个答案会别妥善的存储"""       
        for response in self.responses:       
            self.my_survey.store_response(response)       
        for response in self.resopnses:       
            self.assertIn(response, self.my_survey.responses)       

unittest.main()
```