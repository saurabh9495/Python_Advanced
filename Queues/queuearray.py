class myqueue:
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        self.queue.pop(0)
        
    def peek(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.queue == []
    
    
queue = myqueue()
print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
print(queue.peek())
print(queue.dequeue())
print(queue.size())
print(queue.isEmpty())