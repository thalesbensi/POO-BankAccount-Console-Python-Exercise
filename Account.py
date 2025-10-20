class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def realize_transaction(self, account, transaction):
        transaction.execute(account)

    def add_account(self, account):
        self.accounts.append(account)


class PersonalAccount(Client):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf


class Account:
    def __init__(self, balance, account_number, agency, owner, history):
        self._balance = balance
        self._account_number = account_number
        self._agency = "0001"
        self._owner = owner
        self._history = History()

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount
                self._history.append(f"Deposited: {amount}")
            else:
                raise ValueError("Deposit amount must be positive")

        def withdraw(self, amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
                self._history.append(f"Withdrew: {amount}")
            else:
                raise ValueError("Insufficient funds or invalid amount")

        @classmethod
        def new_account(cls, owner, account_number, agency):
            return cls(
                balance=0,
                account_number=account_number,
                agency=agency,
                owner=owner,
                history=[],
            )

        def get_balance(self):
            return self._balance

        def get_history(self):
            return self._history

        def get_account_number(self):
            return self._account_number

        def get_agency(self):
            return self._agency

        def get_owner(self):
            return self._owner


class NormalAccount(Account):
    def __init__(
        self, balance, account_number, agency, owner, history, limit, withdrawn_limit=0
    ):
        super().__init__(balance, account_number, agency, owner, history)
        self.limit = limit
        self.withdrawn_limit = withdrawn_limit
