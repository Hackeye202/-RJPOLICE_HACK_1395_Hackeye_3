import mysql.connector

# Database Details
host = "localhost"
user = "root"
password = "1234"
database = "hackeye"

conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

def insert_into_crime(data_to_insert):
    insert_query = "INSERT INTO crime (date, time, camera_no, camera_name, camera_loc, type_of_crime, detection_count) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, data_to_insert)
    conn.commit()
    cursor.close()
    conn.close()
