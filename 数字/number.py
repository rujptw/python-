# 整数

print(2+3)
#乘方运算和js最新的乘法运算相同,都是**，以前js是Math.pow()
print(2**3)

# python支持运算顺序的修改，使用（）能使运算顺序更加优先
print(5*(4+3))

# 浮点数

# 和js一样都存在着精度问题
print(0.1+0.2) # 0.30000000000000004
print(3*0.1) #0.30000000000000004

# 类型错误，python是一种强类型的语言，数字类型不能直接与字符串类型相加，需要进行转化

age = 23;
# message = 'Happy '+ age + 'rd Birthday'

# print(message)  # TypeError: can only concatenate str (not "int") to str
# str方法将某一类型的数据转化为字符串
rightmessage = 'Happy ' + str(age) + 'rd Birthday'

print(rightmessage);

# python 2版本整数相除，会直接舍弃小数部分，python 3则会保留
# python 2中，相除要保证其中一个位浮点数，这样小数点才不会被舍弃
