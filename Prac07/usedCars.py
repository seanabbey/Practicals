"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Prac07.car import Car


def main():
    bus = Car(180, "bus")
    bus.drive(30)
    limo = Car(100, "limo")
    limo.add_fuel(20)
    limo.drive(115)
    print("fuel =", bus.fuel)
    print("fuel =", limo.fuel)
    print("odo =", bus.odometer)
    print("odo =", limo.odometer)
    print(bus)

    print("{} {}, {}".format(bus.name, bus.fuel, bus.odometer))
    print("{self.name} {self.fuel}, {self.odometer}".format(self=limo))
main()