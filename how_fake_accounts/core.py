import json
from pathlib import Path
from faker import Faker

fake = Faker('pt_BR')

def generate_accounts(n_accounts=10):
    accounts = []
    for i in range(n_accounts):
        
        accounts.append({
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.cellphone_number(),
            'cpf': fake.cpf(),
            'birth_date': fake.date_of_birth(),
            'address': fake.address(),
            'job': fake.job()
        })
        
    return accounts


def save_accounts(accounts: list, path: str = '.', filename: str = 'accounts.json'):
    filename = Path(path) / 'accounts.json'
    with open(filename, 'w') as file:
        json.dump(accounts, file, default=str)


if __name__ == '__main__':
    accounts = generate_accounts()
    print(accounts)
    save_accounts(accounts)