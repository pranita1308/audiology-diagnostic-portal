#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")

form = cgi.FieldStorage()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)


mycursor = mydb.cursor(dictionary=True)

query = """
SELECT *
FROM doctor
"""



mycursor.execute(query)
myresult = mycursor.fetchall()


tr_html = ''
for x in myresult:
    tr_html += f'''
        <tr>
            <td>
                <a href="doctor_edit.py ?d_id={x['id']}"><button class="btn btn-success"><i class="fas fa-edit"></i></button></a><br><br>
                <a href="doctor_delete.py ?d_id={x['id']}"><button class="btn btn-danger"><i class="fas fa-trash"></i></button></a>
            </td>
            <td>{x['id']}</td>
            <td>{x['fname']}</td>
            <td>{x['mname']}</td>
            <td>{x['lname']}</td>
            <td>{x['mobno']}</td>
            <td>{x['email']}</td>
            <td>{x['dob']}</td>
            <td>{x['gender']}</td>
            <td>{x['aadhar']}</td>
            <td>{x['pan']}</td>
            <td>{x['maritalstatus']}</td>
            <td>{x['bloodgroup']}</td>
            <td><center><img src="{x['doctorphoto']}" style="height:100px; width:100px;"></center></td>
            <td>{x['country']}</td>
            <td>{x['states']}</td>
            <td>{x['city']}</td>
            <td>{x['area']}</td>
            <td>{x['pincode']}</td>
            <td>{x['education']}</td>
            <td>{x['specialisation']}</td>
            <td>{x['member']}</td>
            <td>{x['institute']}</td>
            <td>{x['bnk_name']}</td>
            <td>{x['branch']}</td>
            <td>{x['acc_no']}</td>
            <td>{x['ifsc_code']}</td>
        </tr>
    '''

# Pagination controls

# Search form and table display
print(f'''
<div class="page-wrapper">
<div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Admin's Panel</h4>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                                <ol class="breadcrumb">
                                    <li class="breadcrumb-item"><a href="dashboard.py">Home</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">Doctor's List</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                    <div class="col-7 align-self-center">   
                    </div>
                </div>
            </div>
<div class="container-fluid">     
 <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <center><h2 class="card-title">Doctor's Data</h2></center> 
                                <div class="table-responsive">
                                    <table id="multi_control" class="table table-striped table-bordered display" style="width:100%">                                 
                                <thead>
                                      <tr style="background-color:powderblue;">
                                           <th>Action</th>
                                                <th scope="col">Sr. No.</th>
                                                <th scope="col">First Name</th>
                                                <th scope="col">Middle Name</th>
                                                <th scope="col">Last Name</th>
                                                <th scope="col">Mobile No.</th>
                                                <th scope="col">Email</th>
                                                <th scope="col">Birth Date</th>   
                                                <th scope="col">Gender</th>
                                                <th scope="col">Aadhar No.</th>
                                                <th scope="col">Pan No</th>
                                                <th scope="col">Marital Status</th>
                                                <th scope="col">Blood Group</th>
                                                <th scope="col">Doctor Photo</th>
                                                <th scope="col">Country</th>
                                                <th scope="col">State</th>
                                                <th scope="col">City</th>
                                                <th scope="col">Area</th>
                                                <th scope="col">Pincode</th>
                                                <th scope="col">Education</th>
                                                <th scope="col">Specialisation</th>
                                                <th scope="col">Member</th>
                                                <th scope="col">Institute</th>
                                                <th scope="col">Bank Name</th>
                                                <th scope="col">Bank Branch</th>
                                                <th scope="col">Account No.</th>
                                                <th scope="col">IFSC Code</th>
                                        </tr>
                                </thead>
                                <tbody>
                                    {tr_html}
                                </tbody>
                                <div style="text-align:center;">
                        </div>
                            </table>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
</div>

<script src="../../assets/libs/jquery/dist/jquery.min.js"></script>
    <!-- Bootstrap tether Core JavaScript -->
    <script src="../../assets/libs/popper.js/dist/umd/popper.min.js"></script>
    <script src="../../assets/libs/bootstrap/dist/js/bootstrap.min.js"></script>
    <!-- apps -->
    <script src="../../dist/js/app.min.js"></script>
    <script src="../../dist/js/app.init.js"></script>
    <script src="../../dist/js/app-style-switcher.js"></script>
    <!-- slimscrollbar scrollbar JavaScript -->
    <script src="../../assets/libs/perfect-scrollbar/dist/perfect-scrollbar.jquery.min.js"></script>
    <script src="../../assets/extra-libs/sparkline/sparkline.js"></script>
    <!--Wave Effects -->
    <script src="../../dist/js/waves.js"></script>
    <!--Menu sidebar -->
    <script src="../../dist/js/sidebarmenu.js"></script>
    <!--Custom JavaScript -->
    <script src="../../dist/js/custom.min.js"></script>
    <!--This page plugins -->
    <script src="../../assets/extra-libs/DataTables/datatables.min.js"></script>
    <!-- start - This is for export functionality only -->
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/dataTables.buttons.min.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.flash.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/pdfmake.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/vfs_fonts.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.html5.min.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.print.min.js"></script>
    <script src="../../dist/js/pages/datatable/datatable-advanced.init.js"></script>
</body>
</html>
''')
