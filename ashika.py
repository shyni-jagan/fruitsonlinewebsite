import  sqlite3
conn=sqlite3.connect ('ashika,db');
print("opened detabase created successfully");
conn.execute('''CREATE TABLE USER ROLLNO INT NOT  NULL,NAME TEXT NOT NULL,ADDRESS CHART,
SALARY REAL);''')
print("table created succesfull")
conn.close()
