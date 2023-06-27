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
from how_fake_accounts import generate_accounts, save_accounts

# generate 10 random accounts
accounts = generate_accounts(10)
print(accounts)
save_accounts(accounts)
```


### CLI Interface

To generate 50 accounts, just type into terminal:

```python
how_fake_accounts --n-accounts 50
```
or
```python
python -m how_fake_accounts --n-accounts 50 --save True
```

