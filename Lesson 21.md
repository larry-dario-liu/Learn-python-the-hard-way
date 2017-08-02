## Learn-python-the-hard-way
### Lesson 21
#### 函数可以返回值
前两课只介绍了打印功能的函数，本节的函数介绍了可以返回值的函数，用数学公式概括的讲：  
```
def 函数名（x1,x2...xn）:
    return f(x1,x2...xn)
```
后续调用时，输入函数变量参数即可，可以实现所有数学函数，而且更重要的是，函数之间可以  
相互嵌套，一个函数的运行结果可以作为另一个函数的参数，这跟Excel的嵌套函数一个道理。  
#### 课后思考
拆解实例代码what = add(age, substract(height,multiply(weight,divide(iq,2))))。  
括号的优先级最大，结果等价于what=age+height-weight*(iq/2)。
