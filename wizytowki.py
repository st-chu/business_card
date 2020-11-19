from faker import Faker
from faker.providers import job


class BusinessCard:
    def __init__(self, first_name, last_name, company_name, position, e_mail):
        self.first_name = first_name
        self.last_name = last_name
        self. company_name = company_name
        self.position = position
        self.e_mail = e_mail


def business_card():
    fake = Faker('pl_PL')
    fake.add_provider(job)
    return BusinessCard(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        company_name=fake.company(),
        position=fake.job(),
        e_mail=fake.email()
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
        print('-' * 50)
        print(f'{data.first_name} {data.last_name}, email: {data.e_mail}')


business_card_list = creating_business_cards_list(10)
show_business_cards(business_card_list)
show_business_card(business_card_list[2])