class Adder:
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name
        
    def add(self, x,y):
        return x+y