from power.modules.emobility.models import Battery, Vehicle


def test_battery():
    battery = Battery(capacity=20, soc=1.0)

    battery.discharge(10)
    assert battery.soc == 0.5

    battery.discharge(20)
    assert battery.soc == 0.0

    battery.charge(10)
    assert battery.soc == 0.5

    battery.charge(20)
    assert battery.soc == 1.0


def test_vehicle():
    vehicle = Vehicle(consumption=20, battery=Battery(20))

    vehicle.drive(100)
    assert vehicle.battery.soc == 0.0
