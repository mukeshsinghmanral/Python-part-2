class Student:
    def __init__(self,name,rollno,hobby,rank):
        self.name=name
        self.rollno=rollno
        self.hobby=hobby
        self.rank=rank
    def show(self):
        print('outer class:')
        print(self.name,self.rollno,self.hobby,self.rank)
    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram
        def show(self):
            print('inner class')
            print(self.brand,self.cpu,self.ram)
m1=Student('mukeshmanral',46,'cricket',1)
m1.show()
lap=Student.Laptop('dell','ryzen5','8gb')
lap.show()