class Shop:
    def __init__(self, name, address, types_products):
        self.name = name
        self.address = address
        self.types_products = types_products

    def show(self):
        print(f'\n\nМагазин "{self.name}" знаходиться за адресою: {self.address}.\nВ продажі представлені такі товари як:')
        for ind, el in enumerate(self.types_products, start =1):
            print(f'{ind}) {el}')


class Clothes(Shop):
    def __init__(self, name, address, types_products):
        super().__init__(name, address, types_products)
    
    def show(self):
        super().show()
        print(f'\nВ цьому магазині також можна здати власне взуття в чистку.')


class Grocery(Shop):
    def __init__(self, name, address, types_products):
        super().__init__(name, address, types_products)

    def show(self):
        super().show()
        print('\nВ цьому магазині є відділ кулінарії.\nТут можна поїсті готову їжу.')

    
class Technics(Shop):
    def __init__(self, name, address, types_products):
        super().__init__(name, address, types_products)

    def show(self):
        super().show()
        print('\nВ цьому магазині можна зарядити свої гаджети.')
        




ecco = Clothes('ECCO', 'вул. Нижньодніпровська, 17', ['Взуття', 'Засоби для догляду взуття', 'Косметика'])
touch = Technics('TOUCH', 'вул. Титова, 32', ['Техніка Apple', 'Гаджети Xiaomi', 'Ігрові консолі'])
ashan = Grocery('Ашан', 'вул. Нижньодніпровська, 52', ['Продукти', 'Напої', 'Одяг'])


ecco.show()
touch.show()
ashan.show()
