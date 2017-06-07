'''Write a python standalone program for: 
2              a. insert some values [eg. employee details]in db table. 
3              b. fetch the same data and print it on standard output. 
4              c. update specific employee info. 
5              d. delete specific employee and all the info. '''

import sqlite3 
conn = sqlite3.connect('emp12.db') 
print "Opened database successfully"; 
# prepare a cursor object using cursor() method 
cursor = conn.cursor()


 
# Create table as per requirement 
sql = """CREATE TABLE EMP ( 
         FIRST_NAME  CHAR(20) NOT NULL, 
         LAST_NAME  CHAR(20), 
         AGE INT,   
         SEX CHAR(1), 
         INCOME FLOAT )""" 
 
 
cursor.execute(sql) 
print "table create successfully" 
# insert value in table 
cursor.execute ("INSERT INTO EMP(FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME) \
     VALUES ('astha', 'jain', 21, 'female', 20000.00 )"); 
print "Records inserted successfully" 
 
 
 #display data here 
cursor.execute ("SELECT FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME from EMP ") 
for row in cursor: 
    print "FIRST_NAME = ", row[0] 
    print "LAST_NAME = ", row[1] 
    print "AGE = ", row[2] 
    print "SEX = ", row[3] 
    print "INCOME= ", row[4],"\n" 
conn.commit() 
print "Operation done successfully" 
 
 
 #update data 
cursor.execute("UPDATE EMP set INCOME=25000 where FIRST_NAME='astha'") 
conn.commit() 
 #display data here after updation 
cursor.execute ("SELECT FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME from EMP ") 
for row in cursor: 
    print "FIRST_NAME = ", row[0] 
    print "LAST_NAME = ", row[1] 
    print "AGE = ", row[2] 
    print "SEX = ", row[3] 
    print "INCOME= ", row[4],"\n" 
conn.commit() 
print "Records updated successfully";

 # insert value in table 
cursor.execute ("INSERT INTO EMP(FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME) \
       VALUES ('tiya', 'soni', 22, 'female', 26000.00 )"); 
print "Records inserted successfully" 
 
 
 # delete 
cursor.execute("DELETE from EMP where LAST_NAME = 'jain'") 
conn.commit() 
 #display data here after updation 
cursor.execute ("SELECT FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME from EMP ") 
for row in cursor: 
   print "FIRST_NAME = ", row[0] 
   print "LAST_NAME = ", row[1] 
   print "AGE = ", row[2] 
   print "SEX = ", row[3] 
   print "INCOME= ", row[4],"\n" 
print "Records distroyed successfully"; 
conn.close()


'''Output 
python third.py
Opened database successfully
table create successfully
Records inserted successfully
FIRST_NAME =  asthaLAST_NAME =  jain
AGE =  21
SEX =  female
INCOME=  20000.0 
Operation done successfully
FIRST_NAME =  astha
LAST_NAME =  jain
AGE =  21SEX =  female
INCOME=  25000.0 
Records updated successfull
yRecords inserted successfully
FIRST_NAME =  aditi 
LAST_NAME =  soni
AGE =  22
SEX =  female
INCOME=  26000.0 
Records distroyed successfully
'''
