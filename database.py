from sqlalchemy import  DDL, VARCHAR, Integer, create_engine, event, text
from sqlalchemy import Column,ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

db = create_engine('sqlite:///C:\/sqlite\/banking\/bank.db')
base = declarative_base()

Session = sessionmaker(db)

'''Creating tables in database'''

class AccountType(base):
    __tablename__ = "account_types"
    account_type_id = Column(Integer, primary_key = True)
    account_type_name = Column(VARCHAR(length=64))

class Accounts(base):
    __tablename__ = "accounts"
    account_id = Column(Integer, primary_key = True)
    account_name = Column(VARCHAR(length=64), nullable=False)
    account_surname = Column(VARCHAR(length=64), nullable=False)
    account_number = Column(Integer, unique=True, nullable=False)
    account_email = Column(VARCHAR(length=64), nullable=False)
    balance = Column(Integer, default=0)
    account_type_id = Column(Integer, ForeignKey("account_types.account_type_id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class BankLocations(base):
    __tablename__ = "bank_locations"
    bank_location_id = Column(Integer, primary_key = True)
    city = Column(VARCHAR(length=64), nullable=False)
    bank_address = Column(VARCHAR(length=64), nullable=False)

class TransactionType(base):
    __tablename__ = "transaction_type"
    transaction_type_id = Column(Integer, primary_key = True)
    transaction_name = Column(VARCHAR(length=64), nullable=False)

class Transactions(base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key = True)
    amount = Column(Integer)
    transaction_type_id = Column(Integer, ForeignKey("transaction_type.transaction_type_id"), nullable=False)
    account_id = Column(Integer, ForeignKey("account_types.account_type_id"), nullable=False)
    bank_location_id = Column(Integer, ForeignKey("bank_locations.bank_location_id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

base.metadata.create_all(db)

