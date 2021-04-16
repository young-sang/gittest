class claculator:

    def __init__(self):
        self.result = 0
    
    def add(self,num):
        self.result += num
        return self.result

class FourCal:

    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first +self.second
        return result

a = FourCal()
a.setdata(4,2)
print(a.add())
print(a.first)
print(type(a))
print(id(a.first))