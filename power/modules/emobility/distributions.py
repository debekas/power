from power.modules.emobility.models import (
    ChargingStation,
    Driver,
    Vehicle,
    Battery,
)

from typing import Callable, List, Dict, Generic, TypeVar
from dataclasses import dataclass
import random
from datetime import time

T = TypeVar("T")
Action = Callable[[], Generic[T]]


def battery(capacity: Action[float]) -> Action[Battery]:
    return lambda: Battery(capacity=capacity())


def driver(arrival: Action[time], distance: Action[float]) -> Action[Driver]:
    return lambda: Driver(arrival=arrival(), distance=distance())


def station(power: Action[float]) -> Action[ChargingStation]:
    return lambda: ChargingStation(power=power())


def vehicle(
    consumption: Action[float],
    battery: Action[Battery],
    driver: Action[Driver],
) -> Action[Vehicle]:
    return lambda: Vehicle(
        consumption=consumption(), battery=battery(), driver=driver()
    )


def generate(
    station: Action[ChargingStation],
    person: Action[Driver],
    vehicle: Action[Vehicle],
):
    pass
