#!C:/Python312/python.exe
import header
print (header.homehtml)
print('''
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
                                <form action="doctorbackend.py" class="tab-wizard wizard-circle" method="post" enctype="multipart/form-data">
                                    <!-- Step 1 -->
                                    <h6>Doctor PersonalInformation</h6>
                                    <section>
                                       <div class="col-md-12">
                <div class="row">
                <div class="col-md-4">
                    <label for="firstName">First Name</label>
                    <input type="text" class="form-control" id="fname" name="fname" required>
                </div>
                <div class="col-md-4">
                    <label for="middleName">Middle Name</label>
                    <input type="text" class="form-control" id="mname" name="mname" required>
                </div>
                <div class="col-md-4">
                    <label for="lastName">Last Name</label>
                    <input type="text" class="form-control" id="lname" name="lname" required>
                </div>
                </div>
        </div><br>
              
                <div class="col-md-12">
                <div class="row">  
                <div class="col-md-6">
                    <label for="mobileno">Mobile Number</label>
                    <input type="tel" class="form-control" id="mobno" name="mobno" required>
                </div>
                <div class="col-md-6">
                    <label for="email">Email</label>
                    <input type="email" class="form-control" id="email" name="email" required>
                 </div>
                </div>
                </div><br>
                
                <div class="col-md-12">
                <div class="row"> 
                <div class="col-md-4">
                    <label for="birthdate">Date of birth</label>
                    <input type="date" class="form-control" id="dob" name="dob" required>
                </div>
                <div class="col-md-4">
                    <label for="control-label">Gender</label><br>
                    <select class="form-control" name="gender" id="gender" aria-describedby="emailHelp" required>
                        <option value="">Please select one … </option>
                        <option value="female">Female</option>
                        <option value="male">Male</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <label for="aadhar">Aadhar No.</label>
                    <input type="text" class="form-control" id="aadhar" name="aadhar" required>
                </div>
                </div>
                </div><br>
                
                
                <div class="col-md-12">
                <div class="row"> 
                <div class="col-md-4">
                    <label for="pan">Pan No.</label>
                    <input type="text" class="form-control" id="pan" name="pan" required>
                </div>
                <div class="col-md-4">
                    <label for="control-label">Marital Status</label><br>
                    <select class="form-control" name="maritalstatus" id="maritalstatus" aria-describedby="emailHelp" required>
                        <option value="">Please select one … </option>
                        <option value="married">Married</option>
                        <option value="unmarried">Unmarried</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <label for="control-label">Blood Group</label><br>
                    <select class="form-control" name="bloodgroup" id="bloodgroup" aria-describedby="emailHelp" required>
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
                     <input type="file" name="doctorphoto" class="form-group form-control" id="doctorphoto" required>
                </div>
                                    </section>
                                    
                                    <!-- Step 2 -->
                                    <h6>Doctor Address Information</h6>
                                    <section>
                                       <div class="col-md-12">
                <div class="row"> 
               <div class="col-md-6">
                    <label for="country">Country</label>
                    <input type="text" class="form-control" value="India" id="country" name="country" required>
                </div>
                <div class="col-md-6">
                    <label for="state">State</label>
                    <select id="states" name="states" class="form-control" required>
                        <option value="Andhra Pradesh">Andhra Pradesh</option>
                        <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                        <option value="Assam">Assam</option>
                        <option value="Bihar">Bihar</option>
                        <option value="Chhattisgarh">Chhattisgarh</option>
                        <option value="Goa">Goa</option>
                        <option value="Gujarat">Gujarat</option>
                        <option value="Haryana">Haryana</option>
                        <option value="Himachal Pradesh">Himachal Pradesh</option>
                        <option value="Jharkhand">Jharkhand</option>
                        <option value="Karnataka">Karnataka</option>
                        <option value="Kerala">Kerala</option>
                        <option value="Madhya Pradesh">Madhya Pradesh</option>
                        <option value="Maharashtra" selected>Maharashtra</option>
                        <option value="Manipur">Manipur</option>
                        <option value="Meghalaya">Meghalaya</option>
                        <option value="Mizoram">Mizoram</option>
                        <option value="Nagaland">Nagaland</option>
                        <option value="Odisha">Odisha</option>
                        <option value="Punjab">Punjab</option>
                        <option value="Rajasthan">Rajasthan</option>
                        <option value="Sikkim">Sikkim</option>
                        <option value="Tamil Nadu">Tamil Nadu</option>
                        <option value="Telangana">Telangana</option>
                        <option value="Tripura">Tripura</option>
                        <option value="Uttar Pradesh">Uttar Pradesh</option>
                        <option value="Uttarakhand">Uttarakhand</option>
                        <option value="West Bengal">West Bengal</option>
                        <option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
                        <option value="Chandigarh">Chandigarh</option>
                        <option value="Dadra and Nagar Haveli and Daman and Diu">Dadra and Nagar Haveli and Daman and Diu</option>
                        <option value="Lakshadweep">Lakshadweep</option>
                        <option value="Delhi">Delhi</option>
                        <option value="Puducherry">Puducherry</option>
                        <option value="Ladakh">Ladakh</option>
                        <option value="Jammu and Kashmir">Jammu and Kashmir</option>
                    </select>                    
                </div>
                </div>
            </div><br>
            
            <div class="col-md-12">
                <div class="row"> 
                <div class="col-md-4">
                    <label for="city">City</label>
                    <input type="text" class="form-control" id="city" name="city" required>
                </div>
                <div class="col-md-4">
                    <label for="area">Area / Street </label>
                    <input type="text" class="form-control" id="area" name="area" required>
                </div>
                <div class="col-md-4">
                    <label for="build_name">Pincode</label>
                    <input type="text" class="form-control" id="pincode" name="pincode" required>
                </div>
                </div>
                </div><br><br>
                
                <label>Permanent Address: </label><br><br>
                <div class="col-md-12">
                <div class="row"> 
               <div class="col-md-6">
                    <label for="country">Country</label>
                    <input type="text" class="form-control" value="India" id="country1" name="country1" required>
                </div>
                <div class="col-md-6">
                    <label for="state">State</label>
                    <select id="states1" name="states1" class="form-control" required>
                        <option value="Andhra Pradesh">Andhra Pradesh</option>
                        <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                        <option value="Assam">Assam</option>
                        <option value="Bihar">Bihar</option>
                        <option value="Chhattisgarh">Chhattisgarh</option>
                        <option value="Goa">Goa</option>
                        <option value="Gujarat">Gujarat</option>
                        <option value="Haryana">Haryana</option>
                        <option value="Himachal Pradesh">Himachal Pradesh</option>
                        <option value="Jharkhand">Jharkhand</option>
                        <option value="Karnataka">Karnataka</option>
                        <option value="Kerala">Kerala</option>
                        <option value="Madhya Pradesh">Madhya Pradesh</option>
                        <option value="Maharashtra" selected>Maharashtra</option>
                        <option value="Manipur">Manipur</option>
                        <option value="Meghalaya">Meghalaya</option>
                        <option value="Mizoram">Mizoram</option>
                        <option value="Nagaland">Nagaland</option>
                        <option value="Odisha">Odisha</option>
                        <option value="Punjab">Punjab</option>
                        <option value="Rajasthan">Rajasthan</option>
                        <option value="Sikkim">Sikkim</option>
                        <option value="Tamil Nadu">Tamil Nadu</option>
                        <option value="Telangana">Telangana</option>
                        <option value="Tripura">Tripura</option>
                        <option value="Uttar Pradesh">Uttar Pradesh</option>
                        <option value="Uttarakhand">Uttarakhand</option>
                        <option value="West Bengal">West Bengal</option>
                        <option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
                        <option value="Chandigarh">Chandigarh</option>
                        <option value="Dadra and Nagar Haveli and Daman and Diu">Dadra and Nagar Haveli and Daman and Diu</option>
                        <option value="Lakshadweep">Lakshadweep</option>
                        <option value="Delhi">Delhi</option>
                        <option value="Puducherry">Puducherry</option>
                        <option value="Ladakh">Ladakh</option>
                        <option value="Jammu and Kashmir">Jammu and Kashmir</option>
                    </select>                    
                </div>
                </div>
            </div><br>
            
            <div class="col-md-12">
                <div class="row"> 
                <div class="col-md-4">
                    <label for="city">City</label>
                    <input type="text" class="form-control" id="city1" name="city1" required>
                </div>
                <div class="col-md-4">
                    <label for="area">Area / Street </label>
                    <input type="text" class="form-control" id="area1" name="area1" required>
                </div>
                <div class="col-md-4">
                    <label for="build_name">Pincode</label>
                    <input type="text" class="form-control" id="pincode1" name="pincode1" required>
                </div>
                </div>
                </div><br>
                                    </section>
                                    
                                    <!-- Step 3 -->
                                    <h6> Doctor Educational Information</h6>
                                    <section>
                                     <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                    <label for="Education">Higher Education</label>
                    <input type="text" class="form-control" id="education" name="education" required>
                </div>
                <div class="col-md-6">
                    <label for="control-label">Specialisation</label><br>
                    <select class="form-control" name="specialisation" id="specialisation" aria-describedby="emailHelp" required>
                        <option value="">Please select specialisation … </option>
                        <option value="Neurologist">Neurologist</option>
                        <option value="Oncologist">Oncologist</option>
                        <option value="Audiologist">Audiologist</option>
                        <option value="Orthopedic">Orthopedic</option>
                        <option value="Opthalmologists">Opthalmologists</option>
                        <option value="Dentist">Dentist</option>
                        <option value="Cardiologist">Cardiologist</option>
                        <option value="Gynecologist">Gynecologist</option>
                        <option value="EyeSpecialist">Eye specialist</option>
                        <option value="Dermatologist">Dermatologist</option>
                        <option value="Other">Other</option>
                    </select>
                </div>
                </div>
                </div><br>
                
                <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                    <label for="control-label">member of any other medical associations?</label><br>
                    <select class="form-control" name="member" id="member" aria-describedby="emailHelp" required>
                        <option value="">Please select one … </option>
                        <option value="yes">Yes</option>
                        <option value="no">No</option>
                    </select>
                </div>
                
                <div class="col-md-6">
                    <label for="aadhar">Institute Name</label>
                    <input type="text" class="form-control" id="institute" name="institute" required>
                </div>
                </div>
                </div><br>
                
                <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                <label for="educated"> Please mention about your education. </label><br>
                <textarea class="form-control" id="educated" name="educated" placeholder="Type here..." rows="4"></textarea>
                </div>
                
                <div class="col-md-6">
                <label for="clinics"> Which clinics did you work before? Please list them all. </label>
                <textarea class="form-control" id="clinics" name="clinics" placeholder="Type here..." rows="4"></textarea>
                </div>
                </div>
                </div><br>
                
                
                <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                <label for="workbefore"> Which countries or cities did you work before? Please list them all. </label>
                <textarea class="form-control" id="workbefore" name="workbefore" placeholder="Type here..." rows="4"></textarea>
                </div>
                
                <div class="col-md-6">
                <label for="surgeries"> Please mention the surgeries in general that you have operated before. </label>
                <textarea class="form-control" id="surgeries" name="surgeries" placeholder="Type here..." rows="4"></textarea>
                </div>
                </div>
                </div><br>
                                    </section>
                                    
                                    
                                
                                    <!-- Step 4 -->
                                    <h6>Doctor Banking Information</h6>
                                    <section>
                                     <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                    <label for="bankname">Bank Name</label>
                    <input type="text" class="form-control" id="bnk_name" name="bnk_name" required>
                </div>
                
                <div class="col-md-6">
                    <label for="branch">Branch</label>
                    <input type="text" class="form-control" id="branch" name="branch" required>
                </div>
                </div>
                </div><br>
                
                
                <div class="col-md-12">
                <div class="row">
                <div class="col-md-6">
                    <label for="accno">Account Number</label>
                    <input type="text" class="form-control" id="acc_no" name="acc_no" required>
                </div>
                <div class="col-md-6">
                    <label for="ifsccode">IFSC code</label>
                    <input type="text" class="form-control" id="ifsc_code" name="ifsc_code" required>
                </div>
                </div>
                </div><br>       
                                        
                                    </section>
                                   
                                </form>
                            </div>
                        </div>
                    </div>
                    
                </div>
                
            </div>
           
        </div>
       
    </div>
    
    
 
            </div>
        
    <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
        
    </div>
   
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
  $(".tab-wizard").steps({
      headerTag: "h6",
      bodyTag: "section",
      transitionEffect: "fade",
      titleTemplate: '<span class="step">#index#</span> #title#',
      labels: {
          finish: "Submit"
      },
      onFinished: function(event, currentIndex) {
          $("form").submit();
      }
  });
</script>
</body>
</html>
      ''')