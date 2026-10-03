#!C:/Python312/python.exe
import cgi
import cgitb
import os
import mysql.connector
import header
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")

form = cgi.FieldStorage()
d_id = form.getvalue('d_id')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)

query = f"SELECT * FROM doctor WHERE id = {d_id}"
mycursor.execute(query)
myresult = mycursor.fetchone()

print(f'''
        <!-- ============================================================== -->
        <!-- End Topbar header -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- End Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Page wrapper  -->
        <!-- ============================================================== -->
        <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <br><center><h2>Doctor Form</h2></center><br>
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Start Page Content -->
                <!-- ============================================================== -->
                <div class="row">
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
    <div class="col-12">
        <div class="card">
            <div class="card-body wizard-content">
            <form id="stepForm" action="doctor_update.py" method="post" enctype="multipart/form-data">
                <div class="step" id="step1">
                    <center><h4>Doctor Personal Information</h4></center><br>
                    <div class="form-group"> 
                        <label>Sr No.</label><br>
                        <input type="text" class="form-control" name="id" id="id" value="{myresult['id']}" readonly >
                    </div>
                    
                    <section>
                    <div class="col-md-12">
                    <div class="row">
                    <div class="col-md-4">
                        <label for="firstName">First Name</label>
                        <input type="text" class="form-control" id="fname" value="{myresult['fname']}" name="fname" required>
                    </div>
                    <div class="col-md-4">
                        <label for="middleName">Middle Name</label>
                        <input type="text" class="form-control" id="mname" value="{myresult['mname']}" name="mname" required>
                    </div>
                    <div class="col-md-4">
                        <label for="lastName">Last Name</label>
                        <input type="text" class="form-control" id="lname" value="{myresult['lname']}" name="lname" required>
                    </div>
                    </div>
                    </div><br>
                    
                    <div class="col-md-12">
                    <div class="row">
                    <div class="col-md-6">
                        <label for="motherName">Mobile Number</label>
                        <input type="tel" class="form-control" id="mobno" value="{myresult['mobno']}" name="mobno" required>
                    </div>
                    <div class="col-md-6">
                        <label for="email">Email</label>
                        <input type="email" class="form-control" id="email" value="{myresult['email']}" name="email" required>
                    </div>
                    </div>
                    </div><br>
                  

                    <div class="col-md-12">
                    <div class="row">
                    <div class="col-md-4">
                        <label for="birthdate">Date of birth</label>
                        <input type="date" class="form-control" id="dob" value="{myresult['dob']}" name="dob" required>
                    </div>
                    <div class="col-md-4">
                        <label for="control-label">Gender</label><br>
                        <input type="text" class="form-control" id="gender" value="{myresult['gender']}" name="gender" required>
                    </div>
                    <div class="col-md-4">
                        <label for="aadhar">Aadhar No.</label>
                        <input type="text" class="form-control" id="aadhar" value="{myresult['aadhar']}" name="aadhar" required>
                    </div>
                    </div>
                    </div><br>
                    
                <div class="col-md-12">
                <div class="row"> 
                <div class="col-md-4">
                    <label for="pan">Pan No.</label>
                    <input type="text" class="form-control" id="pan" name="pan" value="{myresult['pan']}" required>
                </div>
                <div class="col-md-4">
                    <label for="control-label">Marital Status</label><br>
                    <select class="form-control" name="maritalstatus" id="maritalstatus" value="{myresult['maritalstatus']}" required>
                        <option value="">Please select one … </option>
                        <option value="married">Married</option>
                        <option value="unmarried">Unmarried</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <label for="control-label">Blood Group</label><br>
                    <select class="form-control" name="bloodgroup" id="bloodgroup" value="{myresult['bloodgroup']}" required>
                        <option value="">Please select one … </option>
                        <option value="A+">A+</option>
                        <option value="B+">B+</option>
                        <option value="A-">A-</option>
                        <option value="B-">B-</option>
                        <option value="AB+">AB+</option>
                        <option value="AB-">AB-</option>
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                    </select>
                </div>
                </div>
                </div><br>
                
                <div class="col-md-12">
                    <label for="">Doctor ID size Photo <span class="text-danger">*</span></label>
                     <input type="file" name="doctorphoto" class="form-group form-control" id="doctorphoto" value="{myresult['doctorphoto']}" required>
                </div>
                    
                </div>
                </section>
                <br><br>
                
                
                <section>
                <div class="step" id="step2">
                <center><h4>Doctor Address Information</h4></center><br>
                    <div class="col-md-12">
                    <div class="row">
                     <div class="col-md-6">
                        <label for="country">Country</label>
                        <input type="text" class="form-control" value="India" value="{myresult['country']}" id="country" name="country">
                    </div>
                     <div class="col-md-6">
                        <label for="state">State</label>
                        <input type="text" class="form-control" id="states" value="{myresult['states']}" name="states" required>                    
                    </div>
                    </div>
                    </div><br>
                    
                    <div class="col-md-12">
                    <div class="row">
                    <div class="col-md-4">
                        <label for="city">City</label>
                        <input type="text" class="form-control" id="city" value="{myresult['city']}" name="city" required>
                    </div>
                    <div class="col-md-4">
                        <label for="area">Area / Street</label>
                        <input type="text" class="form-control" id="area" value="{myresult['area']}" name="area" required>
                    </div>
                   <div class="col-md-4">
                        <label for="pincode">Pincode</label>
                        <input type="text" class="form-control" id="pincode" value="{myresult['pincode']}" name="pincode" required>
                    </div>
                    </div>
                    </div><br>
                    
                  </div>
                </section>
                <br><br>
                
                
                <section>
                 <div class="step" id="step3">
                <center><h4>Doctor Educational Information</h4></center><br>
                <div class="col-md-12">
                <div class="row">
                    <div class="col-md-6">
                        <label for="education">Education</label>
                        <input type="text" class="form-control" id="education" value="{myresult['education']}" name="education" required>
                    </div>
                    <div class="col-md-6">
                    <label for="control-label">Specialisation</label><br>
                    <input type="text" class="form-control" id="specialisation" value="{myresult['specialisation']}"name="specialisation"  required>
                     </div>
                </div>
                </div><br><br>
                    
                <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                    <label for="member">member of any other medical associations?</label><br>
                    <input type="text" class="form-control" id="member" value="{myresult['member']}" name="member" required> 
                </div>
                <div class="col-md-6">
                    <label for="institute">Institute Name</label>
                    <input type="text" class="form-control" id="institute" value="{myresult['institute']}" name="institute" required>  
                </div>
                </div>
                </div><br>
                
             </div>
             </section>
             <br><br>
             
             <section>
            <div class="step" id="step4">
                    <center><h4>Doctor Banking Information</h4></center><br>
                <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                        <label for="bankname">Bank Name</label>
                        <input type="text" class="form-control" id="bnk_name" value="{myresult['bnk_name']}" name="bnk_name" required>
                    </div>
                    
                    <div class="col-md-6">
                        <label for="branch">Branch</label>
                        <input type="text" class="form-control" id="branch" value="{myresult['branch']}" name="branch" required>
                    </div>
                    </div>
                    </div><br>
                
                <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                        <label for="accno">Account Number</label>
                        <input type="text" class="form-control" id="acc_no" value="{myresult['acc_no']}" name="acc_no" required>
                    </div>
                    <div class="col-md-6">
                        <label for="ifsccode">IFSC code</label>
                        <input type="text" class="form-control" id="ifsc_code" value="{myresult['ifsc_code']}" name="ifsc_code" required>
                    </div>
                    </div>
                    </div><br>
                   
                    
                    
                    <center><button type="submit" class="btn">Update</button></center>
                </div>
                 </section>
            </form>
        </div>
    </div>

    
    
                <!-- row -->
                <!-- .row -->
                <!-- /.row -->
                <!-- Row -->
                <!-- .row -->
                <!-- /.row -->
                <!-- .row -->
                <!-- /.row -->
                <!-- .row -->
                <!-- .row -->
                <!-- /.row -->
                <!-- row -->
                <!-- Row -->
                <!-- Row -->
                <!-- ============================================================== -->
                <!-- End PAge Content -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Right sidebar -->
                <!-- ============================================================== -->
                <!-- .right-sidebar -->
                <!-- ============================================================== -->
                <!-- End Right sidebar -->
                <!-- ============================================================== -->
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- footer -->
            <!-- ============================================================== -->
           <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
        <!-- ============================================================== -->
        <!-- End footer -->
        <!-- ============================================================== -->
    </div>
    <!-- ============================================================== -->
    <!-- End Page wrapper  -->
    <!-- ============================================================== -->
</div>
<!-- ============================================================== -->
<!-- End Wrapper -->
<!-- ============================================================== -->
<!-- ============================================================== -->
<!-- customizer Panel -->
<!-- ============================================================== -->
<div class="chat-windows"></div>
<!-- ============================================================== -->
<!-- All Jquery -->
    <!-- ============================================================== -->
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
    <script src="../../dist/js/custom.js"></script>
    <script src="../../assets/libs/jquery-steps/build/jquery.steps.min.js"></script>
    <script src="../../assets/libs/jquery-validation/dist/jquery.validate.min.js"></script>
  <script>
  $(".tab-wizard").steps({{
      headerTag: "h6",
      bodyTag: "section",
      transitionEffect: "fade",
      titleTemplate: '<span class="step">#index#</span> #title#',
      labels: {{
          finish: "Submit"
      }},
      onFinished: function(event, currentIndex) {{
          $("form").submit();
      }}
  }});
</script>
</body>
</html>
 ''')