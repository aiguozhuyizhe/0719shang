class Person():
    #函数名称可以任意
    '''
    zheshi
    '''
    def fget(self):
        print("我的年龄是{0}".format(self._age))
    def fset(self,age):
        #以大写形式保存

        self._age=int(age)
    def fdel(self):
       return

    age = property(fget, fset, fdel, " ")

p1=Person()
p1.age=23.5
print(p1.age)
print(" * " * 20)

print(Person.__doc__)
print(Person.__dict__)
print(Person.__bases__)
print(Person.__name__)