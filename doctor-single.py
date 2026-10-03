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
          <h1 class="text-capitalize mb-5 text-lg">Doctor Details</h1>
		  <h5 class="text-white">"Care, compassion, and commitment—where healing truly begins"</h5>

          <!-- <ul class="list-inline breadcumb-nav">
            <li class="list-inline-item"><a href="home.py" class="text-white">Home</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">Doctor Details</a></li>
          </ul> -->
        </div>
      </div>
    </div>
  </div>
</section>


<section class="section doctor-single" style="padding-bottom:0px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-md-6">
				<div class="doctor-img-block">
					<img src="images/team/1.jpg" alt="" class="img-fluid w-100">

					<div class="info-block mt-4">
						<h4 class="mb-0">Alexandar james</h4>
						<p>Orthopedic Surgary</p>
					</div>
				</div>
			</div>

			<div class="col-lg-8 col-md-6">
				<div class="doctor-details mt-lg-0">
					
					<h4 class="text-capitalize  text-lg" style="font-size:35px">Alexandar james</h4><br>
					<p>Experienced physician with 18+ years in internal medicine and critical care. Expert in diagnostics, emergency response, and global treatment standards. Committed to patient-focused and research-driven care.</p>
					<p></p>

					<h3 style="padding-top:5px">My Educational Qualifications</h3>
					<p style="padding-top:5px">2005–2007: MBBS, M.D., University of Wyoming, USA<br>
					2007–2009: M.D., Netherland Medical College, Netherlands<br>
					2009–2010: MBBS, M.D., University of Japan<br>
				    2010–2011: M.D., *Canada Medical College, Canada</p>
					
					<a href="appoinment.py" class="btn btn-main-2 btn-round-full mt-3">Make an Appoinment<i class="icofont-simple-right ml-2"></i></a>
				</div>
			</div>
		</div>
	</div>
</section>

<section class="section doctor-qualification" style="padding-top:50px;padding-bottom:50px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4">
				<h3>My skills</h3>
				<div class="divider my-4"></div>
				<p>Dr. Alexandar James is highly skilled in emergency and critical care, with strong diagnostic abilities and quick clinical judgment. He is proficient in telemedicine and electronic health records, ensuring effective, tech-enabled care.</p>			
			</div>
			<div class="col-lg-4">
				<div class="skill-list">
					<h5 class="mb-4">Expertise area</h5>
					<ul class="list-unstyled department-service">
						<li><i class="icofont-check mr-2"></i>International Drug Database</li>
						<li><i class="icofont-check mr-2"></i>Stretchers and Stretcher Accessories</li>
						<li><i class="icofont-check mr-2"></i>Cushions and Mattresses</li>
						<li><i class="icofont-check mr-2"></i>Cholesterol and lipid tests</li>
						<li><i class="icofont-check mr-2"></i>Critical Care Medicine Specialists</li>
						<li><i class="icofont-check mr-2"></i>Emergency Assistance</li>
					</ul>
				</div>
			</div>
			<div class="col-lg-4">
				<div class="sidebar-widget  gray-bg p-4">
					<h5 class="mb-4">Make Appoinment</h5>

					<ul class="list-unstyled lh-35">
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
</section>



<section class="section doctor-single" style="padding-bottom:0px;padding-top:30px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-md-6">
				<div class="doctor-img-block">
					<img src="images/doctors/doctor12.jpeg" alt="" class="img-fluid w-100">

					<div class="info-block mt-4">
						<h4 class="mb-0">Jasmeen Roy</h4>
						<p>Dental Surgery</p>
					</div>
				</div>
			</div>

			<div class="col-lg-8 col-md-6">
				<div class="doctor-details mt-lg-0">
					
					<h4 class="text-capitalize  text-lg" style="font-size:35px">Jasmeen Roy</h4><br>
					<p>Dr. Jasmeen Roy is a skilled dental surgeon with over 15 years of experience in cosmetic and restorative dentistry. She is passionate about creating healthy, confident smiles through modern techniques and personalized dental care.</p>
					<p></p>

					<h3 style="padding-top:5px">My Educational Qualifications</h3>
					<p style="padding-top:5px">2003–2008: BDS, King George's Medical University, India<br>
					2008–2011: MDS in Oral & Maxillofacial Surgery, University of Delhi<br>
					2012–2013: Fellowship in Cosmetic Dentistry, University of Melbourne, Australia<br>
				    2014–2015: Advanced Dental Implantology, University of Zurich, Switzerland</p>
					
					<a href="appoinment.py" class="btn btn-main-2 btn-round-full mt-3">Make an Appoinment<i class="icofont-simple-right ml-2"></i></a>
				</div>
			</div>
		</div>
	</div>
