#!C:/Python312/python.exe
import os
import http.cookies

# Step 1: Print headers first
print("Content-Type: text/html\n")

# Step 2: Read session cookie
cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session_id = cookies.get("session_id")
session_valid = False

# Step 3: Check if session file exists
if session_id:
    sid = session_id.value
    session_file = f"sessions/{sid}.txt"
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            content = f.read().strip()
            if content:
                session_valid = True

# Step 4: If session is not valid, redirect to login
if not session_valid:
    print('''
    <script>
        alert("You must login in first.");
        window.location.href = "home.py";  // Your login page
    </script>
    ''')
    exit()

# Your original code starts here — DO NOT CHANGE ANYTHING BELOW
import header
print (header.homehtml)

print('''
<!DOCTYPE html>
<html lang="zxx">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="description" content="Orbitor,business,company,agency,modern,bootstrap4,tech,software">
  <meta name="author" content="themefisher.com">

  <title>Medico- Health & Care Hospital</title>

  <!-- Favicon -->
  <link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico" />

  <!-- bootstrap.min css -->
  <link rel="stylesheet" href="plugins/bootstrap/css/bootstrap.min.css">
  <!-- Icon Font Css -->
  <link rel="stylesheet" href="plugins/icofont/icofont.min.css">
  <!-- Slick Slider  CSS -->
  <link rel="stylesheet" href="plugins/slick-carousel/slick/slick.css">
  <link rel="stylesheet" href="plugins/slick-carousel/slick/slick-theme.css">

  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="css/style.css">
</head>

<body id="top">

<!-- Header is included above from header.py -->

<!-- Slider Start -->

<section class="page-title bg-1">
  <div class="overlay"></div>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="block text-center">
          <h1 class="text-capitalize mb-5 text-lg">Appoinment</h1>
          <h5 class="text-white">"Care, compassion, and commitment—where healing truly begins"</h5>

          <!-- <ul class="list-inline breadcumb-nav">
            <li class="list-inline-item"><a href="home.py" class="text-white">Home</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">Book your Seat</a></li>
          </ul> -->
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section appoinment">
	<div class="container">
		<div class="row align-items-center">
			<div class="col-lg-6 ">
				<div class="appoinment-content">
					<img src="images/team/d30.png" alt="" class="img-fluid"></br></br></br>
					<div class="emergency" style="height:20px;with:50px;">
						<h2 class="text-lg"><i class="icofont-phone-circle text-lg"></i>+23 345 67980</h2>
					</div>
				</div>
			</div>
			<div class="col-lg-6 col-md-10" style="padding-top:0px">
				<div class="appoinment-wrap mt-5 mt-lg-0">
					<h2 class="mb-2 title-color" style="font-size:50px">Book appoinment</h2>
					<p class="mb-4">Our specialists are ready to help — book your appointment with ease</p>
					     <form id="#" class="appoinment-form" method="post" action="appoinmentbackend.py">
                    <div class="row">
                         <div class="col-lg-6">
                            <div class="form-group">
                                <select class="form-control" id="department" required = " ">
                                    <option>Choose Department</option>
                                    <option>Audiology</option>
                                    <option>Cardiology</option>
									<option>Neurology</option>
									<option>Orthopedics</option>
									<option>Dermatology</option>
									<option>Gynecology</option>
									<option>Pediatrics</option>
									<option>General Surgery</option>
									<option>Radiology</option>
									<option>Dental Care</option>
									<option>Physiotherapy</option>
									<option>ENT</option>
									<option>Ophthalmology</option>
									<option>Psychiatry</option>
									<option>Urology</option>
									<option>Oncology</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-lg-6">
                            <div class="form-group">
                                <select class="form-control" id="doctor" required = " ">
                                    <option>Select Doctors</option>
                                    <option>Audiology</option>
                                    <option>General Physician</option>
									<option>Cardiologist</option>
									<option>Neurologist</option>
									<option>Orthopedic Surgeon</option>
									<option>Dentist</option>
									<option>Gynecologist</option>
									<option>Pediatrician</option>
									<option>Dermatologist</option>
									<option>ENT Specialist</option>
									<option>Ophthalmologist</option>
									<option>Psychiatrist</option>
									<option>Urologist</option>
									<option>Oncologist</option>
									<option>Gastroenterologist</option>
									<option>Nephrologist</option>
									<option>Radiologist</option>
									<option>Physiotherapist</option>
									<option>Plastic Surgeon</option>
									<option>Endocrinologist</option>
									<option>Pulmonologist</option>
                                </select>
                            </div>
                        </div>

                         <div class="col-lg-6">
                            <div class="form-group">
                                <input name="date" id="date" type="text" class="form-control" placeholder="dd/mm/yyyy" required ="  ">
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="form-group">
                                <input name="" id="time" type="text" class="form-control" placeholder="Time" required = " ">
                            </div>
                        </div>
                         <div class="col-lg-6">
                            <div class="form-group">
                                <input name="" id="fullname" type="text" class="form-control" placeholder="Full Name" required =" ">
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="form-group">
                                <input name="" id="phone" type="Number" class="form-control" placeholder="Phone Number" required = " ">
                            </div>
                        </div>
                    </div>
                    <div class="form-group-2 mb-4">
                        <textarea name="" id="message" class="form-control" rows="6" placeholder="Your Message" required = " "></textarea>
                    </div>

                    <a class="btn btn-main btn-round-full" href="appoinmentbackend.py" >Make Appoinment <i class="icofont-simple-right ml-2  "></i></a>
                </form>
            </div>
			</div>
		</div>
	</div>
</section>

</body>
</html>
''')

import footer
   

    