class Phone:
    def __init__(self, phone, owner):
        self.phone = phone
        self.owner = owner

    def call(self, x):
        print(f'{self.owner} позвонил, используя "{self.phone}", на телефон "{x.phone}", хозяин которого {x.owner}.')


iphone = Phone('Iphone 11', 'Max')
nokia = Phone('Nokia 6300', 'Viktor')
sony = Phone('Sony 1001', 'Igor')

iphone.call(nokia)
sony.call(iphone)