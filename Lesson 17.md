## Learn-python-the-hard-way
### Lesson 17
#### 文件处理
本节继续介绍文件处理，演示了更多函数的应用：  
- exists  
  注意：加了S，语法是exists(filename),直接返回True/False的结果，VBA也有exist，  
  比如dic.exists(x)，判断字典dic是否存在关键字x。  
- cat  
  由第一行开始显示文件内容，是在shell中的命令，不是脚本的代码。  
- len  
  跟Excel上的公式一模一样，都是计算文本字符长度的。
#### 课后思考
被读取文件、被写入文件为什么都要close？      
从结果来看，去掉最后的close语句，也能正常运行。这个区别留待研究。
