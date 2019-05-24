#去除字符串中的空格
# _*_ coding: utf-8 _*_
def trim(str):
    while str[:1] == " ":
        str = str[1:]
    while str[-1:] == " ":
        str = str[:-1]
    return str
if trim('hello   ') != 'hello':
    print('failed')
elif trim('  hello   ') != 'hello':
    print('failed')
elif trim('') != '':
    print('failed')
elif trim('   ') != '':
    print('failed')
else:
    print('successful')

#取开头和结尾最好用切片：[1:] [-1:]