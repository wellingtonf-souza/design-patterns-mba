
from abc import ABC, abstractmethod
from typing import List
from observer import StateObserver

class State(ABC):
    _instance = None
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance 
    @abstractmethod
    def execute(self):
        pass

class Elevator:
    
    _state = None
    _observers: List[StateObserver] = []

    def __init__(self, state: State):
        self.transition_to(state)

    def transition_to(self, state: State):
        self._state = state

    def operation(self):
        self._state.execute()
        self.verify()

    def get_state_name(self):
        return type(self._state).__name__
    
    def attach(self, observer: StateObserver):
        self._observers.append(observer)

    def verify(self):
        for obs in self._observers:
            obs.call_security_team(self)

class Up(State):   
    def execute(self):
        print("Elevador Subindo")

class Down(State):
    def execute(self):
        print("Elevador Descendo")

class Stop(State):
    def execute(self):
        print("Elevador Parado")

class Stuck(State):
    def execute(self):
        print("Elevador Emperrado")

class Maintenance(State):
    def execute(self):
        print("Elevador Em Manutencao")