#importing sqlite3 so that we can use database
import sqlite3
#conn object we are creating by using connect method of sqlite3 to connect to our database file
conn = sqlite3.connect('College_database.db') #college_database.db is file name you can use your file path location there to access that file.
cursor = conn.cursor() #cursor is a method which acts like a cursor in your file that will enable your to perfome CRUD operation.

def Main():
  """This is the Main() funtion that is going to get executed in this whole program. 
     In this funtion we are going to ask User which Action you want to perform. 
     It's an continuous loop until user enter "4" to Quit. 
     If user enter other option thier functions are called. """
  while True:
    print("\n\t\t\t\t\t College Database Management System ")
    print("Enter \"1\" to select Student Login ")
    print("Enter \"2\" to select Teacher Login ")
    print("Enter \"3\" to select Admin Login ")
    print("Enter \"4\" to Quit")
    answer=input("Enter the option: ")
    print()
    try:
      answer=int(answer)
    except:
      print("You can only enter 1/2/3 as an option")
    if answer==1:
      student()
    elif answer==2:
      teacher()
    elif answer==3:
      Admin()
    elif answer==4:
      print("Thank you")
      break
    else:
      print("Wrong Input")


def Admin():
  """We are checking whether Admin creadentials are correct or not """
  username=input("Enter Your Username: ")
  password=input("Enter Your Password: ")
  if username=="admin" and password=="12345":
    Admin_controls()
  else:
    print("Credentials doesn't matched.")


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
    answer=input("Enter your option: ")
    print()
    try:
      answer=int(answer)
    except:
      print("You can only enter 1/2/3/4/5 as an option")
    if answer==1:
      username=input("Enter Student Username: ")
      password=input("Enter Student Password: ")
      email=input("Enter Student Email Address: ")
      cursor.execute('INSERT INTO users (Username,Email,Password,User_Type) VALUES (?,?,?,?)',(username,email,password,"student"))
      conn.commit()
      if cursor.rowcount < 1:
        print("Error occured while commiting to Database")
      else:
        print("Student with "+username+" has been Registered")
    elif answer==2:
      username=input("Enter Teacher Username: ")
      password=input("Enter Teacher Password: ")
      email=input("Enter Teacher Email Address: ")
      cursor.execute('INSERT INTO users (Username,Email,Password,User_Type) VALUES (?,?,?,?)',(username,email,password,"teacher"))
      conn.commit()
      if cursor.rowcount < 1:
        print("Error occured while commiting to Database")
      else:
        print("Teacher with "+username+" has been Registered")
    elif answer==3:
      username=input("Enter Student's Username you want to Delete: ")
      cursor.execute('DELETE FROM Users WHERE Username= ? AND User_Type="student" ',(username,))
      conn.commit()      
      if cursor.rowcount < 1:
        print("User "+username+ " does not exist")
      else:
        print("Student with Username "+username+" has been deleted")
    elif answer==4:
      username=input("Enter Teacher Username you want to Delete: ")
      cursor.execute('DELETE FROM Users WHERE Username=? AND User_Type="teacher"',(username,))
      conn.commit()
      if cursor.rowcount < 1:
        print("User "+username+" does not exist")
      else:
        print("Teacher "+username+" has been deleted")
    elif answer==5:
      print("Logging out as an Admin")
      break
    else:
      print("Wrong Input, Try Again")


def student():
  while True:
    print("Enter \"1\" if you are an existing student")
    print("Enter \"2\" if you are an new student")
    print("Enter \"3\" to exit from Student")
    answer=input("Enter your option: ")
    print()
    try:
      answer=int(answer)
    except:
      print("You can only enter 1/2/3 as an option")
    if answer==1:
      existing_student()
    elif answer==2:
      new_student()
    elif answer==3:
      print("Exiting From Student")
      break
    else:
      print("Wrong Input, Try Again")

def existing_student():
  print("\n\t\t\t\t\t Existing Student")
  exist=False
  username=input("Enter Username: ")
  password=input("Enter Password: ")
  cursor.execute('SELECT Username,Password FROM Users WHERE User_Type=?',('student',))
  db=cursor.fetchall()
  for i in db:
    a,b=i
    if username==a and password==b:
      exist=True
      print("\t\t\t\t\t Welcome "+username)
      student_login(username,password)
  if exist==False:
    print("Credential doesnt matched")

