from smartphone import Smartphone

catalog = [
    Smartphone("apple", "iphon 14", "+79312371035"),
    Smartphone("samsung", "galaxy", "+79215012345"),
    Smartphone("sony", "5", "+7951876543"),
    Smartphone("xiaomi", "note", "+7999999999"),
    Smartphone("xiaomi", "redmi", "+79361322467")
]

for smartphone in catalog(5):
    brand = input("Марка телефона: ")
    model = input("Модель телефона: ")
    phone_number = input("абоненский номер: ")

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.mode}{smartphone.phone_number}")
