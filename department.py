#!C:/Python312/python.exe

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
          <span class="text-white"></span>
          <h1 class="text-capitalize mb-5 text-lg">All Department</h1>
		  <h5 class="text-white">"Care, compassion, and commitment—where healing truly begins"</h5>

          <!-- <ul class="list-inline breadcumb-nav">
            <li class="list-inline-item"><a href="home.py" class="text-white">Home</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">All Department</a></li>
          </ul> -->
        </div>
      </div>
    </div>
  </div>
</section>


<section class="section service-2">
	<div class="container">
		<div class="row justify-content-center">
			<div class="col-lg-7 text-center">
				<div class="section-title">
					<h2>Award winning patient care</h2>
					<div class="divider mx-auto my-4"></div>
					<p>Recognized for excellence in clinical outcomes, compassion, and innovation. We deliver personalized, world-class healthcare with trust and empathy</p>
				</div>
			</div>
		</div>

		<div class="row">
			<div class="col-lg-4 col-md-6 ">
				<div class="department-block mb-5">
					<img src="images/service/dept1.jpg" alt="" class="img-fluid w-100" style="height:230px;width:200px">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Opthomology</h4>
						<p class="mb-4">Deals with diagnosis and treatment of eye disorders. Provides services like vision tests, cataract surgery, and glaucoma care</p>
						<a href="department-single.py" class="read-more">Learn More  <i class="icofont-simple-right ml-2"></i></a>
					</div>
				</div>
			</div>

			<div class="col-lg-4 col-md-6">
				<div class="department-block mb-5">
					<img src="images/service/dept2.avif" alt="" class="img-fluid w-100" style="height:230px;width:200px">
					<div class="content">
						<h4 class="mt-4 mb-2  title-color">Cardiology</h4>
						<p class="mb-4">Focuses on heart-related conditions such as hypertension, heart attack, and arrhythmias. Offers ECG, angiography, and cardiac care</p>
						<a href="department-single.py" class="read-more">Learn More <i class="icofont-simple-right ml-2"></i></a>
					</div>
				</div>
			</div>
			
			<div class="col-lg-4 col-md-6">
				<div class="department-block mb-5">
					<img src="images/service/dept3.jpg" alt="" class="img-fluid w-100" style="height:230px;width:200px">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Dental Care</h4>
						<p class="mb-4">Provides oral health services like cleaning, fillings, root canals, and cosmetic dentistry. Prevents and treats gum and tooth diseases</p>
						<a href="department-single.py" class="read-more">Learn More <i class="icofont-simple-right ml-2"></i></a>
					</div>
				</div>
			</div>


			<div class="col-lg-4 col-md-6 ">
				<div class="department-block  mb-5 mb-lg-0">
					<img src="images/service/dept4.png" alt="" class="img-fluid w-100" style="height:230px;width:200px">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Child Care</h4>
						<p class="mb-4">Specializes in medical care for infants, children, and adolescents. Covers vaccinations, nutrition, and developmental health</p>
						<a href="department-single.py" class="read-more">Learn More <i class="icofont-simple-right ml-2"></i></a>
					</div>
				</div>
			</div>

			<div class="col-lg-4 col-md-6">
				<div class="department-block mb-5 mb-lg-0">
					<img src="images/service/dept5.jpeg" alt="" class="img-fluid w-100" style="height:230px;width:200px">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Pulmology</h4>
						<p class="mb-4">Treats diseases of the lungs and respiratory system like asthma, bronchitis, and COPD. Offers lung function tests and therapies</p>
						<a href="department-single.py" class="read-more">Learn More <i class="icofont-simple-right ml-2"></i></a>
					</div>
				</div>
			</div>
			
			<div class="col-lg-4 col-md-6">
				<div class="department-block mb-5 mb-lg-0">
					<img src="images/service/dept6.jpg" alt="" class="img-fluid w-100" style="height:230px;width:200px">
					<div class="content">
						<h4 class="mt-4 mb-2 title-color">Gynecology</h4>
						<p class="mb-4">Focuses on women’s reproductive health, including menstruation, pregnancy, and menopause. Provides screenings and fertility support.</p>
						<a href="department-single.py" class="read-more">Learn More <i class="icofont-simple-right ml-2"></i></a>
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