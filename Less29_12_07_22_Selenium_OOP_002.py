# OOP-2

# Инкапсуляция
# Наследование
# Полиморфизм


# Абстракция

# class Laptop:
#     color = 'black'
#     CPU = 'i5'
#     GPU = 'integr'
#
#
#
# class Meat:
#     animal = 'pig'
#     age = 5
#
#
# class Steak:
#     roast = 'bluerare'

'''
[19:56] Буйлук Андрей
Задание 1 Реализуйте класс «Человек».
Необходимо хранить в полях класса:
ФИО, дату рождения, контактный телефон, город, страну, домашний адрес.
Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса.
'''

#
# class Human:
#     surname = 'Default'
#     lastname = 'Default'
#     second_name = 'Default'
#     birth_date = '01.01.1970'
#     phone = '+380123456789'
#     city = 'Odessa'
#     country = 'Ukraine'
#
#     def __init__(self, surname, lastname, phone):
#         self.surname = surname
#         self.lastname = lastname
#         self.phone = phone
#
#     def __str__(self):
#         return f'ФИО {self.surname} {self.lastname}'
#
#     def show_phone(self):
#         print(self.phone)
#
#     def change_phone(self, new_phone):
#         self.phone = new_phone
#
#     def show_city(self):
#         print(self.city)
#
#     def change_city(self, new_city):
#         self.city = new_city
#
#     def show_country(self):
#         print(self.country)
#
#     def change_country(self, new_country):
#         self.country = new_country
#
#
# gordon = Human('Freeman', 'Gordon', '+380123334577')
# print(gordon)
# gordon.show_city()
# gordon.show_country()
# gordon.change_city('City217')
# gordon.show_city()
#
# sten = Human('Kozlov', 'Sema', '+380112223345')
# print(sten)

'''
[20:14] Буйлук Андрей
Задание 2 
Создайте класс «Город». 
Необходимо хранить в полях класса: 
название города, название региона, 
название страны, количество жителей в городе, 
почтовый индекс города, телефонный код города. 
Реализуйте методы класса для ввода данных, вывода данных, 
реализуйте доступ к отдельным полям через методы класса.
'''
#
#
# class City:
#     city_name = 'Empty'
#     city_region = 'somewhere'
#     city_country = 'Ukraine'
#     city_number_of_inhabitants = 1000000
#     city_postal_code = 67500
#     city_telephone_code = '+80482'
#
#     def __init__(self, city_name, city_country, city_postal_code):
#         self.city_name = city_name
#         self.city_country = city_country
#         self.city_postal_code = city_postal_code
#
#     def __str__(self):
#         return f'Ваш город {self.city_name} {self.city_country} {self.city_postal_code}'
#
#     def show_region(self):
#         print(self.city_region)
#
#     def change_region(self, new_region):
#         self.city_region = new_region
#
#     def show_number_of_inhabitants(self):
#         print(self.city_number_of_inhabitants)
#
#     def change_number_of_inhabitants(self, new_number_of_inhabitants):
#         self.city_number_of_inhabitants = new_number_of_inhabitants
#
#     def show_telephone_code(self):
#         print(self.city_telephone_code)
#
#     def change_telephone_code(self, new_telephone_code):
#         self.city_telephone_code = new_telephone_code
#
#
# city123 = City('Odessa', 'Ukraine', 67511)
# print(city123)

'''
[20:36] Буйлук Андрей
Задание 4 
Создайте класс «Дробь». 
Необходимо хранить в полях класса: числитель и знаменатель. 
Реализуйте методы класса для ввода данных, вывода данных, 
реализуйте доступ к отдельным полям через методы класса. 
Также создайте методы класса для выполнения арифметических операций 
(сложение, вычитание, умножение, деление, и т.д.).
'''


class Fraction:
    numerator = '12345'
    denominator = '6789'

    def __init__(self, fraction):
        numerator, denominator = fraction.split('/')
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def add(self, other_fraction):
        other_num, other_de = other_fraction.split('/')
        other_num = int(other_num)
        other_de = int(other_de)
        if self.denominator == other_de:
            self.numerator = self.numerator + other_num


platform1 = Fraction('3/4')
print(platform1)

platform1.add('5/4')
print(platform1)

# def show_region(self):
#     print(self.city_region)
#
# def change_region(self, new_region):
#     self.city_region = new_region

