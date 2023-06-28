import os
import random
from datetime import datetime
from how_fake_accounts import fake

n_accounts = random.randint(10, 500)
accounts = fake.generate_accounts(n_accounts)

filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '-accounts.json'
fake.save_into_s3(
    accounts,
    bucket='008413171063-landing-zone',
    key='desafio-01/fake-accounts/' + filename,
    aws_access_key_id=os.getenv('AWS_ID'),
    aws_secret_access_key=os.getenv('AWS_KEY')
)
