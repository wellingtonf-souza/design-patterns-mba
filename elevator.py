
from abc import ABC, abstractmethod
from typing import List
from state import State
from observer import StateObserver, TransitionStateObserver

class Elevator:

    def __init__(self, state: State):
        self._state = state
        self._observersState: List[StateObserver] = []
        self._observersTransition: List[TransitionStateObserver] = []

    def transition_to(self, state: State):
        self.verifyTransitionStateObserver(self._state, state)
        self._state = state

    def operation(self):
        self._state.execute()
        self.verifyStateObserver()
    
    def attachStateObserver(self, observer: StateObserver):
        self._observersState.append(observer)

    def attachTransitionStateObserver(self, observer: TransitionStateObserver):
        self._observersTransition.append(observer)

    def verifyStateObserver(self):
        for obs in self._observersState:
            obs.check_stuck(self._state)
            obs.check_maintenance(self._state)

    def verifyTransitionStateObserver(self, old: State, new: State):
        for obs in self._observersTransition:
            obs.check_transition(old, new)