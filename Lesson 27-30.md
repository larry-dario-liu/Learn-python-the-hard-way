## Learn-python-the-hard-way
### Lesson 27-30  
#### 逻辑运算  
  if条件语句，语法如下:  
  ```
  if 判断语句：
       判断成立时运算
  if my_age >= 20:
      print "you should work hard"
  ```  
  判断语句后一定要有冒号、要有冒号、要有冒号，条件运算语句要后缩进。  
  if条件语句的变式：  
  ```  
  if 判断语句a:  
      判断语句a成立时运算  
  elif 判断语句b:  
      判断语句b成立时运算  
  else:  
      a、b以外其他情况下运算  
  ```
注意：判断变量与值是否相等时，用双等号==，而不是单等号，单等号是赋值。  
如下编写的if嵌套语句，总是出错，输入100会print出200的结果*留待解决*：  
```
var = raw_input("variable is ")
if var > 200:
  print "Expression value is more than 200"
else:
  print "Could not find big value expression"
  if var == 150:
   print "Which is 150"
  else:
   print "Expression value is less than 50"
```  
*通过咨询学友00，解决了问题。*即：用raw_input输入的数值，默认为文本，当我直接输入100时，  
系统判断为文本的100那的值比数值200还要大。  
结论是python的if函数，可以用常规方式嵌套，缩进4位。
