'''
        The complicity is O(1) of the enqueue().
        The complicity is O(n) of the dequeue().
'''
#FIFI
#Queue = First in first Out

class Queue:
    def __init__(self):
        self.item = []

    #Add kora
    def Enqueue(self,New_Data):
        self.item.append(New_Data)

    #remove kora
    def Dequeue(self):
        return self.item.pop(0)

    def is_empty(self):
        if self.item == []:
            return True
        return False

if __name__ == '__main__':
    q = Queue()
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
    while not q.is_empty():
        person = q.Dequeue()
        print(person)

