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

A arquitetura da solução é a seguinte:
- O pacote `how-fake-accounts` é utilizado para simular a criação de contas aleatórias
- O código localizado em [scripts/ingest_accounts_into_s3.py](scripts/ingest_accounts_into_s3.py) pega os dados de cadastros realizados e faz o upload deles no S3
- O Github Actions é utilizado para schedular um job que consiste em executar o código de ingestão anterior de hora em hora. Isso é feito através do arquivo [.github/workflows/ingest_pipeline.yaml](.github/workflows/ingest_pipeline.yaml). **This pipeline takes in the created accounts for the past hour and ingest them into an S3 bucket**. 

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
import os
from datetime import datetime
from how_fake_accounts import fake

# generate 10 random accounts
accounts = fake.generate_accounts(10)
accounts.head()
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
