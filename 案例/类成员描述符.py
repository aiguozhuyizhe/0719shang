#创建Student类，描述学生类
# 学生具有Student.name属性
#但name格式并不统一
class Student():                #这是初始化，如果要直接赋值则：
    def __init__(self,name,age):  # def __init__(self):
        self.name = name          #    self.name =  "XXX"
        self.age = age            #    self.age = 23    这是直接赋值
        self.setName(name)
        self.setAge(age)

    def intro(self):
        print(" Hai ,my name is {0},age is {1}".format(self.name,self.age))
    def setName(self,name):
        self.name= name.upper()
    def setAge(self,age):#将年龄转换为整数
        self.age=int(age)

s1=Student("xiaojia",23.8)
s2=Student("michi stangle",24.5)
s1.intro()
s2.intro()

