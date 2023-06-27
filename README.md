# How Fake Accounts

Pacote python criado para gerar contas fakes, para o primeiro desafio do bootcamp de engenharia de dados da How.

## How to install

```bash
pip install how-fake-accounts
```

## How to use

We have mainly two ways to use the package:
- as a package itself, to be imported in python scripts
- as a command line interface

### Package Interface

```python
from how_fake_accounts import fake

# generate 10 random accounts
accounts = fake.generate_accounts(10)
print(accounts)
fake.save_locally(accounts)
```


### CLI Interface

To generate 50 accounts, just type into terminal:

```bash
how_fake --n-accounts 50
```
or
```bash
python -m how_fake --n-accounts 50
```

for help, just type:

```bash
how_fake --help
```
