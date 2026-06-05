import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name(self):
        return self.__name_items
    
    @property
    def number(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if len(name) <= 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1
            
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for key in self.__name_items:
            total.append(self.__item_price[key])
        if len(self.__name_items) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for key in self.__name_items:
            if self.__tax_rate[key] == 20:
                twenty_percent_tax.append(key)
        for key in twenty_percent_tax:
            total.append(self.__item_price[key])
        if len(twenty_percent_tax) == 10:
            return sum(total) * 0.9 * 0.2
        else:
            return sum(total) * 0.2
        
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for key in self.__name_items:
            if self.__tax_rate[key] == 10:
                ten_percent_tax.append(key)
        for key in ten_percent_tax:
            total.append(self.__item_price[key])
        if len(ten_percent_tax) == 10:
            return sum(total) * 0.9 * 0.1
        else:
            return sum(total) * 0.1
    
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    def get_telephone_number(self, telephone_number):
        if type(telephone_number) != int:
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return "+7" + str(telephone_number)
        
    def get_date_and_time(self):
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['год:', (lambda x: x.year)(now)],
            ['месяц:', (lambda x: x.month)(now)],
            ['день:', (lambda x: x.day)(now)],
            ['часы:', (lambda x: x.hour)(now)],
            ['минуты:', (lambda x: x.minute)(now)],
            ['секунды:', (lambda x: x.second)(now)],
        ]

        for label, value in date:
            date_and_time.append(f"{label} {value}")

        return date_and_time


test = OnlineSalesRegisterCollector()
test.add_item_to_cheque('кола')
test.add_item_to_cheque('чипсы')
test.add_item_to_cheque('кефир')

print(test.get_name_items)
print(test.get_number_items)

test.check_amount()

test.twenty_percent_tax_calculation()

test.ten_percent_tax_calculation()

test.total_tax()

print(test.get_telephone_number(8006767676)) #простите

print(test.get_date_and_time())