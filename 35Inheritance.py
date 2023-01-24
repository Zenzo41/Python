class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):  #implementing the methods from parent class
    pass  #python doesnt like empty class so we have to add pass inside the class


class Cat(Mammal):
    def annoy(self):
        print("annoy the hooman")


German_Shepherd = Dog()
German_Shepherd.walk()

Cat1 = Cat()
Cat1.annoy()
    
    

    