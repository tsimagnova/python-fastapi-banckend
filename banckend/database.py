import mysql.connector

db_config = {
    'user': 'admin',
    'password': 'tsimagnova',
    'host': 'devops.c2lacie8da2g.us-east-2.rds.amazonaws.com',
    'database': 'gestion_note',
    'raise_on_warnings': True,
}
try:
    db_connection = mysql.connector.connect(**db_config)
    print("connect to the database mysql")
except mysql.connector.Error as err:
    print(f"Error:{err}")

