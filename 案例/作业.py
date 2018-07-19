#1,在用户输入年龄的时候，可以输入整数，小数，浮点数
#2，单内部为了数据清洁，我们统一需要保存整数，直接舍去小数点
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


print(Person.__doc__)
