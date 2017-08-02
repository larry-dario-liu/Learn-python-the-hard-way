## Learn-python-the-hard-way
### Lesson 18-19
#### 自定义函数  
本节非常重要，引入了自定义函数，自定义函数时，需要特别注意格式问题：  
  ```
  def 函数名（变量）：
      函数功能语句1
      函数功能语句2
      ...
  ```
  注意：首行顶格，输入后必须接冒号，后面的行都必须跳格tab一位;函数名  
  不能以数字开头。
我在第一遍学习的时候，因为格式的问题，浪费了大量时间，现在才知道为什么  
作者花这么大篇幅讲function check list.
函数是可以嵌套使用的，例如：  
```
def pluss(x,y):
	return  x + y
def sq(x):
	return x*x
print pluss(sq(3),sq(4))
```
>>25
