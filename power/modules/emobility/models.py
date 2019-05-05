from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class Battery:
    capacity: float
    soc: float = 1.0

    @property
    def dod(self) -> float:
        return 1.0 - self.soc

    @property
    def needed(self) -> float:
        return self.capacity * self.dod


@dataclass(frozen=True)
class Driver:
    arrival: time
    distance: float


@dataclass(frozen=True)
class Vehicle:
    consumption: float
    battery: Battery
    driver: Driver

     


@dataclass(frozen=True)
class ChargingStation:
    power: float

    def charging_time(self, battery: Battery) -> time:
        return time(minute=int(battery.needed / self.power * 60))

    def charge(self, battery: Battery, time: time):
        pass
