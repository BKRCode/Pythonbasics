 # Eine Liste oder(An- ) Sammlung


from typing import override


class Stack(list):
    
    def push(self, item) -> None:
        super().append(item)

    @override
    def pop(self) -> object:
        if len(self) == 0:
            print("Nichts Da zum entfernen.")
        return super().pop()
    
class Limited_Stack(Stack):
    @override
    def __init__(self, limit):
        super()
        self.limit = limit
    
    @override
    def push(self, item) -> bool:
        if len(self) == self.limit:
            return False
        self.append(item)
        return True
    
def run2():
    l = Limited_Stack(3)
    l.push("1")
    l.push("2")
    l.push("3")

    
def run():
    stack01 = Stack()
    stack01.push("Regenschirm")
    print(stack01)
    stack01.push("Regentonne")
    print(stack01)
    stack01.pop()
    stack01.push("Gummistiefel")
    print(stack01)
    stack01.pop()
    stack01.pop()
    stack01.pop()
    print(stack01)

if __name__ == '__main__':
     run2()   