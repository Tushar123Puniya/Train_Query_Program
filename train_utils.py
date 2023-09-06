import sqlite3
import csv

with open('trains.csv') as f:
   reader = csv.reader(f)
   data = list(reader)
   
def query_on_basis_of_train_number(s,db):
   row=db.execute(f"Select * from train_data where train_number = {s};")
   krow=row.fetchall()
   return krow

def query_on_basis_of_train_name(s,db):
   row=db.execute(f"Select * from train_data where train_name = {s};")
   krow=row.fetchall()
   return krow

def quer_on_basis_of_journey_location(s,db):
   row=db.execute(f"Select * from train_data where Destination_Junction={s};")
   krow=row.fetchall()
   return krow

def query_on_location(s):
   return quer_on_basis_of_journey_location(s,db)

def query_on_train_number(s):
   return query_on_basis_of_train_number(s,db)

def query_on_train_name(s):
   return query_on_basis_of_train_name(s,db)
   
db = sqlite3.connect("mydatabase.db")
db.execute('drop table  train_data')
db.execute('create table train_data (train_number char(50),train_name char(50),Destination_Junction char(50),Boarding_time float,Monday char(1),Tuesday char(1),Wednesday char(1),Thrusday char(1),Friday char(1),Satruday char(1),Sunday char(1));')
for row in data:
   db.execute('INSERT INTO train_data VALUES((?),(?),(?),(?),(?),(?),(?),(?),(?),(?),(?))', row)
   
Days={
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thrusday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
}
 
def function(a):
    # print(a)
    s='Number: '+str(a[0][0])+'\n'+'Name: '+str(a[0][1])+'\n'+'Destination: '+str(a[0][2])+'\n'+'Depature Time: '+str(a[0][3])+'\n'+'Boarding Days: '
    x=4
    for x in range(4,len(a[0])):
        if(a[0][x]=='1'):
            s=s+Days[x-3]+' '
    return s

# print(function(query_on_train_name("'KGP_HWH_LOCAL'")))

def function_(a):
   
   s=""
   for i in range(len(a)):
      t='Number: '+str(a[i][0])+'\n'+'Name: '+str(a[i][1])+'\n'+'Destination: '+str(a[i][2])+'\n'+'Depature Time: '+str(a[i][3])+'\n'+'Boarding Days: '
      x=4
      for x in range(4,len(a[i])):
         if(a[i][x]=='1'):
            t=t+Days[x-3]+' '
      s=s+t+'\n'+'\n'
   return s
 
# print(function_(query_on_location("'HWH'")))