</section>

<section class="section doctor-qualification" style="padding-top:50px;padding-bottom:50px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4">
				<h3>My skills</h3>
				<div class="divider my-4"></div>
				<p>Dr. Jasmeen Roy specializes in dental aesthetics, oral surgeries, and full-mouth rehabilitation. She is highly proficient in digital dentistry, painless root canals, and smile designing using advanced techniques and technologies.</p>			
			</div>
			<div class="col-lg-4">
				<div class="skill-list">
					<h5 class="mb-4">Expertise area</h5>
					<ul class="list-unstyled department-service">
						<li><i class="icofont-check mr-2"></i>Cosmetic Dentistry</li>
						<li><i class="icofont-check mr-2"></i>Dental Implants</li>
						<li><i class="icofont-check mr-2"></i>Smile Design & Aesthetics</li>
						<li><i class="icofont-check mr-2"></i>Root Canal Treatments</li>
						<li><i class="icofont-check mr-2"></i>Full Mouth Rehabilitation</li>
						<li><i class="icofont-check mr-2"></i>Oral & Maxillofacial Surgery</li>
					</ul>
				</div>
			</div>
			<div class="col-lg-4">
				<div class="sidebar-widget  gray-bg p-4">
					<h5 class="mb-4">Make Appoinment</h5>

					<ul class="list-unstyled lh-35">
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
</section>



<section class="section doctor-single" style="padding-bottom:0px;padding-top:30px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-md-6">
				<div class="doctor-img-block">
					<img src="images/doctors/doctor1.jpg" alt="" class="img-fluid w-100">

					<div class="info-block mt-4">
						<h4 class="mb-0">Thomas Henry</h4>
						<p>Cardiology</p>
					</div>
				</div>
			</div>

			<div class="col-lg-8 col-md-6">
				<div class="doctor-details mt-lg-0">
					
					<h4 class="text-capitalize  text-lg" style="font-size:35px">Thomas Henry</h4><br>
					<p>Renowned cardiologist with over 20 years of clinical experience in diagnosing and treating complex heart conditions. Specializes in interventional cardiology, heart failure management, and preventive cardiac care. Dedicated to evidence-based treatments and compassionate patient care.</p>
					<p></p>

					<h3 style="padding-top:5px">My Educational Qualifications</h3>
					<p style="padding-top:5px">1998–2003: MBBS, Harvard Medical School, USA<br>
					2003–2006: M.D. in Internal Medicine, Mayo Clinic, USA<br>
					2006–2009: DM Cardiology, Oxford University, UK<br>
				    2010–2011: Fellowship in Interventional Cardiology, Mount Sinai Hospital, USA</p>
					
					<a href="appoinment.py" class="btn btn-main-2 btn-round-full mt-3">Make an Appoinment<i class="icofont-simple-right ml-2"></i></a>
				</div>
			</div>
		</div>
	</div>
</section>

