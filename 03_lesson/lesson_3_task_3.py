from address import Address
from mailing import Mailing


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

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    track="TRACK123456789",
    cost=340.50
    )

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
