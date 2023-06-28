class PrivateMemberException(Exception):
    pass


class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c

    def display(self):
        print("Values in class A:")
        print("a =", self.__a)
        print("b =", self._b)
        print("c =", self.c)


class B(A):
    def display(self):
        super().display()

        try:
            print("Values in class B:")
            raise PrivateMemberException("Cannot access private member 'a'")
        except PrivateMemberException as e:
            print("Exception:", str(e))
        finally:
            print("b =", self._b)
            print("c =", self.c)


o=B(1,2,3)
o.display()
