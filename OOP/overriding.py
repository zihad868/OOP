class A(object):
    def function1(self):
        print("Class of A")
        

class B(A):
    def function1(self):
        print("Class of B")
        super().function1()


class C(B):
    def function1(self):
        print("Class of C")
        super(C, self).function1()
    
    
c = C()

c.function1()
