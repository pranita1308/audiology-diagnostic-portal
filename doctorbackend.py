#!C:/Python312/python.exe
import cgi
import os
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")
form = cgi.FieldStorage()
#basic details
fname = form.getvalue('fname')
mname = form.getvalue('mname')
lname = form.getvalue('lname')
mobno = form.getvalue('mobno')
email = form.getvalue('email')
#personal details
dob = form.getvalue('dob')
gender = form.getvalue('gender')
aadhar = form.getvalue('aadhar')
pan = form.getvalue('pan')
maritalstatus = form.getvalue('maritalstatus')
bloodgroup = form.getvalue('bloodgroup')
fi=form['doctorphoto']
if fi.filename:
    fn = os.path.basename(fi.filename)
    # print(fn)
    ext = os.path.splitext(fi.filename)
    # print(ext)

    uploadimg=f'{fname}'+ext[1]
    open(uploadimg,'wb').write(fi.file.read())
    print('Your Image uploaded successfully')
else:
    print('Your Image is not uploaded')
#address details
country = form.getvalue('country')
states = form.getvalue('states')
city = form.getvalue('city')
area = form.getvalue('area')
pincode = form.getvalue('pincode')
country1 = form.getvalue('country1')
states1 = form.getvalue('states1')
city1 = form.getvalue('city1')
area1 = form.getvalue('area1')
pincode1 = form.getvalue('pincode1')

#educational details
education = form.getvalue('education')
specialisation = form.getvalue('specialisation')
member = form.getvalue('member')
institute = form.getvalue('institute')
educated = form.getvalue('educated')
clinics = form.getvalue('clinics')
workbefore = form.getvalue('workbefore')
surgeries = form.getvalue('surgeries')

#bank details
bnk_name=form.getvalue("bnk_name")
branch=form.getvalue("branch")
acc_no=form.getvalue("acc_no")
ifsc_code=form.getvalue("ifsc_code")

fields = [fname, mname, lname, mobno, email, dob, gender, aadhar, pan,  maritalstatus, bloodgroup, uploadimg, country, states, city, area, pincode, country1, states1, city1, area1, pincode1, education, specialisation, member, institute, educated, clinics, workbefore, surgeries, bnk_name, branch, acc_no, ifsc_code]
for i in range(len(fields)):
    if fields[i] is None:
        fields[i] = ""

conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='hds'
)

cursor = conn.cursor()

try:
    cursor.execute("""INSERT INTO doctor (fname, mname, lname, mobno, email, dob, gender, aadhar, pan, maritalstatus, bloodgroup, doctorphoto, country, states, city, area, pincode, country1, states1, city1, area1, pincode1, education, specialisation, member, institute, educated, clinics, workbefore, surgeries, bnk_name, branch, acc_no, ifsc_code) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                   (fname, mname, lname, mobno, email, dob, gender, aadhar, pan,  maritalstatus, bloodgroup, uploadimg, country, states, city, area, pincode, country1, states1, city1, area1, pincode1, education, specialisation, member, institute, educated, clinics, workbefore, surgeries, bnk_name, branch, acc_no, ifsc_code))
    conn.commit()
    print(f'''
<script>alert("!!! Doctors Register Successfully !!!");
    location.href="doctorlist.py";
</script>''')
except mysql.connector.Error as err:
    print("<html><body>")
    print(f"<h2>Error: {err}</h2>")
    print("</body></html>")
finally:
    cursor.close()
    conn.close()
