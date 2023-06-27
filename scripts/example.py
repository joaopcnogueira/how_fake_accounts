# pip install how-fake-accounts
from how_fake_accounts import fake

accounts = fake.generate_accounts(10)
print(accounts)
fake.save_locally(accounts)
