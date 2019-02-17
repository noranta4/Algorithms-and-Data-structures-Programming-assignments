__author__ = 'Antonio Norelli'

#I create a new class using a list of lists and performing operations with built-in function append(item) and pop()
#I have two values to use properly the SetOfStacks:
#item_last_stack (# of item in the last stack) and stack (index of currently stack)

#COST all single operations are O(1),
#I think python compiler memorizes the size of every list and do in O(1) also append(item) and len(list)

#................................................................................................................

#PROGRAM

class SetOfStacks(object):
    def __init__(self, threshold): #threshold included in the declaration
        self.threshold = threshold
        self.set = [[]]
        self.item_last_stack = 0
        self.stack = 0
    def push(self, item):
        if self.item_last_stack < self.threshold: #if last stack isn't full
            self.set[self.stack].append(item)
            self.item_last_stack += 1
        else:
            self.stack += 1
            self.set.append([]) #create a new stack
            self.set[self.stack].append(item)
            self.item_last_stack = 1
    def pop(self): #possible situation: [[], [0,1], [], []] before pop we have to delete the last two empty stacks
        while self.item_last_stack == 0: #while the last stack is empty
            del self.set[-1] #delete last stack
            self.stack -= 1
            self.item_last_stack = len(self.set[self.stack])
        self.item_last_stack -= 1
        return self.set[self.stack].pop()
    def popAt(self, index):
        if self.stack < index:
            print 'Sorry, but this stack does not exist'
        if len(self.set[index]) == 0:
            print 'This stack is empty'
        else:
            return self.set[index].pop()

#SAMPLE INPUT AND USE

sample = SetOfStacks(3)

for i in range(10):
    sample.push(i)
print 'Sample SetOfStacks: ', sample.set, '\n'

print 'pop five times on sub-stack 1 \nrunning...'
for i in range(5):
    sample.popAt(1)
print '... \nresult: ', sample.set, '\n'

print 'push new item 42'
sample.push(42)
print 'result: ', sample.set, '\n'

print 'pop six times'
for i in range(6):
    sample.pop()
print 'result: ', sample.set









