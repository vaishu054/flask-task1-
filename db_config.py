import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vaishu@1206",
        database="student_db1"
    )
