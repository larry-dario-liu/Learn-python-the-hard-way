## Learn-python-the-hard-way
### Lesson 10
#### 转义字符:反斜杠  
从教材的描述看，就是反斜杠加上相应字符，放在文本中达到避免混淆、特殊排列等效果。  
文本中的转义字符包括：
- \t    制表符，t被视为tab，而不是文本t
- \n    换行，n被视为换行，而不是文本n
- \\    单斜杠，如果要显示斜杠，必须输入2个
- \'    单引号，被视为文本内的单引号，避免重复
- \''   双引号，被视为文本内的双引号，避免重复
- \b    退格，被视为backspace键，退格和缩进反方向，但退格是1个字符，缩进是2个。
- \r    回车，重回行首，即\r后的输出结果从行首开始，这样可以后进先出。  
```
print "10\r9"
```
输出结果是90，即该行会先输出\r后的文本，替换掉转移符前的相同长度的文本。  
注意：双引号和单引号都可以框住文本，形成文本语句，目前看没有区别。
#### 课后思考  
课后思考是一个很简短却很炫酷的代码，实现打印出来像以中点为轴的旋转棒，代码如下:
```
while True:
  for i in ["/","-","\","|"]:
    print "%s\r"%i,
```
代码的关键在于print语句的逗号和转移符\r，print语句的逗号表示在一行打印，然后\r回车重回行首覆盖，形成不断替换的效果。这两个是代码生效的关键。另外，测试得出```\r```放在```%s```前后都有效。

  
