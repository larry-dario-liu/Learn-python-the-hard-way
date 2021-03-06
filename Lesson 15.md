## Learn-python-the-hard-way
### Lesson 15
#### 文件读取  
本节介绍了如何从外部文件取数，隐隐感觉这个功能很强大。简而言之，就是两步：  
1 从外部文件传递数据  
```
变量=open(外部文件全名)
```  
用了open函数。这里的前提是Python的脚本在一个文件夹下（估计不在一个文件夹也可以操作，
只是需要加入路径描述，这个等以后来验证）。
2 通过print变量显示外部文件的内容  
```
print 变量.read()
```  
此处用到read函数，读取文件内容，我尝试了不用函数直接打印，即：  
```
print 变量
```  
直接打印也不会报错，打印结果如下:  
<open file 'ex15_sample.txt',mode 'r' at 0x005FD1D8>  
不用read函数的情况下，打印出来的只是变量的执行open的这个过。但是*不清楚mode 'r'的意思*。
注意:作者提到了hard coding，简单讲就是事前直接输入参数或文本，而不是在运行过程中产生  
（比如从外部文件读取、代码运行内部生成），俗称硬编码，硬编码适用性比较差。
3 简化
  open和read可以连在一起写，从而简化代码，如下：
```
printext=open(filename).read()
print printext
```
4 课后思考
  - 此例中，用argv和raw_input()哪个更好？  
    仅就本例来说，真看不出来。  
  - 跑pydoc了解read函数
    "read at most size bytes,return as a string",因此read返回的结果是文本类型。
  - 是否要运行close()函数
    虽然教材的代码运行了open函数，而且最后也没有close处理，但是并没有看到TXT的打开窗口，  
    从结果来看close并不是必要的。但是从pydoc的解释来说，运行close就不能做I/O操作了，即  
    read就无法进行了。虽然必要性不大，但是看得出及时关闭是良好的编程习惯。
