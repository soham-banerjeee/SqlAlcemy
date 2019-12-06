from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import DatbaseInitialization, Insert
from datetime import datetime

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)



result = session.query(DatbaseInitialization.Customer).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)




result = session.query(DatbaseInitialization.Item).all()
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)


result = session.query(DatbaseInitialization.Order).all()
for row in result:
   print ("ID: ",row.id," Date Placed:",row.date_placed, " Customer Id:",row.customer_id)



print(session.query(DatbaseInitialization.Customer))



print(session.query(DatbaseInitialization.Customer).count())
print(session.query(DatbaseInitialization.Item).count())
print(session.query(DatbaseInitialization.Order).count())



result = session.query(DatbaseInitialization.Customer).first()
print ("Name: ",result.first_name," ",result.last_name, " Address:",result.address, " Email:",result.email)

result = session.query(DatbaseInitialization.Item).first()
print ("Name: ",result.name," Cost Price:",result.cost_price, " Selling Price:",result.selling_price, " Quantity:",result.quantity)

result = session.query(DatbaseInitialization.Order).first()
print ("ID: ",result.id," Date Placed:",result.date_placed, " Customer Id:",result.customer_id)

result = session.query(DatbaseInitialization.Customer).get(1)
print ("Name: ",result.first_name," ",result.last_name, " Address:",result.address, " Email:",result.email)
result = session.query(DatbaseInitialization.Item).get(1)
print ("Name: ",result.name," Cost Price:",result.cost_price, " Selling Price:",result.selling_price, " Quantity:",result.quantity)
result = session.query(DatbaseInitialization.Order).get(100)
if(result != None): print ("ID: ",result.id," Date Placed:",result.date_placed, " Customer Id:",result.customer_id)
else: print(result)

result = session.query(DatbaseInitialization.Customer).filter(DatbaseInitialization.Customer.first_name == 'John').all()
print("All customers with name starting with John:")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result = session.query(DatbaseInitialization.Customer).filter(DatbaseInitialization.Customer.id <= 5, DatbaseInitialization.Customer.town.like("Nor%")).all()
print("All customers with id less than or equal to 5 and living in Norfolk town:")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("find all customers who either live in Peterbrugh or Norfolk")
result = session.query(DatbaseInitialization.Customer).filter(or_(DatbaseInitialization.Customer.town == 'Peterbrugh',DatbaseInitialization.Customer.town == 'Norfolk')).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("find all customers whose first name is John and live in Norfolk")
result = session.query(DatbaseInitialization.Customer).filter(and_(DatbaseInitialization.Customer.first_name == 'John',DatbaseInitialization.Customer.town == 'Norfolk')).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("find all johns who don't live in Peterbrugh")
result = session.query(DatbaseInitialization.Customer).filter(and_(DatbaseInitialization.Customer.first_name == 'John',not_(DatbaseInitialization.Customer.town == 'Peterbrugh',))).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("")


result = session.query(DatbaseInitialization.Order).filter(DatbaseInitialization.Order.date_placed == None).all()
print("All Orders with Date Shipped as None")
if(result != None):
   for row in result:
      print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)
else: print("NO RESULT")

result = session.query(DatbaseInitialization.Order).filter(DatbaseInitialization.Order.date_placed != None).all()
print("All Orders with Date Shipped Not as None")
if(result != None):
   for row in result:
      print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)
else: print("NO RESULT")


result = session.query(DatbaseInitialization.Customer).filter(DatbaseInitialization.Customer.first_name.in_(['Toby', 'Sarah'])).all()
print("All Customers whose name start with Toby or Sarah:")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result = session.query(DatbaseInitialization.Customer).filter(DatbaseInitialization.Customer.first_name.in_(['Toby', 'Sarah'])).all()
print("All Customers whose name does not start with Toby or Sarah:")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result =  session.query(DatbaseInitialization.Item).filter(DatbaseInitialization.Item.cost_price.between(10, 50)).all()
print("All Items whose cost price is between 10 and 50:")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)

result =  session.query(DatbaseInitialization.Item).filter(DatbaseInitialization.Item.cost_price.between(10, 50)).all()
print("All Items whose cost price is not between 10 and 50:")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)

result  = session.query(DatbaseInitialization.Item).filter(DatbaseInitialization.Item.name.like("%r")).all()
print("All Items whose name ends with r:")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)

result  = session.query(DatbaseInitialization.Item).filter(DatbaseInitialization.Item.name.like("w%")).all()
print("All Items whose name starts with w:")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)

result =  session.query(DatbaseInitialization.Customer).limit(2).all()
print("Printing all customers but limiting to 2:")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result =  session.query(DatbaseInitialization.Customer).limit(2).offset(2).all()
print("Printing all customers but limiting to 2 and offsetting to 2:")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result =  session.query(DatbaseInitialization.Item).filter(DatbaseInitialization.Item.name.like("wa%")).order_by(desc(DatbaseInitialization.Item.cost_price)).all()
print("Printing all items that start with wa and then it is sorted by the cost price in descending order:")
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)

result =  session.query(DatbaseInitialization.Customer, DatbaseInitialization.Order.date_placed).join(DatbaseInitialization.Order).all()
print("Join between Customer and Order:")
for row in result:
   print (" Order placed on:",row.date_placed)

result =  session.query(DatbaseInitialization.Customer.first_name, DatbaseInitialization.Order.id).outerjoin(DatbaseInitialization.Order).all()
print("Outer Join between Customer and Order:")
for row in result:
   print (" Order placed by:",row.first_name, " with Order ID:",row.id)

result =  session.query(func.count(DatbaseInitialization.Customer.id)).join(DatbaseInitialization.Order).filter(
   DatbaseInitialization.Customer.first_name == 'John',
   DatbaseInitialization.Customer.last_name == 'Green',
).group_by(DatbaseInitialization.Customer.id).scalar()




result =  session.query(DatbaseInitialization.Customer.town).filter(DatbaseInitialization.Customer.id <=10).distinct().all()


for row in result:
   print (row.town)



s1 = session.query(DatbaseInitialization.Item.id, DatbaseInitialization.Item.name).filter(DatbaseInitialization.Item.name.like("Wa%"))
s2 = session.query(DatbaseInitialization.Item.id, DatbaseInitialization.Item.name).filter(DatbaseInitialization.Item.name.like("%e%"))
result =  s1.union(s2).all()


for row in result:
   print (row)

result = session.query(DatbaseInitialization.Item).filter(
    DatbaseInitialization.Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch')
session.commit()





result = session.query(DatbaseInitialization.Item).filter(DatbaseInitialization.Item.name == 'Monitor').one()
session.delete(result)
session.commit()


print(result.name)




result = session.query(DatbaseInitialization.Order).all()

print("Orders Status:")


def dispatch_order(order_id):

   order = session.query(DatbaseInitialization.Order).get(order_id)

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

print("Orders Status For Order ID 1:")
dispatch_order(1)
print("Orders Status For Order ID 2:")
dispatch_order(2)



