import re

# findall返回值为list
sen = "gopythonc++java"
print(re.findall('python', sen))

sen = "<html><h1>hello<h1></html>"
print(re.findall('<h1>(.*)<h1>', sen))

sen = "I don't like the girl higher than 165 cm."
print(re.findall('\d+', sen))

sen = "https://www.baidu.com and http://www.baidu.com"
print(re.findall('https?://\S*', sen))

sen = "lalala<html>hello</HTML>hahahah"
print(re.findall('<[Hh][Tt][Mm][Ll]>(.*)</[Hh][Tt][Mm][Ll]>', sen))

# sjtu.edu and sjtu 都符合@(.*)\. 所以要用? 区别贪婪与不贪婪
# .*代表贪婪，越长越好  .*?代表不贪婪，越短越好
# 由于.是一个特殊字符，所以用\.表示'.'
sen = "lalala@sjtu.edu.cn"
print(re.findall('@(.*?)\.', sen))

sen = "haaa haa haahha haahhaaa ahhahaa"
print(re.findall('ha{1,2}h', sen))

