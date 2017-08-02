## Learn-python-the-hard-way
### Lesson 16
#### 文件写入、删除  
1 本课是对文件操作的深入，新介绍了几个文件函数：  
  - truncate清空文件内容
  - write向文件写入内容  
  注意：要写入，open的类型要是可写入，即```open(filename,'w')```
       另外，标识符```\n```也可以作为换行的内容  

2 番外：试了一下用Excel文件跑代码，报错，可能是notepad不支持这种格式。

3 课后练习
  - 如何一次性输入
    课本重写文件时，有3行文本，输入了6次，一次性输入的办法就是把文本合并，如下：  
 ```
    context = line1 +"\n"+line2+"\n"+line3
    target.write(context)
 ```
  - 如果write重写之后，还需要truncate先期清除文件吗     
    代码移除truncate之后，确实没有区别，write的内容自动替代了文本原内容。
