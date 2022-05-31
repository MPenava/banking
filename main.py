from database import Session, db, Accounts, AccountType, Transactions, TransactionType, BankLocations
local_session=Session(bind=db)

''' Inserting data to database

local_session.add(AccountType(account_type_name = 'checking'))
local_session.add(AccountType(account_type_name = 'savings'))

local_session.add(Accounts(account_name = 'Marko', account_surname = 'Penava', account_number = 12345678, account_email = 'marko.penava@fpmoz.sum.ba', account_type_id = 1))
local_session.add(Accounts(account_name = 'Ivo', account_surname = 'Ivić', account_number = 87654321, account_email = 'ivo.ivic@fpmoz.sum.ba', account_type_id = 1))
local_session.add(Accounts(account_name = 'Lovro', account_surname = 'Penava', account_number = 22222222, account_email = 'lovro.penava@fpmoz.sum.ba', account_type_id = 1))
local_session.add(Accounts(account_name = 'Pero', account_surname = 'Perić', account_number = 12312312, account_email = 'ivo.ivic@fpmoz.sum.ba', account_type_id = 1))

local_session.add(TransactionType(transaction_name = 'deposit'))
local_session.add(TransactionType(transaction_name = 'withdraw'))

local_session.add(BankLocations(city = 'Posušje', bank_address = 'Fra Grge Martića 28'))

'''

'''Alternative procedures'''

def deposit(accountNumber, amountTransaction, location):
    if(amountTransaction > 0):
        current_account = local_session.query(Accounts.account_id, Accounts.balance).filter(Accounts.account_number == accountNumber).first()
        if(current_account != ""):
            local_session.add(Transactions(amount = amountTransaction, transaction_type_id = 1, account_id = current_account[0], bank_location_id = location))
            local_session.query(Accounts).filter(Accounts.account_id == current_account[0]).update({'balance' : current_account[1] + amountTransaction})
            return "The transaction was completed successfully!"
        return "The account does not exist!"
    return "The amount must be greater than 0!"

def withdraw(accountNumber, amountTransaction, location):
    if(amountTransaction > 0):
        current_account = local_session.query(Accounts.account_id, Accounts.balance).filter(Accounts.account_number == accountNumber).first()
        if(current_account != "" and current_account[1] > amountTransaction):
            local_session.add(Transactions(amount = amountTransaction, transaction_type_id = 2, account_id = current_account[0], bank_location_id = location))
            local_session.query(Accounts).filter(Accounts.account_id == current_account[0]).update({'balance' : current_account[1] - amountTransaction})
            return "The transaction was completed successfully!"
        return "The account does not exist or you do not have enough money in the account!"
    return "The amount must be greater than 0!"


'''Reading data
accounts = local_session.query(Accounts).all()
for a in accounts:
    print(a.account_name, "-", a.account_surname)
'''

'''Deleting data
local_session.query(Accounts).filter(Accounts.account_id == 4).delete()
'''


# print(deposit(12345678, 313, 1))

local_session.commit()
