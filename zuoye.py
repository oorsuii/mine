
# #day01通过代码获取两段内容，并且计算他们长度的和
# a = len(input("请输入a的值："))
# print("a的长度：",a)
# b = len(input("请输入b的值："))
# print("b的长度：",b)
# print("字段长度和",a+b)


#day02在字典里输入name、age、sex
d = {}
print(d)
a= input("请输入姓名：")
b = input("请输入年龄：")
c = input("请输入性别：")
d.update(name=a)
d.update(age=b)
d.update(sex=c)
print(d)