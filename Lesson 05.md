## Learn-python-the-hard-way
### Lesson 5
#### More variables and printing
本章依旧是讨论变量，不过增加如何把文本和变量结合。注意：文本是为了人阅读而用的。  
代码示例：  
```
print "nice to meet %s."%yourname
```
写法上，其实有点拐弯抹角，先输入文本，文本中需要被替代的地方写类似```%s```的格式符，输玩文本后写```%加变量名```即可。注意：这里实际上增加了变量的数据类型限定。  
相比VBA就直观多了:  
```
msgbox "nice to meet"& yourname
```
不过Python变量也可以批量带入，只要结尾的%加上括号，括号内可写入多个变量。当然，文本内的格式符数量和最后变量输入数量必须一致。
#### format character
- %r 表示所有格式
- %s 表示文本格式string
- %d 表示整数decimal
- %f 表示浮点数即带小数点float
