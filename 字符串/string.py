# python的字符串于js的字符串类似，可以用单引号和双引号包裹，但是不能保证正确
# 地闭合，不能混杂
# 错误的例子:message = "hello world'"'

# 字符串首字母变为大写

name = 'ada lovelace'
# 方法调用与js类似,都是.+函数名+()
print(name.title())
#字符串变为大写
print(name.upper());
#字符串变为小写
print(name.lower());

# 字符串拼接用+号,与js相同

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
message = 'Hello, '+ full_name.title()+'!'
print(message)

# 制表符/换行符添加空白，制表符:\t,换行符\n

print('\tPython')
print('\nPython')
print('\n\tPython')

# 去除空白,strip方法会返回一个去除首尾空格的新字符串

favorite_language = ' python  '
print("favorite_language "+favorite_language)
print("favorite_language "+favorite_language.strip())
