class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def print_index(self):
        print("Ирдекс:", self.index)

    def print_city(self):
        print("Город:", self.city)

    def print_street(self):
        print("Улица:", self.street)

    def print_house(self):
        print("Дом:", self.house)

    def print_apartment(self):
        print("Квартира:", self.apartment)
