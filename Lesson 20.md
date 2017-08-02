## Learn-python-the-hard-way
### Lesson 20
#### 自定义函数与文件操作  
本节实例代码把函数和文件结合，并介绍了1个新函数：  
- readline()
  方法用于从文件读取整行，包括 "\n" 字符，括号内空值时默认整行，  
  有>=0的整数时，就规定了读取的最大字长，规定字长比文件大，就用空格填充。
```
print open(filename).readline()
```
  readline是从当前指针初开始的一行读取，这也是教材立体的核心原理，作者调  
  用了3次ReadLine就读取了三行。但是我自己把代码简化，去掉f=open(filename),  
  直接用三个```print open(filename).readline```就重复读取了第一行，这是  
  因为每次都重新打开了文件，从第一行开始。
 - seek  
   调整指针的位置，如何把教材的seek(0)函数去掉，则readline都是空值，因为  
   在ReadLine运行前，文件指针已经在文件末尾了，此时ReadLine对象是空值，读取  
   的结果自然无效。
 #### 总结：  
 一定要对代码进行各种肢解、折腾才能更清晰了理解含义。
