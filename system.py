
from elevator import ElevatorContext
from state import Up, Down, Stop, Stuck, Maintanance
from observer import StuckObserver, MaintenanceObserver, MaintenanceTransitionObserver


class SystemElevator: # facade

    def __init__(self):
        self.elevadorA = ElevatorContext(Stop.get_instance())
        self.elevadorA.attach_state_observer(StuckObserver())
        self.elevadorA.attach_state_observer(MaintenanceObserver())
        self.elevadorA.attach_transition_state_observer(MaintenanceTransitionObserver())

        self.elevadorB = ElevatorContext(Stop.get_instance())
        self.elevadorB.attach_state_observer(StuckObserver())
        self.elevadorB.attach_state_observer(MaintenanceObserver())
        self.elevadorB.attach_transition_state_observer(MaintenanceTransitionObserver())

    def process(self):
        self.elevadorA.operation()
        self.elevadorA.transition_to(Stuck.get_instance())
        self.elevadorA.operation()

        self.elevadorB.operation()
        self.elevadorB.transition_to(Up.get_instance())
        self.elevadorB.operation()

        self.elevadorA.transition_to(Maintanance.get_instance())
        self.elevadorA.operation()

        self.elevadorB.operation()

        self.elevadorA.transition_to(Up.get_instance())
        self.elevadorA.operation()
        self.elevadorB.operation()

if __name__ == '__main__':
    # codigo cliente
    SystemElevator().process()