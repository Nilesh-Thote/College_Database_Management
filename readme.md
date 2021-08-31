# College_Database_Management_System
This is built using Python3 and sqlite.
you can use any database 

##To run this program just import any database you want and import it in program and make a connection with database file and just run it.

``` python
import sqlite3
## conn object we are creating by using connect method of sqlite3 to connect to our database file
conn = sqlite3.connect('College_database.db') ##college_database.db is file name you can use your file path location there to access that file.
## but it should be a database file.
cursor = conn.cursor() ##cursor is a method which acts like a cursor in your file that will enable your to perfome CRUD operation.
```

## Admin username and password are already fixed in the program i.e username=admin and password=12345
you can change if you want other user name and password
```python
def Admin():
  """We are checking whether Admin creadentials are correct or not """
  username=input("Enter Your Username: ")
  password=input("Enter Your Password: ")
  if username=="admin" and password=="12345":
    Admin_controls()
  else:
    print("Credentials doesn't matched.")
```

In this program there is Admin, Teacher and Students each have their own rights to access database.

## Admin can Retrieve,Modify and Delete any record in database.

## Teacher can modify,insert,register detail

## student can insert,modify,register his detail

## Admin can perform all this function.

```python
def Admin_controls():
  """This function contains action which can be performed by Admin.
     In this funtion we are going to ask User which Action you want to perform. 
     It's an continuous loop until user enter "5" to Log Out.
     Admin can Register new Student or Teacher or can Delete Existing Student or Teacher."""
  while True:
    print("\n\t\t\t\t\t Welcome Admin")
    print("Enter \"1\" to Register Student detail  ")
    print("Enter \"2\" to Register Teacher detail  ")
    print("Enter \"3\" to Delete Student detail  ")
    print("Enter \"4\" to Delete Teacher detail  ")
    print("Enter \"5\" to Log Out  ")
```

## Student can perform all this function.
```python
def student():
  while True:
    print("Enter \"1\" if you are an existing student")
    print("Enter \"2\" if you are an new student")
    print("Enter \"3\" to exit from Student")
    answer=input("Enter your option: ")
```
## if he is an existing student he can login using username and password which has to be in database if not then it will print 'Credential didn't match'.

## if 'Credential matched', then he will be logged in as student then he can change his username, email and password.

## if he is new student he will be ased for username and password that will get commit in database

## Teacher can perform similar function as students.
