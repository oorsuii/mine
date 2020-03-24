"""
print("hello world")
print(2333) # 整数
print(1.111111) # 小数
print(True) # 布尔值
print(()) # 元祖
print([]) # 数组
print({}) # 字典


print("哈哈哈哈", 233333)
print("嘻嘻"+"哈哈") #字符串的拼接，只能同类型的字符串进行拼接，比如不能汉字和数字进行拼接
print("哈哈哈"*100) #乘
print(((1+2)*100-99)/2) #运算
print(2>3) #布尔值判断 False
print(2<3) #布尔值判断True


#变量、赋值
name = "张三" #name是变量 张三是赋给name的值
print(name)


#input方法
a = input("请输入：") #通过input获取的都是字符串
print("input获取的内容：",a)


#通过input获取的都是字符串,只能拼接
a = input("请输入：") 
b = input("请输入：")
print("input获取的内容：",a+b)
"""

"""
#type方法
# print(type("哈哈哈"))   #字符串str
# print(type(66666))     #整数int
# print(type(2.666666))  #小数float
# print(type(True))      #布尔值bool
# print(type(()))        #元祖tuple
# print(type([]))        #数组list
# print(type({}))        #字典dict


# #将整数型转化为字符串
# a = str(666)
# print(type(a))


#将小数型转化为字符串
# b = int(2.33333)
# print(type(b))


#将字符串类型转换为整型之后才能做加法，否则只能做拼接
# a = int(input("请输入a的值：")) #input里面可以输入任何类型的数据，但是通过input获取的都是字符串,只能拼接
# b = int(input("请输入b的值："))
# print("a+b：",a+b)

#通过代码获取两段内容，并且计算他们长度的和
# a = len(input("请输入a的值："))
# print("a的长度：",a)
# b = len(input("请输入b的值："))
# print("b的长度：",b)
# print("字段长度和",a+b)

# a = len(input("第一段内容："))
# b = len(input("第一段内容："))
# print("字段长度和：",a+b)
"""


a = input("请输入a的值：")
print("a的内容：",a)
b = len(a)
print("a的内容的长度",b)
c = input("请输入c的值：")
print("c的内容：",c)
d = len(c)
print("c的内容的长度",d)
print("a和c内容的长度和：",b+d)

# a = input()
# print(a)
# b = len(a)
# print(b)
# c = input()
# print(c)
# d=len(c)
# print(d)
# print(b+d)

