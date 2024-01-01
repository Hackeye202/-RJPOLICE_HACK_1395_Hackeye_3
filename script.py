import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'localhost\\SQLEXPRESS'
DATABASE_NAME = 'hackathon'

connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust_Connection=yes;
"""

conn = pyodbc.connect(connection_string)
print(conn)

cursor = conn.cursor()

testdict = {'date': '2023-12-31', 'time': '19:54:17', 'camera_status': 'Inactive', 'location': 'Street A', 'detection_count': 155, 'violence_detected': True}

'2023-12-31','19:54:17','Inactive','Street A',155,True

columns = ",".join(testdict.keys())
values = ",".join('?' for _ in testdict.values())

stmt = f"INSERT INTO crime ({columns}) VALUES ({values})"
stmt = stmt + ';'
print(stmt)

#cursor.execute(stmt, list(testdict.values()))
cursor.execute(stmt, ('2023-12-31','19:54:17','Inactive','Street A',155,True))
conn.commit()

cursor.close()
conn.close()
