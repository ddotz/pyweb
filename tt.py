class Field(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __eq__(self, other):
        return '%s = %r'%(self.key, other)
    def __lt__(self, other):
        return '%s < %r'%(self.key,other)
class User(object):
    def __init__(self,name=None,age=None):
        self.name=Field('name',name)
        self.age=Field('age',age)
def filter(str):
    return querySql(str)
def querySql(str):
    res = str #看成str处理后的结果
    return res
if __name__ == "__main__":
    user = User('zhang',18)
    print(filter(user.name == 'zhang'))
    print(filter(user.age < 20))
