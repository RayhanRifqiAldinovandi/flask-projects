import psycopg2


def db_connection():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='db_blog', #The name of your database must be same as this  
        user='postgres',    #Adjust this to the database owner name in your device
        password='warmachine200' #Adjust this to the password you entered when entering psql or pgAdmin
    )
    return conn