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
        print(f'Wybieram numer +48 {self.phone_number} i dzwonię do {self.first_name} {self.last_name}.')


class BaseContact(BusinessCard):
    def __init__(self, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email


class BusinessContact(BusinessCard):
    def __init__(self, email, job, company_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.job = job
        self.company_name = company_name


def business_card():
    fake = Faker('pl_PL')
    fake.add_provider(job)
    return BusinessCard(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        phone_number=fake.phone_number(),
    )


def creating_business_cards_list(quantity):
    list_1 = []
    for card in range(quantity):
        list_1.append(business_card())
    return list_1


def show_business_card(card):
    print(f'Imię: {card.first_name}\nNazwisko: {card.last_name}')
    print(f'Firma: {card.company_name}\nStanowisko: {card.position}\ne-mail: {card.e_mail}')


def show_business_cards(list):
    for data in list:
        print('-' * 60)
        print(data)


ja = BaseContact('marrek', 'starzyk', 883397333)
#business_card_list = sorted(business_card_list, key=lambda name: name.first_name)
#business_card_list[3].contact()
print(ja.label_length)
