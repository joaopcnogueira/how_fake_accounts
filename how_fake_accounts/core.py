import json
from pathlib import Path

from faker import Faker
from faker.providers import BaseProvider

fake = Faker('pt_BR')

class GenerateAccountsProvider(BaseProvider):
    def generate_accounts(self, n_accounts=10):
        accounts = []
        for i in range(n_accounts):
            accounts.append({
                'registration_date': str(fake.date_time_between(start_date='-1y', end_date='now')),
                'name': fake.name(),
                'email': fake.email(),
                'phone': fake.cellphone_number(),
                'cpf': fake.cpf(),
                'birth_date': fake.date_of_birth(),
                'address': fake.address(),
                'job': fake.job()
            })
        return accounts

    def save_locally(self, accounts, path='.', filename='accounts.json'):
        filename = Path(path) / 'accounts.json'
        with open(filename, 'w') as file:
            json.dump(accounts, file, default=str)

    def save_into_s3(self, accounts):
        #import boto3
        #s3 = boto3.resource('s3')
        #object = s3.Object(bucket, filename)
        #object.put(Body=json.dumps(accounts, default=str))
        raise NotImplementedError
            

fake.add_provider(GenerateAccountsProvider)

if __name__ == '__main__':
    accounts = fake.generate_accounts()
    print(accounts)
    fake.save_locally(accounts)
