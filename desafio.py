class Animal():
    def barulho(self):
        pass

class Gato(Animal):
    def barulho(self):
        return "Miau"
    
class Cachorro(Animal):
    def barulho(self):
        return "auu!"

class Barulho:
    def barulho(self,animal:Animal):
        return animal.barulho()

cat =Cachorro ()
barulho = Barulho()

print(barulho.barulho(cat))