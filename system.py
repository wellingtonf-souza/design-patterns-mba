
from elevator import Elevator
from state import Up, Down, Stop, Stuck, Maintenance
from observer import StuckObserver, MaintenanceObserver, MaintenanceTransitionObserver


class System: # facade

    def __init__(self):
        self.elevadorA = Elevator(Stop.get_instance())
        self.elevadorA.attachStateObserver(StuckObserver())
        self.elevadorA.attachStateObserver(MaintenanceObserver())
        self.elevadorA.attachTransitionStateObserver(MaintenanceTransitionObserver())

        self.elevadorB = Elevator(Stop.get_instance())
        self.elevadorB.attachStateObserver(StuckObserver())
        self.elevadorB.attachStateObserver(MaintenanceObserver())
        self.elevadorB.attachTransitionStateObserver(MaintenanceTransitionObserver())

    def process(self):
        self.elevadorA.operation()
        self.elevadorA.transition_to(Stuck.get_instance())
        self.elevadorA.operation()

        self.elevadorB.operation()
        self.elevadorB.transition_to(Up.get_instance())
        self.elevadorB.operation()

        self.elevadorA.transition_to(Maintenance.get_instance())
        self.elevadorA.operation()

        self.elevadorB.operation()

        self.elevadorA.transition_to(Up.get_instance())
        self.elevadorA.operation()
        self.elevadorB.operation()

if __name__ == '__main__':
    # codigo cliente
    System().process()