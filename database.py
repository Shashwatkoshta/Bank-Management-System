import mysql.connector as sql

mydb = sql.connect(
    host ="localhost",
    user="root",
    passwd="Shashwatk44",
    database="bank"
)

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers
            (username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            name varchar(20) NOT NULL,
            age integer NOT NULL,
            city varchar(20) NOT NULL,
            balance INTEGER NOT NULL,
            account_number integer NOT NULL,
            status boolean NOT NULL)            
''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()