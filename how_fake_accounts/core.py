import os
import json
import logging
import pandas as pd
from pathlib import Path
from datetime import datetime

import boto3
from io import StringIO
from botocore.exceptions import ClientError

from faker import Faker
from faker.providers import BaseProvider


fake = Faker('pt_BR')

class GenerateAccountsProvider(BaseProvider):
    def generate_accounts(self, n_accounts=10) -> pd.DataFrame:
        """Generate a list of fake accounts"""
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
        return pd.DataFrame(accounts)
            

fake.add_provider(GenerateAccountsProvider)
