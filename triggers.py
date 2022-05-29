from database import Session, db, Accounts, AccountType, Transactions, TransactionType, BankLocations
from sqlalchemy import  DDL, event


'''Triggers'''

db.execute(
    """CREATE TRIGGER validate_account_email
    BEFORE INSERT ON accounts
    BEGIN
    SELECT
        CASE
        WHEN NEW.account_email NOT LIKE '%_@__%.__%' THEN
        RAISE (ABORT,'Invalid email address')
        END;
    END;
    """
)

db.execute(
    """CREATE TRIGGER validate_account_number 
    BEFORE INSERT ON accounts
    BEGIN
    SELECT
        CASE
        WHEN length(NEW.account_number) != 8 THEN
        RAISE (ABORT,'The account number must be exactly 8 digits')
        END;
    END;
    """
)