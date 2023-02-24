"""
This module contains a more functional approach to composing a single Duck
class with behaviors-as-functions instead of behaviors-as-interfaces. Since
the point of interfaces is to provide behavior, this functionally is no 
different. If you must encapsulate the functions into an interface-like 
package, you can put them into a single module namespace to organize them.
"""

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
