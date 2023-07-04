import pytz
import random
import awswrangler as wr
from datetime import datetime
from how_fake_accounts import fake

n_accounts = random.randint(50, 500)
accounts = fake.generate_accounts(n_accounts)

sao_paulo_timezone = pytz.timezone('America/Sao_Paulo')
partition_folder = "extracted_at=" + datetime.now(sao_paulo_timezone).strftime('%Y-%m-%dT%H:00:00')
filename = 'accounts.parquet'

wr.s3.to_parquet(
    df=accounts, 
    path='s3://008413171063-landing-zone/desafio-01/fake-accounts/' + partition_folder + '/' + filename
)
