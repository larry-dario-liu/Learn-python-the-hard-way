## Learn-python-the-hard-way
### Lesson 38
#### list列表处理
#### 1. list列表方法的处理逻辑   
本节作者讲解了python list方法的运行机制，非常重要。   
mystuff.append("hello")运行时，（1）首先，程序要寻找mystuff，看是变量还是函数，本例是一个list变量；   
（2）逗号，启动程序去识别所有list的函数；（3）append，启动程序去定位list的append函数；（4）append函
数首先要找到一个变量，就是对象本身，mystuff.append("hello")实质为append(mystuff,'hello'),因此不难
理解，为什么说mystuff.append("hello")有2个参数。   
#### 2. 代码修改
承接1.知识点，教材列示了一段参数数量错误代码：  
```
class thing(object):
  def test(hi):
      print "hi"
a = thing()
a.test("hello")
```  
运行代码，会显示参数数量错误，需要1个提供了2个。这是因为定义函数test只含1个变量，而输入参数时a.test("hello")  
实际是test(a,"hello")有2个变量，这就是区别。修正方法，把test(hi)修改成test（self，hi）即可。  
#### 3.join文本方法
语法如下：  
```str.join(sequence)```,str是文本链接符号，例如空格、“-”等，sequence是被连接的序列list，代码举例：  
```
thing = "i'11 code all day long"
stuff = thing.split(" ")
print ' '.join(stuff) #这里的str用双引号、单引号都可以
```
#### 4.list列表的部分截取  
list=[元素1，元素2，...元素n]，我们如果只需要部分元素，可以用list[1:6]截取。注意这个范围取值不含最后一个，0表  
示第1个。
