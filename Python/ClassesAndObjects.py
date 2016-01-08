import pygame
#To import do "from NAMEOFFILE import NAMEOFCLASS
#Example class called Cookie
class Cookie:
    def __init__(self, cookie_name, cookie_taste): #Constructor declaration. self is keyword used to indicate that functions will be run on a specific object
        self.name = cookie_name
        self.taste = cookie_taste

    def eat(self):
        print("You ate a " + self.name + " and it was " + self.taste + ".")
    
    def notyetdefinedfunction(self):
        pass #pass used to put nothing here

tasty_cookie = Cookie("tasty cookie", "tasty")
bad_cookie = Cookie("bad cookie", "bleh")

print(bad_cookie.name)
bad_cookie.eat()


#Inheritance. blueberry cookie inherited __init__ and eat functions
class BerryCookie(Cookie):
    def dip(self):
        print("BerryCookie was dipped in berries")

blueberry_cookie = Cookie("blueberry cookie", "blue")
blueberry_cookie.eat()

class CookieGame:

    def main():
        a_berry_cookie = BerryCookie("Gooseberry", "gross")
        a_berry_cookie.dip()

    if __name__ == "__main__": #python automatically sets __name__ to __main__
        main()
