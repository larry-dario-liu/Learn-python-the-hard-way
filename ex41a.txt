from urllib import urlopen
doc = urlopen("http://www.baidu.com").read()
print doc