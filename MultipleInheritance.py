class A:
    def A(self):
        print("Class A")
    
class B:
    def B(self):
        print("Class B")

class C(A, B):
    def C(self):
        print("Class B")
    

c = C()
c.A()
