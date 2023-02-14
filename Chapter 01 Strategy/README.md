# The Strategy Pattern

This chapter has a few design principles. I'll recap them here and then give my take in general on designing algorithms from a functional programming perspective.

### Design Principle 1

    Identify the aspects of your application that vary and separate them from what stays the same.

In other words, encapsulate what varies (e.g., into functions, modules, or classes), allowing you to alter or extend those sections while not impacting the rest. This forms the basis of most design patterns as strategies to accomplish this goal.

### Design Principle 2

    Favor composition over inheritance.

While most people learn OOP via Java with a strong emphasis on inheritance, a lot of the flexibility in designing systems comes from composition. Inheritance to me should be justified and driven by domain-design. Even then, composition should be preferred--that is to say, even your data types and objects should be defined via composition from simpler times than merely by relational inheritance. 

It should be pointed out that inheritance is an IS-A relationship (a Honda is-a subtype of car). What we should aim for are HAS-A relationships (a Honda has-a set of tires, has-a engine, etc.). 

## Functional Programming Perspective

As an alternative to using classes, or at least thinking in terms of objects, we can encapsulate data and behavior in a number of ways. 

### Interfaces 

These are basically a class of behaviors. They can have supporting attributes, but whereas objects tend to be thought of as data + behavior, interfaces are behavior + optional data. In terms of imperative and functional programming design, it is not uncommon to encapsulate common behaviors into a single reference object. Another way of thinking about these are as modules, but with a class instantiation. 

### Modules

If you have a class object that is all static methods, you don't need to instantiate it. That, to me, is truly a module. Python has 2 ways to implement these. Obviously using static classes will accomplish this goal. The nice thing here is you can co-locate multiple such interfaces in a single package module. Alternatively, and an approach I tend to take, is to create actual python modules as purely coding modules. Compare the 2 approaches here. 


Using classes (suppose in Math.py in a package)
```
class Math:
    @staticmethod
    def add(a, b):
        return a+b
    
    @staticmethod
    def sub(a, b):
        return a-b
```

Using modules (as just the content in Math.py in a package)
```
def add(a, b):
    return a+b

def sub(a, b):
    return a-b
```

And using either of them
```
import Math as M  # module approach
from Math import Math  # class approach

M.add(1, 2)
Math.add(1, 2)
```

I think there are good reasons to use classes when you are trying to build an interface and there are additional class variables to support that contract and their use. However, for most simple encapsulation models, just using a Python module as the actual module you import like a class dispatch accomplishes the same thing with less overhead. Additionally, the module itself can have additional code and variables defined, such as constants and helper functions not implicitly exposed on import. 

## Should we use objects?

To this question I mean should we use "data + behavior"? My answer in most cases is no. We can use class machinery to implement a lot of the same content in easier-to-maintain code, but thinking purely in terms of defing class objects distracts from the separation of concern between data and behavior. Instead, I emphasize a domain-driven design approach. First define your data (types). Then define your behavior for how you interact with and relate those data (functions). The composition of data and composition of functions takes very simple imperative designs into a large body of services that can be reused wherever they apply. It's as loosely coupled as you can get! 
