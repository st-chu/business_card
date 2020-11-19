from faker import Faker
from faker.providers import job


class BusinessCard:
    def __init__(self, first_name, last_name, company_name, position, e_mail):
        self.first_name = first_name
        self.last_name = last_name
        self. company_name = company_name
        self.position = position
        self.e_mail = e_mail

    @property
    def len_first_last_name(self):
        return len(self.first_name + ' ' + self.last_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name} email: {self.e_mail}'

    def __repr__(self):
        return f'BusinessCard(first_name={self.first_name}, last_name={self.last_name}, ' \
               f'company_name={self.company_name}, position={self.position}, e_mail={self.e_mail}) '

    def contact(self):
        print(f'Kontaktuj się z {self.first_name} {self.last_name}, stanowisko: {self.position}, e-mail: {self.e_mail}')


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
        print('-' * 60)
        print(data)


ja = BusinessCard('Marek', 'Starzyk', 'Zinel FM', 'technik', 'stachu.ms9@gmail.com')
business_card_list = creating_business_cards_list(10)
business_card_list = sorted(business_card_list, key=lambda name: name.first_name)
business_card_list[3].contact()
print(business_card_list[3].len_first_last_name)
