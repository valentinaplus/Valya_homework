from address import Address
from mailing import Mailing


mailing = Mailing(
    to_address="Санкт-Петербург",
    from_address="Гатчина",
    track="TRACK123456789",
    cost="340.50")

to_address = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="30",
    apartment="5")

from_address = Address(
    index="188300",
    city="Гатчина",
    street="Голицыных",
    house="15",
    apartment="1")
