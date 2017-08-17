## Learn-python-the-hard-way
### Lesson 39 字典
#### 1. list的可更改特性  
list不仅仅可以添加，所有位置的已存在的元素都能被替换。  
#### 2. dict字典用法  
前言：python的字典用法与VBA极像。

- 典型字典格式
```
dict={键1：项1，键2：项2....键n:项n}
```
键不可重复，重复输入键的项值，已后者为准，同vba。
- 添加dict[关键字i]=项i   
- 删除某项del dict[关键字i]
- 删除字典del dict
- 清空dict.clear（）
- 返回指定值dict.get(键)
- 判断键存在dict.has_key(键) *同VBA dict.exists(键)*   
- 返回所有键dict.keys() *同VBA* 
- 返回所有值dict.values()*VBA是dict.items*
- 返回所有键值数组dict.items()

注意：区别dict.clear()与del dict，前者仅仅是清空字典，保留一个空字典，后者是彻底清除字典；  
dict采用hash算法数据是无序的，如果需要有序，则要引用collections包的orderedDict模块。


