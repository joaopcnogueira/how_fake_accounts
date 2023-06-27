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

Currently, every hour an ingestion pipeline at [.github/workflows/ingest_pipeline.yaml](.github/workflows/ingest_pipeline.yaml) is triggered. This pipeline takes in the created accounts for the past hour and ingest them into an S3 bucket. 

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
print(accounts)

filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '-accounts.json'
fake.save_into_s3(
    accounts,
    bucket='missy-aulas-how',
    key='bronze/desafio-01/' + filename,
    aws_access_key_id=os.getenv('AWS_ID'),
    aws_secret_access_key=os.getenv('AWS_KEY')
)
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
