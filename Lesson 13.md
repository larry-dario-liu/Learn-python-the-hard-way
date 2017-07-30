## Learn-python-the-hard-way
### Lesson 13
#### 参数输入、模块引入
本节与上节一样，内容都是关于参数输入的方法，但不同的是引入了模块的概念，详见如下代码： 
```
from sys import argv
#注：sys是模块，argv是sys模块的feature，就叫它子模块吧！argv可以实现后续的参数输入功能，简单讲，需要特定功能时，  
我们要先引用，就是有些东西你没必要买它，买多了家里放不下，用的时候要先借，比如单车。
script,first,second,third =argv
#注：script是固定语句，此代码是说把argv收到的输入参数传递给script脚本中的3个变量，first、second、third，那么在  
终端界面输入的时候，一定要包括对应的参数，脚本名（对应script）、参数1（对应变量1）、参数2（对应变量2）、参数3（对
应变量3）
```  
总结：  
- argv至少要包含脚本名变量script，其他变量≥0即可。  
- argv和raw_input()的区别，需要运行前输入参数，后者可以运行的过程中输入，而且可加提示，更灵活但是前者可输入的更多。

