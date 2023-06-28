import random
import awswrangler as wr
from datetime import datetime
from how_fake_accounts import fake

n_accounts = random.randint(10, 500)
accounts = fake.generate_accounts(n_accounts)

filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '-accounts.parquet'

wr.s3.to_parquet(
    df=accounts, 
    path='s3://008413171063-landing-zone/desafio-01/fake-accounts/' + filename
)
