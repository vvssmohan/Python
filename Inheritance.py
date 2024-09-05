#Single inheritance


class parent:
    def method1(self):
        print('i am a parent')

class child(parent):
    def method2(self):
        print('i am a child')

child1=child()
child1.method2()
child1.method1()