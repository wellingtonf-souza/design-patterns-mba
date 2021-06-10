
# from elevator import Elevator
from abc import ABC, abstractmethod

class StateObserver(ABC):
    @abstractmethod
    def call_security_team(self, subject):
        pass

class StuckObserver(StateObserver):
    def call_security_team(self, subject):
        if subject.get_state_name() == 'Stuck':
            print('Call security and maintenance teams')

class MaintenanceObserver(StateObserver):
    def call_security_team(self, subject):
        pass