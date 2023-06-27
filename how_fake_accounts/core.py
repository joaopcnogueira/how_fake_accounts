import os
import json
import logging
from pathlib import Path
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

from faker import Faker
from faker.providers import BaseProvider

fake = Faker('pt_BR')

class GenerateAccountsProvider(BaseProvider):
    def generate_accounts(self, n_accounts=10):
        """Generate a list of fake accounts

        Args:
            n_accounts (int, optional): Number of accounts to generate. Defaults to 10.

        Returns:
            list: List of accounts

        Example:
            >>> fake.generate_accounts(2)
            [
                {
                    'registration_date': '2021-08-31 10:00:00',
                    'name': 'João da Silva',
                    'email': '
                    'phone': '(11) 99999-9999',
                    'cpf': '999.999.999-99',
                    'birth_date': '1990-01-01',
                    'address': 'Rua dos Bobos, 0',
                    'job': 'Programador'
                },
                {
                    'registration_date': '2021-08-31 10:00:00',
                    'name': 'João da Silva',
                    'email': '
                    'phone': '(11) 99999-9999',
                    'cpf': '999.999.999-99',
                    'birth_date': '1990-01-01',
                    'address': 'Rua dos Bobos, 0',
                    'job': 'Programador'
                }
            ]
        """
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
        """Save accounts into a json file locally
        """
        filename = Path(path) / 'accounts.json'
        with open(filename, 'w') as file:
            json.dump(accounts, file, default=str)


    def save_into_s3(self, 
                    accounts, 
                    bucket,
                    key,
                    aws_access_key_id=None,
                    aws_secret_access_key=None
    ): 
        """Save accounts into a json file in S3 bucket"""
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        try:
            s3_client.put_object(
                Body=json.dumps(accounts, default=str),
                Bucket=bucket,
                Key=key
            )
        except ClientError as e:
            logging.error(e)
            return False
        
        return True
            

fake.add_provider(GenerateAccountsProvider)


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    accounts = fake.generate_accounts()
    filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '-accounts.json'

    fake.save_into_s3(
        accounts,
        bucket='missy-aulas-how',
        key='bronze/desafio-01/' + filename,
        aws_access_key_id=os.getenv('AWS_ID'),
        aws_secret_access_key=os.getenv('AWS_KEY')
    )
