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
          <h1 class="text-capitalize mb-5 text-lg">Blog Single</h1>
		  <h5 class="text-white">"Care, compassion, and commitment—where healing truly begins"</h5>


          <!-- <ul class="list-inline breadcumb-nav">
            <li class="list-inline-item"><a href="index.html" class="text-white">Home</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">News details</a></li>
          </ul> -->
        </div>
      </div>
    </div>
  </div>
</section>



<section class="section blog-wrap">
	<div class="container">
		<div class="row">

			<div class="col-lg-12">
				<div class="">
					<img src="images/blog/blog-1.jpg" alt="" class="img-fluid" style="height:500px;width:1300px">
				</div>
			</div>

			<div class="col-lg-12" style="padding-top:50px">
				<div class="blog-item">
					<h2 class="mb-4 text-md"><a href="blog-single.html">Healthy environment to care with modern equipment</a></h2>
					<p class="lead mb-4">At our facility, we believe that healing begins not just with treatment, but with the environment around you. That’s why we’ve created a space that’s not only clean and safe but also equipped with cutting-edge medical technology.</p>
					<p class="lead mb-4 font-weight-normal text-black"> Why a Healthy Environment Matters:<br>
						1.A well-maintained, hygienic space reduces the risk of infections and creates a peaceful atmosphere that promotes quicker recovery.<br>

						2.Our hospital is designed with natural lighting, ventilation, and comfort in mind—so you feel at ease the moment you walk in.</p>

					<blockquote class="quote">
						 "A brand for a healthcare institution is like trust for a doctor — it’s earned through care, compassion, and doing difficult things with excellence."
					</blockquote>

					<p class="lead mb-4 font-weight-normal text-black">Why Modern Equipment is Essential:<br>

						1.We use state-of-the-art diagnostic and treatment tools to ensure precision, speed, and better outcomes.<br>

						2.From imaging (like CT scans and MRIs) to surgical systems and lab testing machines—our technology is up to international standards.<br>

						3.Modern tools mean less invasive procedures, faster results, and fewer errors.</p><br>

					<p class="lead mb-4 font-weight-normal text-black"> Our Promise:<br>mitted to combining modern science with compassionate care, providing every patient with a space that feels safe, welcoming, and trustworthy.</p>

				<div class="mt-5 clearfix">
				    <ul class="float-left list-inline tag-option"> 
				    	<li class="list-inline-item"><a href="#">Advancher</a></li>
				    	<li class="list-inline-item"><a href="#">Landscape</a></li>
				    	<li class="list-inline-item"><a href="#">Travel</a></li>
				   	</ul>        

				    <ul class="float-right list-inline">
				        <li class="list-inline-item"> Share: </li>
				        <li class="list-inline-item"><a href="#" target="_blank"><i class="icofont-facebook" aria-hidden="true"></i></a></li>
				        <li class="list-inline-item"><a href="#" target="_blank"><i class="icofont-twitter" aria-hidden="true"></i></a></li>
				        <li class="list-inline-item"><a href="#" target="_blank"><i class="icofont-pinterest" aria-hidden="true"></i></a></li>
				        <li class="list-inline-item"><a href="#" target="_blank"><i class="icofont-linkedin" aria-hidden="true"></i></a></li>
				    </ul>
			    </div>
				</div>
			</div>
		
	
	<div class="col-lg-12">
		<div class="row">
			<div class="col-lg-6">
				<form class="comment-form my-5" id="comment-form">
					<h4 class="mb-4">Write a comment</h4>
					<div class="row">
						<div class="col-md-6">
							<div class="form-group">
								<input class="form-control" type="text" name="name" id="name" placeholder="Name:">
							</div>
						</div>
						<div class="col-md-6">
							<div class="form-group">
								<input class="form-control" type="text" name="mail" id="mail" placeholder="Email:">
							</div>
						</div>
					</div>
					<textarea class="form-control mb-4" name="comment" id="comment" cols="30" rows="6" placeholder="Comment"></textarea>

					<input class="btn btn-main-2 btn-round-full" type="submit" name="submit-contact" id="submit_contact" value="Submit Message">
				</form>
			</div>


			<div class="col-lg-6" style="padding-top:50px">
				<div class="sidebar-widget schedule-widget mb-2">
					<h5 class="">Time Schedule</h5>
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
				</div>
			</div>
		</div>
	</div>

  </div>
 </div>

</section>


</body>
</html>
''')

import footer
