## Learn-python-the-hard-way
### Lesson 33  
#### while-loops循环  
- while-loop的语法  
```
while 条件判断：
     （判断为真时）执行运算     
```  
条件判断为真时，执行循环，否则跳出循环,条件判断一定要有终点即为false，否则无限循环.  
- continue和break命令  
  continue 用于跳过该次循环，break 则是用于退出循环。  
  示例如下：  
```
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:      
        continue        
    print n
```
此处用到break，偶数时跳出整个循环，print结果为1,但是当我把break替换成continue时，print为1,3,5,7,9。  
而其实continue仅仅跳出单次循环，用处不大，if函数本身可以实现，上述语句if改成不等于0即可。  
思考:*上例中为什么n=n+1放在print语句前面，就无法运行呢？*  
- 课后习题，结合while-loop和自定义函数  
```
def printlist(a):
	i= 0
	num= []
	while i < a:
		num.append(i)
		i=i+1
	print num
printlist(int(raw_input("??? ")))	
```  
- 课后习题，结合for循环和自定义函数  
```
def printlist(a):
	i= 0
	num= []
	for i in range(1,a,2):
		num.append(i)
		i=i+3 #此处无效，步长已经在range规定了 
	print num
printlist(int(raw_input("??? ")))	  
```
