from abc import ABC, abstractmethod
from state import State

class StateObserver(ABC):
    @abstractmethod
    def check_stuck(self, subject: State):
        pass
    
    @abstractmethod
    def check_maintenance(self, subject: State):
        pass

class StuckObserver(StateObserver):
    def check_stuck(self, subject: State):
        if subject.get_state_name() == 'Stuck':
            print('Call security and maintenance teams')
    
    def check_maintenance(self, subject: State):
        pass


class MaintenanceObserver(StateObserver):
    def check_stuck(self, subject: State):
        pass

    def check_maintenance(self, subject: State):
        if subject.get_state_name() == 'Maintanance' and subject._behavior[0] == 'normal':
            print('Mudando comportamento dos elevadores para anormal')
            subject.behavior_anormal()


class TransitionStateObserver(ABC):
    @abstractmethod
    def check_transition(self, old: State, new: State):
        pass

class MaintenanceTransitionObserver(TransitionStateObserver):

    def check_transition(self, old: State, new: State):
        if old.get_state_name() == 'Maintanance' and new.get_state_name() != 'Maintanance':
            print('Mudando comportamento dos elevadores para normal')
            new.behavior_normal()