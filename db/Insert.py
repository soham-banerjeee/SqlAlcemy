from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import Create
engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)
c1 = Create.Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address = '1662 Kinney Street',
              town = 'Wolfden'
              )