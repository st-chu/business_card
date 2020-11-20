from faker import Faker
from faker.providers import job


class BusinessCard:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    @property
    def label_length(self):
        return len(self.first_name + ' ' + self.last_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, phone number: {self.phone_number}'

    def __repr__(self):
        return f'BusinessCard(first_name={self.first_name}, last_name={self.last_name}, ' \
               f'phone_number={self.phone_number})'

    def contact(self):
        return print(f'Wybieram numer +48 {self.phone_number} i dzwonię do {self.first_name} {self.last_name}.')


class BaseContact(BusinessCard):
    def __init__(self, first_name, last_name, phone_number, email):
        super().__init__(first_name, last_name, phone_number)
        self.email = email

    def __repr__(self):
        return f'BaseContact(first_name={self.first_name}, last_name={self.last_name}, '\
               f'phone_number={self.phone_number}, email={self.email})'


class BusinessContact(BusinessCard):
    def __init__(self, first_name, last_name, phone_number, email, job, company_name):
        super().__init__(first_name, last_name, phone_number)
        self.email = email
        self.job = job
        self.company_name = company_name

    def __repr__(self):
        return f'BusinessContact(first_name={self.first_name}, last_name={self.last_name}, '\
               f'phone_number={self.phone_number}, email={self.email}, job={self.job}, '\
               f'company_name={self.company_name})'


def create_contact(type_of_card, quantity):
    fake = Faker('pl_PL')
    fake.add_provider(job)
    list_of_card = []
    if type_of_card == BaseContact and type(quantity) == int:
        for card in range(quantity):
            list_of_card.append(BaseContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email()
            ))
        return list_of_card
    elif type_of_card == BusinessContact and type(quantity) == int:
        for card in range(quantity):
            list_of_card.append(BusinessContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                job=fake.job(),
                company_name=fake.company()
            ))
        return list_of_card
    else:
        print("You made a mistake try again")


def show_card_list(card_list):
    list = sorted(card_list, key= lambda last_name: last_name.last_name)
    if type(list[0]) == BaseContact:
        print('*'*72)
        print('|' + 'BASE CONTACT'.center(70) + '|')
        for card in list:
            print('*'*72)
            print(
                f'Osoba kontaktowa: {card.first_name} {card.last_name}\nTelefon kontaktowy: {card.phone_number}'
                f'\nAdres e-mail: {card.email}'
            )
    elif type(list[0]) == BusinessContact:
        print('*' * 72)
        print('|' + 'BUSINESS CONTACT'.center(70) + '|')
        for card in list:
            print('*' * 72)
            print(
                f'Osoba kontaktowa: {card.first_name} {card.last_name}\nTelefon kontaktowy: {card.phone_number}' \
                f'\nAdres e-mail: {card.email}\nNazwa firmy: {card.company_name}\nStanowisko: {card.job}'
            )


basic_list = create_contact(BaseContact, 2)
business_list = create_contact(BusinessContact, 2)
show_card_list(basic_list)
show_card_list(business_list)
