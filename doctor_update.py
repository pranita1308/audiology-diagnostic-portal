#!C:/Python312/python.exe
import cgi
import os
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
id=form.getvalue('id')
#print(id)

#basic detailsinstitute
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
#educational details
education = form.getvalue('education')
specialisation = form.getvalue('specialisation')
member = form.getvalue('member')
institute = form.getvalue('institute')
#bank details
bnk_name=form.getvalue("bnk_name")
branch=form.getvalue("branch")
acc_no=form.getvalue("acc_no")
ifsc_code=form.getvalue("ifsc_code")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE doctor SET fname = '{fname}', mname = '{mname}', lname = '{lname}', mobno = '{mobno}', email = '{email}', dob = '{dob}', gender = '{gender}', aadhar = '{aadhar}', pan = '{pan}', maritalstatus = '{maritalstatus}', bloodgroup = '{bloodgroup}', doctorphoto = '{uploadimg}', country = '{country}', states = '{states}', city = '{city}', area = '{area}', pincode = {pincode}, education = '{education}', specialisation = '{specialisation}',member = '{member}',institute = '{institute}', bnk_name = '{bnk_name}', branch = '{branch}', acc_no = '{acc_no}', ifsc_code = '{ifsc_code}' WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Doctor Record Updated Successfully !!!");
        location.href="doctorlist.py";
    </script>''')