<section class="section doctor-qualification" style="padding-top:50px;padding-bottom:50px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4">
				<h3>My skills</h3>
				<div class="divider my-4"></div>
				<p>Dr. Thomas Henry is skilled in cardiac imaging, catheter-based procedures, and managing advanced heart failure. He is adept at interpreting ECG, echocardiograms, and performing angioplasty and stent placements with precision and care.</p>			
			</div>
			<div class="col-lg-4">
				<div class="skill-list">
					<h5 class="mb-4">Expertise area</h5>
					<ul class="list-unstyled department-service">
						<li><i class="icofont-check mr-2"></i>Cardiac Catheterization</li>
						<li><i class="icofont-check mr-2"></i>Angioplasty & Stenting</li>
						<li><i class="icofont-check mr-2"></i>ECG & Holter Monitoring</li>
						<li><i class="icofont-check mr-2"></i>Echocardiography</li>
						<li><i class="icofont-check mr-2"></i>Heart Failure Management</li>
						<li><i class="icofont-check mr-2"></i>Preventive Cardiology</li>
					</ul>
				</div>
			</div>
			<div class="col-lg-4">
				<div class="sidebar-widget  gray-bg p-4">
					<h5 class="mb-4">Make Appoinment</h5>

					<ul class="list-unstyled lh-35">
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
</section>



<section class="section doctor-single" style="padding-bottom:0px;padding-top:30px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-md-6">
				<div class="doctor-img-block">
					<img src="images/doctors/doctor22.jpeg" alt="" class="img-fluid w-100">

					<div class="info-block mt-4">
						<h4 class="mb-0">Edwa John</h4>
						<p>Neurology</p>
					</div>
				</div>
			</div>

			<div class="col-lg-8 col-md-6">
				<div class="doctor-details mt-lg-0">
					
					<h4 class="text-capitalize  text-lg" style="font-size:35px">Edwa John</h4><br>
					<p>Dr. Edwa John is a senior neurologist with 16+ years of experience in diagnosing and managing complex neurological disorders. She specializes in epilepsy, stroke, multiple sclerosis, and neurodegenerative conditions with a focus on personalized, evidence-based care.</p>
					<p></p>

					<h3 style="padding-top:5px">My Educational Qualifications</h3>
					<p style="padding-top:5px">2002–2007: MBBS, All India Institute of Medical Sciences, India<br>
					2007–2010: M.D. in Internal Medicine, University of Glasgow, UK<br>
					2010–2013: DM in Neurology, Johns Hopkins University, USA<br>
				    2014–2015: Fellowship in Clinical Neurophysiology, University of Toronto, Canada</p>
					
					<a href="appoinment.py" class="btn btn-main-2 btn-round-full mt-3">Make an Appoinment<i class="icofont-simple-right ml-2"></i></a>
				</div>
			</div>
		</div>
	</div>
</section>

<section class="section doctor-qualification" style="padding-top:50px;padding-bottom:50px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4">
				<h3>My skills</h3>
				<div class="divider my-4"></div>
				<p>Dr. Edwa John excels in clinical neurology, neuroimaging, and neurodiagnostic procedures. She is experienced in managing seizures, brain stroke recovery, and chronic neurological conditions with precision and empathy.</p>			
			</div>
			<div class="col-lg-4">
				<div class="skill-list">
					<h5 class="mb-4">Expertise area</h5>
					<ul class="list-unstyled department-service">
						<li><i class="icofont-check mr-2"></i>Epilepsy and Seizure Management</li>
						<li><i class="icofont-check mr-2"></i>Stroke Rehabilitation</li>
						<li><i class="icofont-check mr-2"></i>EEG and EMG Testing</li>
						<li><i class="icofont-check mr-2"></i>Neurodegenerative Disorders</li>
						<li><i class="icofont-check mr-2"></i>Headache and Migraine Therapy</li>
						<li><i class="icofont-check mr-2"></i>Multiple Sclerosis Treatment</li>
					</ul>
				</div>
			</div>
			<div class="col-lg-4">
				<div class="sidebar-widget  gray-bg p-4">
					<h5 class="mb-4">Make Appoinment</h5>

					<ul class="list-unstyled lh-35">
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
</section>



