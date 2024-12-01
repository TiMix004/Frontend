import mysql.connector
import time

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "#MsQ_2471-InT",
  database = "ttmdb"
)

def add_User(first_name: str, last_name: str, username: str, email: str, password: str, date_of_birth: str):

    user = {
        "first_name": first_name, #varchar(20)
        "last_name": last_name, #varchar(30)
        "username": username, #int
        "email": email, #char
        "password": password, #char
        "date_of_birth": date_of_birth, #date
    }   

    print(f'Your Database: {mydb}')

    mycursor = mydb.cursor()

    sql = ('INSERT INTO users (firstname, lastname, username, email, password, birthdate, creationdate) VALUES (%s, %s, %s, %s, %s, %s, %s)')
    val = (user["first_name"], user["last_name"], user["username"], user["email"], user["password"], user["date_of_birth"], time.strftime('%Y-%m-%d'))

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    return f"User {user["first_name"]}, {user["last_name"]}, {user["username"]}, {user["email"]}, {user["password"]}, {user["date_of_birth"]} was added at {time.strftime('%Y-%m-%d')}"

#def main(name: str):
#    return name