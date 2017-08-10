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
如下编写的if嵌套语句，总是出错，*留待解决*：  
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
