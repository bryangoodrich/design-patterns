# The Observer Pattern

The observer pattern defines a `subject` or `observable` that can be related to `observers` that will respond whenever the `subject` notifies them of changes in its state. It is often thought of as a "pub-sub" model where observers subscribe to the `subject` which publishes whenever things change. 

The book uses the common example of a weather station. The weather station is observable and provides periodic data updates. Subscribed observers can then use that data to update their views (e.g., readings, summaries, visuals, etc.). Another common example is an online marketplace. The marketplace is the `subject`, and the users who are interested in a particular product are the `observers`. Whenever the availability or pricing of a product changes, the marketplace notifies its users, and they can respond accordingly. 


### Design Pattern 1


### A Functional Alternative and More

Suppose we have a generic design in Python like this.

```
class Subject:
    def __init__(self):
        self._observers = set()
    
    def attach(self, observer):
        self._observers.add(observer)
    
    def detach(self, obsrver):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class DisplayObserver(Observer):
    def update(self, message):
        print(f"DisplayObserver receieved message: {message}")

class LogObserver(Observer):
    def update(self, message):
        print(f"LogObserver received message: {message}")

# Usage
subject = Subject()
observer1 = DisplayObserver()
obsrever2 = LogObserver()

subject.attach(observer1)
subject.attach(observer2)
subject.notify("Hello, World!")
# Output:
# DisplayObserver receieved message: Hello, World!
# LogObserver received message: Hello, World!

subject.detach(observer1)
subject.notify("Goodbye, World!")
# Output:
# LogObserver receieved message: Goodbye, World!
```

We see here the classic OOP interface design where we encapsulate the specific observer behaviors inside classes. This is Python, so it begs the question, does all the extra lines of code add anything when we just need functions? Compare this to using `callbacks`. A callback is a function that is called in response to another function being called, often used in asynchronous communications, like a callback to notify you when an asynchronous activity has finished processing. If we refactor the above code to treat our observers as callbacks, we get a more sleek, yet similar design.

```
class Subject:
    def __init__(self):
        self._callbacks = []
    
    def attach(self, callback):
        self._callbacks.add(callback)
    
    def detach(self, callback):
        self._callbacks.remove(callback)
    
    def notify(self, message):
        for callback in self._callbacks:
            callback(message)

def display_observer(self, message):
    print(f"DisplayObserver receieved message: {message}")

def log_observer(self, message):
    print(f"LogObserver received message: {message}")

# Usage
subject = Subject()

subject.attach(display_observer)
subject.attach(log_observer)
subject.notify("Hello, World!")
# Output:
# DisplayObserver receieved message: Hello, World!
# LogObserver received message: Hello, World!

subject.detach(display_observer)
subject.notify("Goodbye, World!")
# Output:
# LogObserver receieved message: Goodbye, World!
```

With this implementation, in place of interface classes that support a generic `update` method, we instead define the `observer` as simply a function that responds to the message. We get the same loose coupling without the abundant OOP pageantry. To me, this is already a step in the right direction: favor direct function use instead of encapsulating in unnecessary classes. Furthermore, if you're defining classes that consist of one function and a constructor, you just need a function! 

But wait, we can go further beyond! By using *closures* we can avoid the `subject` as a class altogether. Now I don't recommend this approach necessarily. I think a true functional programming observer pattern would be some sort of reactive programming style I am not equipped to discuss. But I think this is still a worthwhile pattern to look at for the coding perspective. 

```
def subject():
    callbacks = []
    
    def attach(callback):
        callbacks.append(callback)
    
    def detach(callback):
        callbacks.remove(callback)
    
    def notify(message):
        for callback in callbacks:
            callback(message)
    
    return (attach, detach, notify)

def observer(name):
    def observe(message):
        print(f"{name} received message: {message}")
    
    return observe

attach, detach, notify = subject()
observer1 = observer("DisplayObserver")
observer2 = observer("LogObserver)

attach(observer1)
attach(observer2)
notify("Hello, World!")
# Output:
# DisplayObserver receieved message: Hello, World!
# LogObserver received message: Hello, World!

detach(observer1)
notify("Goodbye, World!")
# Output:
# LogObserver receieved message: Goodbye, World!
```

In this implementation, you have to think differently than OOP style. But some translation helps. We can think of `subject` and `observer` functions as *constructors*. Really, they're closer to factory patterns as we'll see in chapter 4. But the constructor idea fits here. We construct the subject by exposing its 3 functions directly. A closure encapsulates the data (list of observers in this case) within a function scope that those 3 functions have access to. Conceptually it is like "data + behavior" in OOP but flipped on its head. Instead, it is "behavior + data". Likewise, the observers encapsulate their names in this case, providing a uniform way to build observers of this type (the factory part). However, you lose the advantage of a more fully fleshed out observer class object. In any case, the implementation should be designed for the specific use cases it serves and the problems it tries to solve. I hope these 3 examples illustrate the diversity of thought you can have when approaching this solution pattern in your use cases. 