<section class="section doctor-single" style="padding-bottom:0px;padding-top:30px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-md-6">
				<div class="doctor-img-block">
					<img src="images/doctors/doctor8.jpeg" alt="" class="img-fluid w-100">

					<div class="info-block mt-4">
						<h4 class="mb-0">Priti Yadav</h4>
						<p>General Medicine</p>
					</div>
				</div>
			</div>

			<div class="col-lg-8 col-md-6">
				<div class="doctor-details mt-lg-0">
					
					<h4 class="text-capitalize  text-lg" style="font-size:35px">Priti Yadav</h4><br>
					<p>Dr. Priti Yadav is an accomplished physician with 14+ years of experience in internal medicine. She is dedicated to comprehensive patient care, preventive health, and chronic disease management through evidence-based clinical practices.</p>
					<p></p>

					<h3 style="padding-top:5px">My Educational Qualifications</h3>
					<p style="padding-top:5px">2004–2009: MBBS, Grant Medical College, Mumbai, India<br>
					2009–2012: M.D. in General Medicine, PGIMER, Chandigarh<br>
					2013–2014: Fellowship in Diabetes & Endocrinology, University of Edinburgh, UK<br>
				    2015–2016: Certificate in Advanced Internal Medicine, Cleveland Clinic, USA</p>
					
					<a href="appoinment.py" class="btn btn-main-2 btn-round-full mt-3">Make an Appoinment<i class="icofont-simple-right ml-2"></i></a>
				</div>
			</div>
		</div>
	</div>
</section>

<section class="section doctor-qualification" style="padding-top:50px;padding-bottom:50px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4">
				<h3>My skills</h3>
				<div class="divider my-4"></div>
				<p>Dr. Priti Yadav is well-versed in diagnosing and treating a wide range of adult health issues. Her skills include managing hypertension, diabetes, thyroid disorders, and infectious diseases with patient-centric precision and care.</p>			
			</div>
			<div class="col-lg-4">
				<div class="skill-list">
					<h5 class="mb-4">Expertise area</h5>
					<ul class="list-unstyled department-service">
						<li><i class="icofont-check mr-2"></i>Chronic Disease Management</li>
						<li><i class="icofont-check mr-2"></i>Diabetes and Thyroid Care</li>
						<li><i class="icofont-check mr-2"></i>Hypertension Treatment</li>
						<li><i class="icofont-check mr-2"></i>General Health Checkups</li>
						<li><i class="icofont-check mr-2"></i>Infectious Disease Care</li>
						<li><i class="icofont-check mr-2"></i>Preventive Medicine</li>
					</ul>
				</div>
			</div>
			<div class="col-lg-4">
				<div class="sidebar-widget  gray-bg p-4">
					<h5 class="mb-4">Make Appoinment</h5>

					<ul class="list-unstyled lh-35">
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
</section>



<section class="section doctor-single" style="padding-bottom:0px;padding-top:30px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-md-6">
				<div class="doctor-img-block">
					<img src="images/doctors/doctor11.jpeg" alt="" class="img-fluid w-100">

					<div class="info-block mt-4">
						<h4 class="mb-0">Henry Forth</h4>
						<p>Pediatrics</p>
					</div>
				</div>
			</div>

			<div class="col-lg-8 col-md-6">
				<div class="doctor-details mt-lg-0">
					
					<h4 class="text-capitalize  text-lg" style="font-size:35px">Henry Forth</h4><br>
					<p>Dr. Henry Forth is a compassionate pediatrician with over 12 years of experience in child health and development. He is dedicated to ensuring the physical, emotional, and developmental well-being of infants, children, and adolescents through expert, child-friendly care.</p>
					<p></p>

					<h3 style="padding-top:5px">My Educational Qualifications</h3>
					<p style="padding-top:5px">2005–2010: MBBS, University of California, Los Angeles (UCLA), USA<br>
					2010–2013: M.D. in Pediatrics, Stanford University, USA<br>
					2014–2015: Fellowship in Neonatology, University of Toronto, Canada<br>
				    2016–2017: Certification in Pediatric Emergency Medicine, Boston Children’s Hospital, USA</p>
					
					<a href="appoinment.py" class="btn btn-main-2 btn-round-full mt-3">Make an Appoinment<i class="icofont-simple-right ml-2"></i></a>
				</div>
			</div>
		</div>
	</div>
</section>

