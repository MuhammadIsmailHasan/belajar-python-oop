class A :
    def method(self) :
        print("method dari A")

class B :
    def method(self) :
        print("method dari B")

class C :
    def method(self) :
        print("method dari C")

class D(C, B) :
    pass


d = D()
d.method()
# yang di print adalah method dari C, karena dalam pewarisannya, yg pertama adalah C
