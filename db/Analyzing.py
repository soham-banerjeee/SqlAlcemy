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

result = session.query(Create.Item).first()
print ("Name: ",result.name," Cost Price:",result.cost_price, " Selling Price:",result.selling_price, " Quantity:",result.quantity)

result = session.query(Create.Order).first()
print ("ID: ",result.id," Date Placed:",result.date_placed, " Customer Id:",result.customer_id)
print("===========================")

print("=========get()=========")
result = session.query(Create.Customer).get(1)
print ("Name: ",result.first_name," ",result.last_name, " Address:",result.address, " Email:",result.email)
result = session.query(Create.Item).get(1)
print ("Name: ",result.name," Cost Price:",result.cost_price, " Selling Price:",result.selling_price, " Quantity:",result.quantity)
result = session.query(Create.Order).get(100)
if(result != None): print ("ID: ",result.id," Date Placed:",result.date_placed, " Customer Id:",result.customer_id)
else: print(result)
print("===========================")

print("=========filter()=========")
result = session.query(Create.Customer).filter(Create.Customer.first_name == 'John').all()
print("\n~~All customers with name starting with John:~~")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result = session.query(Create.Customer).filter(Create.Customer.id <= 5, Create.Customer.town.like("Nor%")).all()
print("\n~~All customers with id less than or equal to 5 and living in Norfolk town:~~")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("\n~~find all customers who either live in Peterbrugh or Norfolk~~")
result = session.query(Create.Customer).filter(or_(Create.Customer.town == 'Peterbrugh',Create.Customer.town == 'Norfolk')).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("\n~~find all customers whose first name is John and live in Norfolk~~")
result = session.query(Create.Customer).filter(and_(Create.Customer.first_name == 'John',Create.Customer.town == 'Norfolk')).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("\n~~find all johns who don't live in Peterbrugh~~")
result = session.query(Create.Customer).filter(and_(Create.Customer.first_name == 'John',not_(Create.Customer.town == 'Peterbrugh',))).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)
print("===========================")
print("\n")

print("=========filter() with NOT, NULL, IN, BETWEEN=========")
result = session.query(Create.Order).filter(Create.Order.date_placed == None).all()
print("\n~~All Orders with Date Shipped as None:~~")
if(result != None):
   for row in result:
      print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)
else: print("NO RESULT")

result = session.query(Create.Order).filter(Create.Order.date_placed != None).all()
print("\n~~All Orders with Date Shipped Not as None:~~")
if(result != None):
   for row in result:
      print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)
else: print("NO RESULT")


result = session.query(Create.Customer).filter(Create.Customer.first_name.in_(['Toby', 'Sarah'])).all()
print("\n~~All Customers whose name start with Toby or Sarah:~~")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result = session.query(Create.Customer).filter(Create.Customer.first_name.in_(['Toby', 'Sarah'])).all()
print("\n~~All Customers whose name does not start with Toby or Sarah:~~")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result =  session.query(Create.Item).filter(Create.Item.cost_price.between(10, 50)).all()
print("\n~~All Items whose cost price is between 10 and 50:~~")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)

result =  session.query(Create.Item).filter(Create.Item.cost_price.between(10, 50)).all()
print("\n~~All Items whose cost price is not between 10 and 50:~~")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)

result  = session.query(Create.Item).filter(Create.Item.name.like("%r")).all()
print("\n~~All Items whose name ends with r:~~")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)

result  = session.query(Create.Item).filter(Create.Item.name.like("w%")).all()
print("\n~~All Items whose name starts with w:~~")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)
print("===========================")


print("=========limit()=========")
result =  session.query(Create.Customer).limit(2).all()
print("~~Printing all customers but limiting to 2:~~")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)
print("===========================")

print("=========offset()=========")
result =  session.query(Create.Customer).limit(2).offset(2).all()
print("~~Printing all customers but limiting to 2 and offsetting to 2:~~")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)
print("===========================")

print("=========order_by()=========")
result =  session.query(Create.Item).filter(Create.Item.name.like("wa%")).order_by(desc(Create.Item.cost_price)).all()
print("~~Printing all items that start with wa and then it is sorted by the cost price in descending order:~~")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)
print("===========================")

print("\n=========join()=========")
result =  session.query(Create.Customer, Create.Order.date_placed).join(Create.Order).all()
print("~~Join between Customer and Order:~~")
for row in result:
   print (" Order placed on:",row.date_placed)
print("===========================")

print("\n=========outerjoin()=========")
result =  session.query(Create.Customer.first_name, Create.Order.id).outerjoin(Create.Order).all()
print("~~Outer Join between Customer and Order:~~")
for row in result:
   print (" Order placed by:",row.first_name, " with Order ID:",row.id)
print("===========================")


print("\n=========groupby()=========")
result =  session.query(func.count(Create.Customer.id)).join(Create.Order).filter(
   Create.Customer.first_name == 'John',
   Create.Customer.last_name == 'Green',
).group_by(Create.Customer.id).scalar()
print("~~Number of Orders made by John Green:~~")
print(result)
print("===========================")


print("\n=========Dealing with Duplicates=========")
result =  session.query(Create.Customer.town).filter(Create.Customer.id <=10).distinct().all()
print("~~Distinct towns:~~")

for row in result:
   print (row.town)
print("===========================")

print("\n=========Union=========")
s1 = session.query(Create.Item.id, Create.Item.name).filter(Create.Item.name.like("Wa%"))
s2 = session.query(Create.Item.id, Create.Item.name).filter(Create.Item.name.like("%e%"))
result =  s1.union(s2).all()
print("~~Union between items starting with Wa and having a e in between:~~")

for row in result:
   print (row)
print("===========================")

print("\n=========Updating Data=========")
result = session.query(Create.Item).filter(
    Create.Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch')
session.commit()
print("~~Updating  Item starting with W:~~")

print(result)
print("===========================")

print("\n=========Deleting Data=========")
result = session.query(Create.Item).filter(Create.Item.name == 'Monitor').one()
session.delete(result)
session.commit()
print("~~Deleting Item Monitor:~~")

print(result.name)
print("===========================")


print("\n=========Transactions=========")
result = session.query(Create.Order).all()

print("~~Orders Status:~~")


def dispatch_order(order_id):

   order = session.query(Create.Order).get(order_id)

   try:
      if not order:
         raise ValueError("Invalid order id: {}.".format(order_id))
   except ValueError as e:
      print(e)
      return

   try:
      if order.date_shipped:
         print("Order already shipped.")
         return
   except:
      pass

   try:
      for i in order.line_items:
         i.item.quantity = i.item.quantity - i.quantity

      order.date_shipped = datetime.now()
      session.commit()
      print("Transaction completed.")

   except IntegrityError as e:
      print(e)
      print("Rolling back ...")
      session.rollback()
      print("Transaction failed.")

print("~~Orders Status For Order ID 1:~~")
dispatch_order(1)
print("~~Orders Status For Order ID 2:~~")
dispatch_order(2)
print("~~Orders Status For Order ID 3:~~")
dispatch_order(3)
print("~~Orders Status For Order ID 4:~~")
dispatch_order(4)
print("===========================")

