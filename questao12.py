import abc


class DomesticAnimal:

    def __init__(self, name):
        self.name = name
        print("I am a domestic animal and i love my human, {}, and my name is {}".format(self.speak(), self.name))

    def ask_for_food(self):
        print("{}".format(self.speak()))
        DomesticAnimal.ask_for_food(self)

    """vemos que uma vantagem de usar , métodos estáticos, é manter em ordem a funcionalidade de uma 
     função em uma classe visto que a função não chama nada da propria classe """

    @staticmethod
    def need_food():
        print("I am hungry, {}")

    @classmethod
    def why_have_them(cls):
        print("Studies shows that having a domestic partner enhances your life's quality")

    """Abstract methods can be used to organize when you have implemented something or not
    like in this case we will implement the method speak later, when the animal's speak is known"""
    @abc.abstractmethod
    def speak(self):
        return None


class Dogs(DomesticAnimal):
    def speak(self):
        return "woof"

    def show_love(self):
        print(self.speak() + " i am a good boy")


class Cats(DomesticAnimal):
    def speak(self):
        return "meow"

    def break_things_on_purpose(self):
        print(self.speak + " i broke your plate")


class Golden(Dogs):
    def speak_again(self):
        print(self.speak() + ", i have long golden hair")


class Corgi(Dogs):
    def speak_again(self):
        print(self.speak() + ", i am petite and cute")


class Sphynx(Cats):
    def be_mad(self):
        print(self.speak() + " im an alien")


def see_duck_typing():
    rufus = Golden("Rufus")
    spyke = Corgi("Spyke")
    king = Sphynx("King")
    for animal in rufus, spyke, king:
        animal.show_love()


"""Class methods can be used when you need to 'know' something without the need of having an instance of the class"""
DomesticAnimal.why_have_them()
see_duck_typing()
