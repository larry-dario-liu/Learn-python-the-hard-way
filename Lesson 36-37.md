## Learn-python-the-hard-way
### 笨办法学Python的在线笔记
#### 概念及符号自查
1. lambda
  用来创建无名函数，一次性的用后即废.  
 1.1 简例
```
f = lambda x,y:x+y
print f(3,4)
>>7
```  
 1.2 语法
总结来看，lambda的语法较简单，即：  
```
函数名y=lambda 变量x1,x2,x3....:函数f(x1,x2,x3...)
y(参数1，参数2，参数3)
```  
 1.3 再例  
```
mults = filter(lambda x:x%4==0,[0,2,4,6,8,10,14])
print mults
>>[0,4,8]  
```  
总结：lambda可以达到简化自定义函数的目的。
