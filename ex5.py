x = "there are %d types of people." %10
binary="binary"
do_not = "don't"
y = "those who know %s and those who %s" %(binary,do_not)

print x
print y

print "i said: %r." %x
print " i alse said:'%s'."%y

hilarious = False
joke_evaluation = "isn't that joke so funny?!%r"
#变量分拆
print joke_evaluation% hilarious 

w = "this is the left side of ..."
e = "a string with a right side."
# 字符串可以实现+的链接
print w + e

