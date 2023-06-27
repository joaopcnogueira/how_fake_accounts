# How Fake Accounts

Pacote python criado para gerar contas fakes, para o primeiro desafio do bootcamp de engenharia de dados da How. O pacote é a implementação de um provider customizado do [Faker](https://faker.readthedocs.io/en/master/#), conforme sugerido em https://faker.readthedocs.io/en/master/#how-to-create-a-provider.

As contas feitas simulam o cadastro de usuários em um aplicativo e contém as seguintes informações para cada usuário cadastrado:

- nome
- email
- número de telefone
- cpf
- data de nascimento
- endereço
- emprego

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
