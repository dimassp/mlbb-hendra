from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def walk(self):
        pass
    
    @abstractmethod
    def basick_attack(self):
        pass