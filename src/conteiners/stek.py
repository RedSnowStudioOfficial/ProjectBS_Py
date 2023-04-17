class Node:
    def __init__(self, elem):
        '''
        Node - вспомогательный класс-контейнер
        являеться вспомогательной ссылкой на последовательность
        объекта ресурса или события в очереди.

        ПОНЯТЬ КАК ВЫТАСКИВАТЬ ИЗ НЕГО ОБЪЕКТЫ И ПЕРЕКЛАДЫВАТЬ В ДРУГИЕ
        КОНТЕЙНЕРЫ!
        '''
        self.elem = elem
        self.nextNode = None

class Stek:
    def __init__(self):
        self.top=None
        
    def Push(self, elem):
        new=Node(elem)
        new.nextNode = self.top
        self.top = new
        if self.top is None: #Если Стек пуст.
            self.top = new #Ссылка top начинает ссылаться на новый эелемент!
        else:
            new.nextNode = self.top
            self.top = new
    
    def Pop_Out(self, elem):
        if self.top is None:
            print("Stek is already empty!")
        else:
            obj = self.top.elem
            self.top = self.top.next_Node
            return obj
    
    def Top_Return(self):
        return self.top.elem
    
    def isEmpty(self) -> bool:
        if self.top is None:
            return True
        else:
            return False
    
# st1=Stek()
# st1.Push(12)
# print(st1.top.elem)
# print(st1.top.nextNode)

# st1.Push(22)
# print(st1.top.elem)
# print(st1.top.nextNode)

# if st1.isEmpty() == True:
    # print("Empty!")
# else:
    # print("We have something!")

# print(">>>>>>CUSTOM<<<<<<")

# new_resource = Node("Half-Life 3 is real!")

# LibStek = SteckMass()

# if LibStek.isEmpty(SM.SteckMass) == True:
    # print("Empty!")
# else:
    # print("We have something!")