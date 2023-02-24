"""
SimUDuck Package

This layout mirrors that from the book.
"""


from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        return "I'm flapping!"

class FlyNoWay(FlyBehavior):
    def fly(self):
        return ""


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        return "Quack Quack!"

class Squeak(QuackBehavior):
    def quack(self):
        return "Squeak Squeak!"

class MuteQuack(QuackBehavior):
    def quack(self):
        return ""


class Duck(ABC):
    def __init__(self, flybehavior=None, quackbehavior=None):
        self.wings = flybehavior if flybehavior is not None else FlyNoWay()
        self.beak = quackbehavior if quackbehavior is not None else MuteQuack()
    
    @abstractmethod
    def __repr__(self):
        pass
    
    def swim(self):
        print(f"a swimming {self}.")
    
    def performQuack(self):
        return self.beak.quack()
    
    def performFly(self):
        return self.wings.fly()
    
    def setFlyBehavior(self, behavior):
        self.wings = behavior
    
    def setQuackBehavior(self, behavior):
        self.beak = behavior

class Mallard(Duck):
    def __init__(self):
        Duck.__init__(self, flybehavior=FlyWithWings(), quackbehavior=Quack())
    
    def __repr__(self):
        return "mallard duck"

class RedHead(Duck):
    def __init__(self):
        Duck.__init__(self, flybehavior=FlyWithWings(), quackbehavior=Quack())
    
    def __repr__(self):
        return "redhead duck"

class Rubber(Duck):
    def __init__(self):
        Duck.__init__(self, flybehavior=FlyNoWay(), quackbehavior=Squeak())
    
    def __repr__(self):
        return "rubber ducky"

class Decoy(Duck):
    def __init__(self):
        Duck.__init__(self, flybehavior=FlyNoWay(), quackbehavior=MuteQuack())
    
    def __repr__(self):
        return "not a duck"
