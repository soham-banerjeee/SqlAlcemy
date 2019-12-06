from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import Create, Populate
from datetime import datetime

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)

print("=========Customers=========")

result = session.query(Create.Customer).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)
print("===========================")

print("=========Item=========")

result = session.query(Create.Item).all()
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)
print("===========================")

print("=========Orders=========")

result = session.query(Create.Order).all()
for row in result:
   print ("ID: ",row.id," Date Placed:",row.date_placed, " Customer Id:",row.customer_id)
print("===========================")

print("=========SQL Query for Customer=========")
print(session.query(Create.Customer))
print("===========================")

print("=========count()=========")
print(session.query(Create.Customer).count())
print(session.query(Create.Item).count())
print(session.query(Create.Order).count())
print("===========================")

print("=========first()=========")
result = session.query(Create.Customer).first()
print ("Name: ",result.first_name," ",result.last_name, " Address:",result.address, " Email:",result.email)