def student_login(username,password):
  while True:
    print("Enter \"1\" if you want to change email address")
    print("Enter \"2\" if you want to change Password address")
    print("Enter \"3\" if you want to Log Out")
    answer=input("Enter your option: ")
    print()
    try:
      answer=int(answer)
    except:
      print("You can only enter 1/2/3 as an option")    
    if answer==1:
      new_email=input("Enter new Email Address: ")
      cursor.execute('UPDATE Users SET Email=? WHERE Username=? AND Password=?',(new_email,username,password))
      conn.commit()
      if cursor.rowcount < 1:
        print("Error Occured while Updating Email Address in Database")
      else:
        print("User "+username+" Email Address is changed as "+new_email)
    elif answer==2:
      new_password=input("Enter new Password Address: ")
      cursor.execute('UPDATE Users SET Password=? WHERE Username=? AND Password=?',(new_password,username,password))
      conn.commit()
      if cursor.rowcount < 1:
        print("Error Occured while Updating Password in Database")
      else:
        print("User "+username+" Password is changed.")
        password=new_password
    elif answer==3:
      print("Logging out as Student")
      break
    else:
      print("Wrong Input, Try Again")

def new_student():
  print("\n\t\t\t\t\t Enter Your Details: ")
  email=input("Enter Email Address: ")  
  username=input("Enter Your Username: ")
  password=input("Enter password: ")
  cursor.execute('INSERT INTO Users(Username,Email,Password,User_Type) VALUES(?,?,?,?)',(username,email,password,'student'))
  conn.commit()
  if cursor.rowcount < 1:
    print("Error Occured while registering details in Database")
  else:
    print("User "+username+" is registered in Database")



def teacher():
  while True:
    print("Enter \"1\" if you are an existing Teacher")
    print("Enter \"2\" if you are an new Teacher")
    print("Enter \"3\" to exit from Teacher")
    answer=input("Enter your option: ")
    print()
    try:
      answer=int(answer)
    except:
      print("You can only enter 1/2/3 as an option")
    if answer==1:
      existing_teacher()
    elif answer==2:
      new_teacher()
    elif answer==3:
      print("Exiting From Teacher")
      break
    else:
      print("Wrong Input, Try Again")

def existing_teacher():
  print("\n\t\t\t\t\t Existing Teacher")
  exist=False
  username=input("Enter Username: ")
  password=input("Enter Password: ")
  cursor.execute('SELECT Username,Password FROM Users WHERE User_Type=?',('teacher',))
  db=cursor.fetchall()
  print(db)
  for i in db:
    a,b=i
    if username==a and password==b:
      exist=True
      print("\n\t\t\t\t\t Welcome "+username)
      teacher_login(username,password)
  if exist==False:
    print("Credential doesnt matched")


def teacher_login(username,password):
  while True:
    print("Enter \"1\" if you want to change email address")
    print("Enter \"2\" if you want to change Password address")
    print("Enter \"3\" if you want to Log Out")
    answer=input("Enter your option: ")
    print()
    try:
      answer=int(answer)
    except:
      print("You can only enter 1/2/3 as an option")    
    if answer==1:
      new_email=input("Enter new Email Address: ")
      cursor.execute('UPDATE Users SET Email=? WHERE Username=? AND Password=?',(new_email,username,password))
      conn.commit()
      if cursor.rowcount < 1:
        print("Error Occured while Updating Email Address in Database")
      else:
        print("User "+username+" Email Address is changed as "+new_email)
    elif answer==2:
      new_password=input("Enter new Email Address: ")
      cursor.execute('UPDATE Users SET Password=? WHERE Username=? AND Password=?',(new_email,username,password))
      conn.commit()
      if cursor.rowcount < 1:
        print("Error Occured while Updating Password in Database")
      else:
        print("User "+username+" Password is changed.")
        password=new_password
    elif answer==3:
      print("Logging out as Student")
      break
    else:
      print("Wrong Input, Try Again")

def new_teacher():
  print("\n\t\t\t\t\t Enter Your Details")
  email=input("Enter Email Address: ")  
  username=input("Enter Your Username: ")
  password=input("Enter password: ")
  cursor.execute('INSERT INTO Users(Username,Email,Password,User_Type) VALUES(?,?,?,?)',(username,email,password,'teacher'))
  conn.commit()
  if cursor.rowcount < 1:
    print("Error Occured while registering details in Database")
  else:
    print("User "+username+" is registered in Database")

Main()


