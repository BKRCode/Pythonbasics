from typing import override


class Queue(list):

    def enqueue(self, item) -> None:
        super().append(item)

    

    def dequeue(self) -> object:
        if len(self) == 0:
            print("Gibt nix zum entfernen")
        return super().pop(0)
    

def run1():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Welcome contestants ..", q)

    print("Dequeued.. disqualified", q.dequeue())

    print("Remaining:", q)
      

run1()
