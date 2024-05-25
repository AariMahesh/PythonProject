import mysql.connector as mc
con=mc.connect(user='root',password='Mahesh@89',host='localhost',database='Bank')

c=con.cursor()
#c.execute('create database Bank')
#c.execute('create table users(name varchar(20), age int)')
#c.execute('insert into users values("akash",20)')
#c.execute('insert into users values("dinesh",23)')
#c.execute('create table deposite_amount(userid int,amount decimal(10,2))')
#c.execute('delete from deposite_amount where userid=202')
c.execute('select * from users')
data=c.fetchall()
print(data)
for i in data:
    print(i)
#con.commit()
