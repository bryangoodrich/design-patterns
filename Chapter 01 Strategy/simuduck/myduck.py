def no_behavior():
    return ""

def flapping():
    return "I'm flapping!"

def quack():
    return "Quack Quack!"

def squeak():
    return "Squeak Squeak!"

class MallardDuck:
    def __init__(self, fly=flapping, quack=quack):
        self.fly = fly
        self.quack = quack
    
    def __repr__(self):
        return "mallard duck"

class RedheadDuck:
    def __init__(self, fly=flapping, quack=quack):
        self.fly = fly
        self.quack = quack
    
    def __repr__(self):
        return "redhead duck"

class RubberDuck:
    def __init__(self, fly=None, quack=squeak):
        self.fly = no_behavior
        self.quack = quack
    
    def __repr__(self):
        return "rubber duck"

class DecoyDuck:
    def __init__(self, fly=None, quack=None):
        self.fly = no_behavior
        self.quack = no_behavior
    
    def __repr__(self):
        return "decoy duck"
