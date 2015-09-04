#Stack Implementation
class Stack:
        def __init__(self):
                self.items = []

        def push(self, number):
                self.items.append(number)

        def pop(self):
                return self.items.pop()

        def checkSize(self):
                return len(self.items)


#stack test
print "Running Test Stack"
testStack = Stack();
for (i) in range (10):
	testStack.push(i)

while testStack.checkSize() != 0:
	print testStack.pop()	
	print "size: " + str(testStack.checkSize())
