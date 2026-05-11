class Animal:
    def make_sound(self):
        print("Some animal sound")
    def move(self):
        print("moves")
        
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
    def move(self):
        print("runs")
        
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
    def move(self):
        print("walks silently")
        
class Cow(Animal):
    def make_sound(self):
        print("Moo!")
    def move(self):
        print("walks slowly")
        
Dog().make_sound()   #→ "Woof! Woof!"
Dog().move()         #→ "runs"
Cat().make_sound()   #→ "Meow!"
Cat().move()         #→ "walks silently"
Cow().make_sound()   #→ "Moo!"
Cow().move()         #→ "walks slowly"
Animal().make_sound()#→ "Some animal sound"
Animal().move()      #→ "moves"
