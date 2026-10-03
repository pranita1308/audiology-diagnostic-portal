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
          <h1 class="text-capitalize mb-5 text-lg">What We Do</h1>
		  <h5 class="text-white">"Care, compassion, and commitment—where healing truly begins"</h5>

          <!-- <ul class="list-inline breadcumb-nav">
            <li class="list-inline-item"><a href="home.py" class="text-white">Home</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">Our services</a></li>
          </ul> -->
        </div>
      </div>
    </div>
  </div>
</section>


<section class="section service-2">
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-md-6 col-sm-6">
				<div class="service-block mb-5">
					<img src="images/service/service-1.jpg" alt="" class="img-fluid">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Child care</h4>
						<p class="mb-4">Comprehensive medical care for infants, children, and teens.We ensure your child grows up healthy, safe, and strong</p>
					</div>
				</div>
			</div>

			<div class="col-lg-4 col-md-6 col-sm-6">
				<div class="service-block mb-5">
					<img src="images/service/service-2.jpg" alt="" class="img-fluid">
					<div class="content">
						<h4 class="mt-4 mb-2  title-color">Personal Care</h4>
						<p class="mb-4">Support with daily tasks like bathing, grooming, and mobility.Promoting comfort, dignity, and independence</p>
					</div>
				</div>
			</div>
			
			<div class="col-lg-4 col-md-6 col-sm-6">
				<div class="service-block mb-5">
					<img src="images/service/service-3.jpg" alt="" class="img-fluid">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">CT scan</h4>
						<p class="mb-4">Advanced imaging to diagnose internal injuries and diseases.Quick, accurate, and non-invasive diagnostic tool</p>
					</div>
				</div>
			</div>


			<div class="col-lg-4 col-md-6 col-sm-6">
				<div class="service-block mb-5 mb-lg-0">
					<img src="images/service/service-4.jpg" alt="" class="img-fluid">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Joint replacement</h4>
						<p class="mb-4">Surgical solutions for chronic joint pain and stiffness.Regain mobility and live pain-free</p>
					</div>
				</div>
			</div>

			<div class="col-lg-4 col-md-6 col-sm-6">
				<div class="service-block mb-5 mb-lg-0">
					<img src="images/service/service-6.jpg" alt="" class="img-fluid">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Examination & Diagnosis</h4>
						<p class="mb-4">Thorough medical check-ups and accurate testing.Early diagnosis for better treatment</p>
					</div>
				</div>
			</div>
			
			<div class="col-lg-4 col-md-6 col-sm-6">
				<div class="service-block mb-5 mb-lg-0">
					<img src="images/service/service-8.jpg" alt="" class="img-fluid">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Alzheimer's disease</h4>
						<p class="mb-4">Specialized care for patients with memory loss and confusion</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<section class="section cta-page">
	<div class="container">
		<div class="row">
			<div class="col-lg-7">
				<div class="cta-content">
					<div class="divider mb-4"></div>
					<h2 class="mb-5 text-lg">We are pleased to offer you the <span class="title-color">chance to have the healthy</span></h2>
					<a href="appoinment.py" class="btn btn-main-2 btn-round-full">Get appoinment<i class="icofont-simple-right  ml-2"></i></a>
				</div>
			</div>
		</div>
	</div>
</section>

</body>
</html>
''')

import footer