<section class="section doctor-qualification" style="padding-top:50px;padding-bottom:50px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4">
				<h3>My skills</h3>
				<div class="divider my-4"></div>
				<p>Dr. Henry Forth is proficient in pediatric diagnosis, vaccination programs, neonatal care, and child nutrition. He ensures a comfortable and engaging clinical environment for young patients while offering parental guidance and early developmental assessments.</p>			
			</div>
			<div class="col-lg-4">
				<div class="skill-list">
					<h5 class="mb-4">Expertise area</h5>
					<ul class="list-unstyled department-service">
						<li><i class="icofont-check mr-2"></i>Child Growth & Development</li>
						<li><i class="icofont-check mr-2"></i>Immunizations & Vaccinations</li>
						<li><i class="icofont-check mr-2"></i>Neonatal Intensive Care</li>
						<li><i class="icofont-check mr-2"></i>Pediatric Emergency Care</li>
						<li><i class="icofont-check mr-2"></i>Asthma and Allergy Treatment</li>
						<li><i class="icofont-check mr-2"></i>Nutrition and Wellness Guidance</li>
					</ul>
				</div>
			</div>
			<div class="col-lg-4">
				<div class="sidebar-widget  gray-bg p-4">
					<h5 class="mb-4">Make Appoinment</h5>

					<ul class="list-unstyled lh-35">
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
</section>



<section class="section doctor-single" style="padding-bottom:0px;padding-top:30px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4 col-md-6">
				<div class="doctor-img-block">
					<img src="images/doctors/doctor7.jpeg" alt="" class="img-fluid w-100">

					<div class="info-block mt-4">
						<h4 class="mb-0">Sukanya Rathi</h4>
						<p>Traumatology</p>
					</div>
				</div>
			</div>

			<div class="col-lg-8 col-md-6">
				<div class="doctor-details mt-lg-0">
					
					<h4 class="text-capitalize  text-lg" style="font-size:35px">Sukanya Rathi</h4><br>
					<p>Dr. Sukanya Rathi is a highly skilled traumatologist with 13+ years of experience in managing critical injuries and emergency trauma cases. She specializes in fracture management, polytrauma care, and post-accident rehabilitation, with a focus on rapid and precise treatment.</p>
					<p></p>

					<h3 style="padding-top:5px">My Educational Qualifications</h3>
					<p style="padding-top:5px">2004–2009: MBBS, B.J. Medical College, Pune, India<br>
					2009–2012: M.S. in Orthopedics, AIIMS, New Delhi, India<br>
					2012–2013: Fellowship in Traumatology, Charité – Universitätsmedizin Berlin, Germany<br>
				    2014–2015: Advanced Training in Emergency Surgery, Harvard Medical School, USA</p>
					
					<a href="appoinment.py" class="btn btn-main-2 btn-round-full mt-3">Make an Appoinment<i class="icofont-simple-right ml-2"></i></a>
				</div>
			</div>
		</div>
	</div>
</section>

<section class="section doctor-qualification" style="padding-top:50px;padding-bottom:50px">
	<div class="container">
		<div class="row">
			<div class="col-lg-4">
				<h3>My skills</h3>
				<div class="divider my-4"></div>
				<p>Dr. Sukanya Rathi excels in emergency trauma care, orthopedic trauma surgery, and rapid diagnostics. She is proficient in managing fractures, dislocations, complex injuries, and post-surgical recovery with precision and empathy.</p>			
			</div>
			<div class="col-lg-4">
				<div class="skill-list">
					<h5 class="mb-4">Expertise area</h5>
					<ul class="list-unstyled department-service">
						<li><i class="icofont-check mr-2"></i>Fracture & Injury Management</li>
						<li><i class="icofont-check mr-2"></i>Polytrauma Care</li>
						<li><i class="icofont-check mr-2"></i>Emergency Orthopedic Surgery</li>
						<li><i class="icofont-check mr-2"></i>Spinal Injury Treatment</li>
						<li><i class="icofont-check mr-2"></i>Post-Trauma Rehabilitation</li>
						<li><i class="icofont-check mr-2"></i>Accident & Emergency Response</li>
					</ul>
				</div>
			</div>
			<div class="col-lg-4">
				<div class="sidebar-widget  gray-bg p-4">
					<h5 class="mb-4">Make Appoinment</h5>

					<ul class="list-unstyled lh-35">
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
</section>


</body>
</html>
''')

import footer