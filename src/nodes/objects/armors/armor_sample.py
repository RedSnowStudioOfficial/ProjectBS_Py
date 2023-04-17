class Object_Armor:
    def __init__(self, name : str(), health : int(), resist : int() ):
        self.name = name
        self.health = health
        self.resist = resist
        
        self.state = 1 #1 = Stable; 0 = Broken.

    def print_stats(self):
        if self.state == 1:
            print("Название ->", self.name)
            print('Прочность ->', self.health)
            print('Сопротивление урону ->', self.resist)
        else:
            print("Название ->", "Сломанная " + self.name)
            print('Прочность ->', self.health)
            print('Сопротивление урону ->', self.resist)