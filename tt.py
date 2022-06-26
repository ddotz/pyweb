class Field():
    def __init__(self):
        pass
class Meta(type):
    def __new__(cls, clsname, bases, attrs):
        print(cls)
        return super(Meta, cls).__new__(
            cls, clsname, bases, attrs)
class Model(metaclass=Meta):
    def do(self):
        pass
    # def __init__(self,name):
    #     self.name = name

class User(Model):
    name = Field()
class Role(Model):
    name = Field
if __name__ == "__main__":
    pass