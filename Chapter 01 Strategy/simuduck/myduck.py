def no_behavior():
    return ""

def flapping():
    return "I'm flapping!"

def quack():
    return "Quack Quack!"

def squeak():
    return "Squeak Squeak!"

class Duck:
    def __init__(self, description, flybehavior, quackbehavior):
        self.fly = flybehavior
        self.quack = quackbehavior
        self.type = description
    
    def __str__(self):
        return str(self.type)
    
    def __repr__(self):
        return str(self)

MallardDuck = Duck("mallard duck", flapping, quack)
RedheadDuck = Duck("redhead duck", flapping, quack)
RubberDuck = Duck("rubber duck", no_behavior, squeak)
DecoyDuck = Duck("decoy duck", no_behavior, no_behavior)
