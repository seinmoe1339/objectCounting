class  Stack(object):
    def __init__(self):
        self.stack=[]
    def push(self,object):
            self.stack.append(object)
    def pop(self):
            return self.stack.pop()
    def length(self):
            return len(self.stack)

s=Stack()
s.push("Dave")
s.push(42)
s.push([3,4,5])
Z=s.length()
print(Z)
x=s.pop()
print(x)
y=s.pop()
print(y)
del s

