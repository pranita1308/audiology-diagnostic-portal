#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")
form = cgi.FieldStorage()

# Retrieve form data and check for None values
def get_value(field):
    return form.getvalue(field) if form.getvalue(field) else ''

department = get_value('department')
doctor = get_value('doctor')
date = get_value('date')
time = get_value('time')
fullname = get_value('fullname')
phone = get_value('phone')
message = get_value('message')



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor()

query = """INSERT INTO onlineappointment(department, doctor, date , time , fullname ,phone , message) VALUES (%s, %s, %s, %s, %s , %s, %s)"""

values = (department , doctor , date , time , fullname , phone , message)

mycursor.execute(query, values)
mydb.commit()

print('''
<script>
    alert("Appoinment Booked Successfully We will Contact you Soon.!!");
    location.href="confirmation.py";
</script>
''')
