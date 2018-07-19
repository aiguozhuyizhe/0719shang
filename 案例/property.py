#定义一个Person类，具有name,age属性
#对于任意输入的姓名，我们希望都用大写方式保存
#年龄，我们希望内部统一用整数保存
# x=property（fget,fset,fdel,doc）
class Person():
    #函数名称可以任意
    def fget(self):
        return self._name*2
    def fset(self,name):
        #以大写形式保存
        self._name=name.upper()
    def fdel(self):
        self._name= "NoName"


    name = property(fget,fset,fdel,"操作了")
p1=Person()
p1.name="xiaojia"
print(p1.name)