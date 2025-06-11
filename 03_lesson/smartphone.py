class Smartphone:
    def __init__(self, brand, model, phone_nomber):
        self.brand = brand
        self.model = model
        self.phone_nomber = phone_nomber

    def print_brand(self):
        print("Марка телефона:",  self.brand)

    def print_model(self):
        print("Модель телефона:", self.model)

    def prinit_phone_nomber(self):
        print("Абоненеский номер:", self.phone_nomber)
