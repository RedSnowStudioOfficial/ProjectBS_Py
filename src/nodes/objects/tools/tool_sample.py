class Object_Tool:
    def __init__(self, name : str(), health : int(), damage : int(), pic ):
        self.name = name
        self.health = health
        
        self.damage = damage

        self.state = 1 #1 = Stable; 0 = Broken.
        
        self.pic = pic
    