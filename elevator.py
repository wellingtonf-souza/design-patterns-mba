
from abc import ABC, abstractmethod
from typing import List
from state import State
from observer import StateObserver, TransitionStateObserver

class ElevatorContext:

    def __init__(self, state: State):
        self._state = state
        self._observersState: List[StateObserver] = []
        self._observersTransition: List[TransitionStateObserver] = []

    def transition_to(self, state: State):
        self.verify_transition_state_observer(self._state, state)
        self._state = state

    def operation(self):
        self._state.execute()
        self.verify_state_observer()
    
    def attach_state_observer(self, observer: StateObserver):
        self._observersState.append(observer)

    def attach_transition_state_observer(self, observer: TransitionStateObserver):
        self._observersTransition.append(observer)

    def verify_state_observer(self):
        for obs in self._observersState:
            obs.check_stuck(self._state)
            obs.check_maintenance(self._state)

    def verify_transition_state_observer(self, old: State, new: State):
        for obs in self._observersTransition:
            obs.check_transition(old, new)