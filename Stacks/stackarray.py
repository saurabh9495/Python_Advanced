class mystack():
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    
stac = mystack()
print(stac.push(1))
print(stac.push(2))
print(stac.push(3))
print(stac.push(4))
print(stac.push(5))
print(stac.isEmpty())
print(stac.peek())
print(stac.size())
print(stac.pop())
print(stac.pop())