import util

class DiffieHellman:
    def __init__(self, g, p) -> None:
        self.__g = g
        self.__p = p
        self.__private_key = self.__generate_private_key()
        self.public_key = self.__primo()
        
        
    def __generate_private_key(self):
        return util.primo(2, 3333)
    
    def __primo(self):
        return (self.__g**self.__private_key) % self.__p
    
    def generate_shared_key(self, public_key_other):
        return (public_key_other**self.__private_key) % self.__p
        