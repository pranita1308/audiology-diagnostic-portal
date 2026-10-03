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

<section class="page-title bg-1">
  <div class="overlay"></div>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="block text-center">
          <h1 class="text-capitalize mb-5 text-lg">Blog articles</h1>
          <h5 class="text-white">"Care, compassion, and commitment—where healing truly begins"</h5>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section blog-wrap">
    <div class="container">
	   <div class="row">
			<div class="col-lg-12">

			  	<div class="sidebar-widget search mb-3">
            		<h5>Search Here</h5>
            		<form action="#" class="search-form">
              			<input type="text" class="form-control" placeholder="search">
              			<i class="ti-search"></i>
            		</form>
          		</div>


				<div class="row">

					<div class="col-lg-6">
						<div class="blog-item">
							<img src="images/blog/blog-1.jpg" alt="" class="img-fluid" style="height:550px">
						</div>
					</div>

				<div class="col-lg-6">
					<div class="blog-item-content">
					<h2 class=""><a href="blog-single.html">Choose quality service over type of things</a></h2><br>
						<p class="mb-4">When it comes to your health, never compromise on quality.<br></br>

							Here’s why quality matters:</br>

							1.Your Health is Precious
							Quality care means accurate diagnosis, safe treatment, and faster recovery.<br>

							2.Expert Care
							Skilled doctors, nurses, and clean, well-equipped facilities make all the difference.<br>

							3.True Cost Savings
							Cheap care can lead to mistakes, extra treatments, and more expenses later.<br>

							4.Peace of Mind
							With trusted professionals, you feel safe, supported, and confident in your care.<br></p><br>
						
						<a href="blog-single.html" target="_blank" class="btn btn-main btn-icon btn-round-full">Read More <i class="icofont-simple-right ml-2  "></i></a>
					</div>
				</div>
			</div>

			
			<div class="col-lg-12" style="padding-top:100px">
				<div class="row">
					<div class="col-lg-6">
						<div class="blog-item">
							<img src="images/blog/blog-2.jpg" alt="" class="img-fluid" style="height:550px;width:550px">
						</div>
					</div>

					<div class="col-lg-6">
						<div class="blog-item-content">
							<h2 class=""><a href="blog-single.html">All test cost 25% in always in our laboratory</a></h2>
							<p class="mb-4">We offer a flat 25% discount on all diagnostic tests in our laboratory—every day, no conditions.<br><br>

								Why choose our lab?<br>

								1.Affordable Pricing
								Quality tests at reduced costs, helping you save on healthcare.<br>

								2.Advanced Equipment
								We use modern, reliable machines for accurate results.<br>

								3.Quick & Trusted Reports
								Fast processing with reports reviewed by expert technicians.<br>

								4.No Hidden Charges
								Transparent pricing—what you see is what you pay.</p><br>

							<a href="blog-single.html" target="_blank" class="btn btn-main btn-icon btn-round-full">Read More <i class="icofont-simple-right ml-2  "></i></a>
						</div>
					</div>
				</div>
			</div>

			<div class="col-lg-12" style="padding-top:100px">
				<div class="row">
					<div class="col-lg-6">
						<div class="blog-item">
							<div class="blog-thumb">
								<img src="images/blog/blog-4.jpg" alt="" class="img-fluid" style="height:550px;width:550px">
							</div>
						</div>
					</div>

					<div class="col-lg-6">
						<div class="blog-item-content">
								<h2 class=""><a href="blog-single.html">Get Free consultation from surgeon and doctors</a></h2>
								<p class="mb-4">Take the first step toward better health with a free consultation from our top specialists—no hidden fees.<br><br>

									Why book with us?

									1.Specialist Access
									Meet experienced doctors and surgeons without any consultation charges.<br>

									2.Personalized Guidance
									Get expert opinions, diagnosis, and advice tailored to your needs.<br>

									3.No Commitment
									Absolutely free—no pressure to proceed unless you're ready.<br>

									4.Early Intervention
									Discuss symptoms early and plan your treatment the right way.<br></p><br>

								<a href="blog-single.html" target="_blank" class="btn btn-main btn-icon btn-round-full">Read More <i class="icofont-simple-right ml-2  "></i></a>
						</div>
					</div>
				</div>
			</div>
		</div> <!-- End of inner row -->
  	</div> <!-- End of col-lg-12 -->



	<div="col-lg-12" style="padding-top:100px">
		<div="row">
	
			<div class="col-lg-6" style="padding-top:100px">
				<div class="sidebar-widget schedule-widget mb-3">   
						<h5 class="mb-2">Time Schedule</h5>
						<ul class="list-unstyled">
						<li class="d-flex justify-content-between align-items-center">
							<a href="#">Monday - Friday</a>
							<span>9:00 - 17:00</span>
						</li>
						<li class="d-flex justify-content-between align-items-center">
							<a href="#">Saturday</a>
							<span>9:00 - 16:00</span>
						</li>
						<li class="d-flex justify-content-between align-items-center">
							<a href="#">Sunday</a>
							<span>Closed</span>
						</li>
						</ul>
						<div class="sidebar-contatct-info mt-4">
						<p class="mb-0">Need Urgent Help?</p>
						<h4>+23-4565-65768</h4>
						</div>
				</div>
			</div>


			<div class="col-lg-6">
				<div class="row mt-5">
					<div class="col-lg-8">
						<nav class="pagination py-2 d-inline-block">
							<div class="nav-links">
								<span aria-current="page" class="page-numbers current">1</span>
								<a class="page-numbers" href="learnmore.py">2</a>
								<a class="page-numbers" href="service.py">3</a>
								<a class="page-numbers" href="about.py"><i class="icofont-thin-double-right"></i></a>
							</div>
						</nav>
					</div>
				</div> 
			</div>
		</div>
	</div>
</section>

<!-- Footer will be printed below -->
''')

import footer
