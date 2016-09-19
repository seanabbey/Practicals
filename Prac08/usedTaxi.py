from Prac08.taxi import SilverServiceTaxi


def main():
    prius = SilverServiceTaxi("prius", 100, 2)
    prius.start_fare()
    prius.drive(10)
    print(prius)
    # prius.start_fare()
    # prius.drive(100)
    # print(prius)

main()
