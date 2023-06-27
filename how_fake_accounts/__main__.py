import argparse
from how_fake_accounts import fake

def parse_command_line():
    """Parse the command line for input arguments."""
    parser = argparse.ArgumentParser(description='Generate fake accounts.')
    parser.add_argument('-n', '--n-accounts', type=int, default=10)
    parser.add_argument('-p', '--path', type=str, default='.')
    parser.add_argument('-f', '--filename', type=str, default='accounts.json')
    parser.add_argument('-s', '--save', type=bool, default=True)
    parser.add_argument('-v', '--verbose', type=bool, default=False)
    return parser.parse_args()

def main():
    args = parse_command_line()
    accounts = fake.generate_accounts(args.n_accounts)

    if args.save:
        fake.save_locally(accounts, path=args.path, filename=args.filename)
    if args.verbose:
        print(accounts)

if __name__ == '__main__':
    main()
