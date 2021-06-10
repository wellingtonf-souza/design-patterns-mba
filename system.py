
from elevator import Elevator, Up, Down, Stop, Stuck, Maintenance
from observer import StuckObserver

class System: # facade

    def __init__(self):
        self.elevadorA = Elevator(Stop.get_instance())
        self.elevadorB = Elevator(Stop.get_instance())

    def process(self):
        self.elevadorA = Elevator(Up.get_instance())
        self.elevadorA.attach(StuckObserver())
        self.elevadorA.operation()
        self.elevadorA.get_state_name()

        self.elevadorA.transition_to(Stuck.get_instance())
        self.elevadorA.operation()