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
    def __init__(self, email, job, company_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
    if type_of_card == 'BaseContact':
        for card in range(quantity):
            list_of_card.append(BaseContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email()
            ))
        return list_of_card
    elif type_of_card == 'BusinessContact':
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


class BaseContact(BusinessCard):
    def __init__(self, phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone_number = phone_number
        self.company_name = 0
        self.position = 0


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
        phone_number=fake.phone_number(),
    )


def creating_business_cards_list(quantity):
    list_1 = []
    for card in range(quantity):
        list_1.append(business_card())
    return list_1


def show_business_cards(list):
    for data in list:
        print('-' * 60)
        print(data)
<<<<<<< HEAD


ja = BaseContact
business_card_list = creating_business_cards_list(10)
business_card_list = sorted(business_card_list, key=lambda name: name.first_name)
business_card_list[3].contact()
print(ja)
=======


basic_list = create_contact('BaseContact', 3)
business_list = create_contact('BusinessContact', 5)


>>>>>>> for_test
