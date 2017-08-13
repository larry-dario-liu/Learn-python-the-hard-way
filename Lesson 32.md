## Learn-python-the-hard-way
### Lesson 32
#### list列表和for循环
- list的语法  
listname=[元素1,元素2,元素3,...]  
二维list为listname=[[元素a1,元素a2,元素a3...],[元素b1,元素b2,元素b3...]]
- for循环语句  
```
for item in listname:
    依次对list的元素执行运算
```
注意:for行以冒号结尾，而且这里的item变量不用事先声明.
- append()方法  
```
list.append(object)
```
功能是把object添加到list的结尾，list可为空，但是一定要实现声明。
- range()函数  
range()函数可创建一个整数列表，一般用在 for 循环中。  
range(start, end, [step])从start开始，以end的前一个步长结束，不含end,step步长可选默认为1.  
range()函数可以直接赋值给list,```listname=range(start,end)```
