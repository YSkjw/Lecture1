class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()

class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()

class D(B, C):
    def hello(self):
        print("Hello from D")
        super().hello()

class E(C):
    pass

class F(B, E):
    pass

class G(E, B):
    pass

print(F.__mro__)
print(G.__mro__)
try:
    class H(G, F):
        pass
except Exception as e:
    print(e)

# F MRO: F, B, E, C, A, object
# G MRO: G, E, C, B, A, object
# MRO error occurs because Python cannot create a consistent method resolution order for H(G, F).



