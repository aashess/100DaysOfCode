class Person():
    def __init__(self, name):
        self.name=name
    
    def talk(self):
        print(f"Hi this is {self.name}")

person1 = Person("aashish")
person1.talk()

person2 = Person("Anushka")
person2.talk()