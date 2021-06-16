
from abc import ABC, abstractmethod

class State(ABC):
    _instance = None
    _behavior = ['normal']

    @classmethod
    def get_instance(cls): # singleton
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance 

    def behavior_anormal(self):
        self._behavior.append('anormal')
        self._behavior.pop(0)
    
    def behavior_normal(self):
        self._behavior.append('normal')
        self._behavior.pop(0)

    @classmethod
    def get_state_name(cls):
        return cls.__name__
    
    @abstractmethod
    def execute(self):
        pass

class Up(State):   
    def execute(self):
        if self._behavior[0] == 'normal':
            print("Elevador Subindo")
        else: 
            print("Elevador Subindo Rapidamente")

class Down(State):
    def execute(self):
        if self._behavior[0] == 'normal':
            print("Elevador Descendo")
        else: 
            print("Elevador Descendo Rapidamente")

class Stop(State):
    def execute(self):
        print("Elevador Parado")

class Stuck(State):
    def execute(self):
        print("Elevador Emperrado")

class Maintanance(State):
    def execute(self):
        print("Elevador Em Manutencao")