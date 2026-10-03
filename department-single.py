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
          <h1 class="text-capitalize mb-5 text-lg">Department Details</h1>
		  <h5 class="text-white">"Care, compassion, and commitment—where healing truly begins"</h5>

          <!-- <ul class="list-inline breadcumb-nav">
            <li class="list-inline-item"><a href="home.py" class="text-white">Home</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">Department Details</a></li>
          </ul> -->
        </div>
      </div>
    </div>
  </div>
</section>



<section class="section department-single" style="padding-top:100px">
	<div class="container">
		<div class="col-lg-12">
			<div class="row">
				<div class="col-lg-8">
					<div class="department-img">
						<img src="images/service/dept1.jpg" alt="" class="img-fluid" style="height:400px;width:800px">
					</div>
				</div>
				
				<div class="col-lg-4" style="padding-left:50px">
					<h3 class="">Services features</h3>
						<div class="divider my-4"></div><br>
							<ul class="list-unstyled department-service">
								<li><i class="icofont-check mr-2"></i>Vision Testing & Eye Exams</li>
								<li><i class="icofont-check mr-2"></i>Cataract & LASIK Surgery</li>
								<li><i class="icofont-check mr-2"></i>Retina & Glaucoma Treatment</li>
								<li><i class="icofont-check mr-2"></i>Pediatric Eye Care</li>
								<li><i class="icofont-check mr-2"></i>Corneal Transplants</li>
								<li><i class="icofont-check mr-2"></i>Diabetic Eye Disease Screening</li>
							</ul>
						    <a href="appoinment.py" class="btn btn-main-2 btn-round-full">Make an Appoinment<i class="icofont-simple-right ml-2  "></i></a>
				        </div>
			    </div>
		    
		</div>

		<div class="col-lg-12">
				<div class="department mt-5">
					<h3 class="text-md">Ophthalmology (Eye Care)</h3>
					<div class="divider my-4"></div>
					<p class="lead">Ophthalmology deals with the diagnosis, treatment, and prevention of eye diseases and visual disorders.
						It manages conditions like cataracts, glaucoma, diabetic retinopathy, and macular degeneration.
						Doctors perform surgeries such as LASIK, cataract removal, and corneal transplants.
						Refractive errors (myopia, hyperopia, astigmatism) are corrected with glasses, contact lenses, or surgery.
						Routine eye checkups help detect early signs of vision loss or eye strain.</p>

					<p>The department includes retina specialists, pediatric ophthalmologists, and optometrists.
						Children with squint (strabismus) or lazy eye (amblyopia) receive therapy and surgical options.
						Dry eye syndrome, allergies, infections, and conjunctivitis are treated with medications.
						Emergency care is provided for eye trauma, chemical exposure, or sudden vision loss.
						Advanced tools like Optical Coherence Tomography (OCT) and fundus photography aid diagnosis.
						Intraocular pressure checks help monitor and manage glaucoma.</p>
				</div>
		</div>
	  </div>
	</div>
</section>



<section class="section department-single" style="padding-top:0px">
	<div class="container">
		<div class="col-lg-12">
			<div class="row">
				<div class="col-lg-8">
					<div class="department-img">
						<img src="images/service/dept2.avif" alt="" class="img-fluid" style="height:400px;width:800px">
					</div>
				</div>
				
				<div class="col-lg-4" style="padding-left:50px">
					<h3 class="">Services features</h3>
						<div class="divider my-4"></div><br>
							<ul class="list-unstyled department-service">
								<li><i class="icofont-check mr-2"></i>ECG, Echo, and Stress Testing</li>
								<li><i class="icofont-check mr-2"></i>Angiography & Angioplasty</li>
								<li><i class="icofont-check mr-2"></i>Pacemaker Implantation</li>
								<li><i class="icofont-check mr-2"></i>Cardiac Rehabilitation</li>
								<li><i class="icofont-check mr-2"></i>Heart Failure Management</li>
								<li><i class="icofont-check mr-2"></i>24/7 Emergency Cardiac Care</li>
							</ul>
						    <a href="appoinment.py" class="btn btn-main-2 btn-round-full">Make an Appoinment<i class="icofont-simple-right ml-2  "></i></a>
				        </div>
			    </div>
		    
		</div>

		<div class="col-lg-12">
				<div class="department mt-5">
					<h3 class="text-md">Cardiology (Heart Care)</h3>
					<div class="divider my-4"></div>
					<p class="lead">Cardiology focuses on the diagnosis and management of heart and blood vessel diseases.
						It treats conditions like hypertension, heart attacks, heart failure, and arrhythmias.
						Advanced diagnostic tools such as ECG, 2D Echo, Holter monitoring, and stress tests are used.
						Coronary angiography and angioplasty are performed for blocked arteries.
						Cardiac rehabilitation programs help patients recover after heart surgery or attacks.
						Pacemaker implantation and defibrillator therapy are available for rhythm disorders.
						Patients with congenital heart defects receive lifelong specialized care.</p>					
					
					<p>Cardiologists provide long-term management for blood pressure and cholesterol.
						Non-invasive cardiology services reduce the need for surgical procedures.
						Emergency care is provided for acute chest pain, heart attack, or sudden collapse.
						Smoking cessation and weight management support are part of preventive care.
						Dietary counseling is offered to manage heart-friendly nutrition.
						Stress management and lifestyle modification clinics are conducted regularly.
						Regular cardiac checkups help in early detection and risk assessment.
						Valve disorders and murmurs are diagnosed with echocardiography and managed surgically if needed.</p>
				</div>
		</div>
		</div>
	</div>
</section>



<section class="section department-single" style="padding-top:0px">
	<div class="container">
		<div class="col-lg-12">
			<div class="row">
				<div class="col-lg-8">
					<div class="department-img">
						<img src="images/service/dept3.jpg" alt="" class="img-fluid" style="height:400px;width:800px">
					</div>
				</div>
				
				<div class="col-lg-4" style="padding-left:50px">
					<h3 class="">Services features</h3>
						<div class="divider my-4"></div><br>
							<ul class="list-unstyled department-service">
								<li><i class="icofont-check mr-2"></i>Teeth Cleaning & Scaling</li>
								<li><i class="icofont-check mr-2"></i>Fillings & Root Canal Treatment</li>
								<li><i class="icofont-check mr-2"></i>Braces & Invisalign</li>
								<li><i class="icofont-check mr-2"></i>Cosmetic Dentistry & Whitening</li>
								<li><i class="icofont-check mr-2"></i>Tooth Implants & Dentures</li>
								<li><i class="icofont-check mr-2"></i>Wisdom Tooth Extraction</li>
							</ul>
							<a href="appoinment.py" class="btn btn-main-2 btn-round-full">Make an Appoinment<i class="icofont-simple-right ml-2  "></i></a>
				        </div>
			    </div>
		    
		</div>

		<div class="col-lg-12">
				<div class="department mt-5">
					<h3 class="text-md">Dental Care</h3>
					<div class="divider my-4"></div>
					<p class="lead">Dental care involves the diagnosis, treatment, and prevention of oral health problems.
						Common issues treated include tooth decay, gum disease, bad breath, and tooth loss.
						Routine dental checkups help in early identification of oral infections.
						Tooth cleaning and polishing remove plaque and tartar to prevent cavities.
						Fillings are done to restore teeth damaged by decay.
						Root canal treatment saves infected or decayed teeth without removal.
						Crowns and bridges restore broken or missing teeth.
						Orthodontics provides braces and aligners to correct misaligned teeth.
						Cosmetic procedures include teeth whitening, veneers, and smile makeovers.
						Pediatric dentistry handles children's dental problems with special care.</p>

					<p>Wisdom tooth extractions are performed with local or general anesthesia.
						Gum surgeries treat advanced periodontitis and bleeding gums.
						Implantology offers tooth implants as permanent replacements.
						Digital X-rays and oral scans are used for precise diagnosis.
						Bad breath treatment includes tongue cleaning, mouthwash, and professional hygiene.
						Tooth sensitivity is treated with desensitizing procedures and fluoride.
						Dentures are customized for senior patients who’ve lost teeth.</p>
				</div>
		</div>
		</div>
	</div>
</section>



<section class="section department-single" style="padding-top:0px">>
	<div class="container">
		<div class="col-lg-12">
			<div class="row">
				<div class="col-lg-8">
					<div class="department-img">
						<img src="images/service/bg-1.jpg" alt="" class="img-fluid" style="height:400px;width:800px">
					</div>
				</div>
				
				<div class="col-lg-4" style="padding-left:50px">
					<h3 class="">Services features</h3>
						<div class="divider my-4"></div><br>
							<ul class="list-unstyled department-service">
								<li><i class="icofont-check mr-2"></i>General OPD Consultations</li>
								<li><i class="icofont-check mr-2"></i>Management of Chronic Illnesses</li>
								<li><i class="icofont-check mr-2"></i>Infectious Disease Diagnosis & Treatment</li>
								<li><i class="icofont-check mr-2"></i>Preventive Health Check-ups</li>
								<li><i class="icofont-check mr-2"></i>Vaccinations & Immunization</li>
								<li><i class="icofont-check mr-2"></i>Minor Procedures</li>
								<li><i class="icofont-check mr-2"></i>Fever & Infection Management</li>
								<li><i class="icofont-check mr-2"></i>Lifestyle & Diet Counseling</li>
								<li><i class="icofont-check mr-2"></i>Multisystem Symptom Evaluation</li>
							</ul>

						<a href="appoinment.py" class="btn btn-main-2 btn-round-full">Make an Appoinment<i class="icofont-simple-right ml-2  "></i></a>
				</div>
			</div>
		</div>



		<div class="row">
			<div class="col-lg-12">
				<div class="department-content mt-5">
					<h3 class="text-md">Medecine and Health</h3>
					<div class="divider my-4"></div>
					<p class="lead">The Medicine and Health department serves as the backbone of internal medical care in any hospital.
						It provides diagnosis and non-surgical treatment for a wide range of adult health problems.
						General physicians manage acute conditions like fever, infections, and allergies.
						They also offer long-term care for chronic diseases such as diabetes, hypertension, and thyroid disorders.
						Patients with overlapping symptoms affecting multiple organs are evaluated comprehensively.
						Routine physical check-ups are available for health maintenance and early disease detection.
						Preventive care, including lifestyle advice and vaccination, is a major focus of the department.
						Management of seasonal diseases like dengue, malaria, and viral infections is provided.
						The department often acts as the first point of contact before referrals to specialties.</p>

					<p>Blood pressure, sugar levels, and cholesterol are monitored and managed regularly.
						Medical management for headaches, fatigue, dehydration, and gastric issues is provided.
						Support for conditions like anemia, vitamin deficiency, and hormonal imbalance is offered.
						Outpatient care is available for minor illnesses, while inpatient care handles more complex conditions.
						Specialized clinics may run for diabetes, hypertension, and obesity management.
						Electrolyte imbalance, joint pain, and fatigue are investigated and treated effectively.</p>
				</div>
			</div>
		</div>
	</div>
</section>



<section class="section department-single" style="padding-top:0px">
	<div class="container">
		<div class="col-lg-12">
			<div class="row">
				<div class="col-lg-8">
					<div class="department-img">
						<img src="images/service/dept4.png" alt="" class="img-fluid" style="height:400px;width:800px">
					</div>
				</div>
				
				<div class="col-lg-4" style="padding-left:50px">
					<h3 class="">Services features</h3>
						<div class="divider my-4"></div><br>
							<ul class="list-unstyled department-service">
								<li><i class="icofont-check mr-2"></i>Vaccinations & Immunizations</li>
								<li><i class="icofont-check mr-2"></i>Growth & Development Monitoring</li>
								<li><i class="icofont-check mr-2"></i>Nutritional Counseling</li>
								<li><i class="icofont-check mr-2"></i>Newborn & Premature Baby Care</li>
								<li><i class="icofont-check mr-2"></i>Asthma & Allergy Management</li>
								<li><i class="icofont-check mr-2"></i>Pediatric Emergency Care</li>
							</ul>
						    <a href="appoinment.py" class="btn btn-main-2 btn-round-full">Make an Appoinment<i class="icofont-simple-right ml-2  "></i></a>
				        </div>
			    </div>
		    
		</div>

		<div class="col-lg-12">
				<div class="department mt-5">
					<h3 class="text-md">Child Care (Pediatrics)</h3>
					<div class="divider my-4"></div>
					<p class="lead">Pediatrics focuses on the overall physical and mental development of children from birth to adolescence.
						It includes preventive care like immunizations and routine health checkups.
						Newborn screening detects inherited or metabolic disorders early.
						Growth monitoring ensures children are developing at a healthy pace.
						Nutritional counseling is provided for underweight or obese children.
						Vaccination programs follow national and international schedules.
						Common childhood illnesses like fever, cold, diarrhea, and infections are treated.
						Special care is given to premature or low-birth-weight babies.</p>

					<p>Pediatricians assess and manage delayed milestones in speech or movement.
						Developmental disorders like autism or ADHD are screened and referred early.
						Pediatric cardiology, neurology, and endocrinology services are available.
						Asthma and allergies are managed with inhalers and desensitization therapy.
						Behavioral counseling helps with anxiety, learning issues, and school stress.
						Adolescent health counseling focuses on puberty, menstruation, and hygiene.
						Regular deworming and vitamin supplementation is advised in growing years.
						Parents receive guidance on feeding, sleep habits, and screen time.</p>
				</div>
		</div>
		</div>
	</div>
</section>



<section class="section department-single" style="padding-top:0px">
	<div class="container">
		<div class="col-lg-12">
			<div class="row">
				<div class="col-lg-8">
					<div class="department-img">
						<img src="images/service/dept5.jpeg" alt="" class="img-fluid" style="height:400px;width:800px">
					</div>
				</div>
				
				<div class="col-lg-4" style="padding-left:50px">
					<h3 class="">Services features</h3>
						<div class="divider my-4"></div><br>
						<ul class="list-unstyled department-service">
							<li><i class="icofont-check mr-2"></i>Asthma & COPD Management</li>
							<li><i class="icofont-check mr-2"></i>Bronchoscopy & Pulmonary Tests</li>
							<li><i class="icofont-check mr-2"></i>Sleep Apnea Diagnosis</li>
							<li><i class="icofont-check mr-2"></i>Tuberculosis Diagnosis & Treatment</li>
							<li><i class="icofont-check mr-2"></i>Smoking Cessation Programs</li>
							<li><i class="icofont-check mr-2"></i>Oxygen Therapy & Chest Physiotherapy</li>
						</ul>
						    <a href="appoinment.py" class="btn btn-main-2 btn-round-full">Make an Appoinment<i class="icofont-simple-right ml-2  "></i></a>
				        </div>
			    </div>
		    
		</div>

		<div class="col-lg-12">
				<div class="department mt-5">
					<h3 class="text-md">Pulmonology (Respiratory Care)</h3>
					<div class="divider my-4"></div>
					<p class="lead">Pulmonology focuses on diseases related to the lungs and respiratory system.
						Common conditions treated include asthma, COPD, tuberculosis, pneumonia, and bronchitis.
						Pulmonary function tests (PFTs) assess lung capacity and breathing patterns.
						Chest X-rays and CT scans are used to detect infections or tumors.
						Bronchoscopy allows doctors to view the airways and collect samples.
						Allergy testing is done to find triggers for respiratory allergies and asthma.
						Long-term oxygen therapy is offered for patients with chronic breathing issues.
						Sleep studies help diagnose sleep apnea and related conditions.
						Tuberculosis is diagnosed and treated through national TB control programs.
						Smoking cessation programs assist in lung health recovery.</p>

					<p>Chronic cough and breathlessness are evaluated with spirometry and imaging.
						Pulmonary rehabilitation improves quality of life in patients with lung damage.
						Inhalers, nebulizers, and steroid therapies are prescribed based on severity.
						Lung infections in immunocompromised patients are managed with precision antibiotics.
						ICU and ventilator support are available for critically ill patients.
						Respiratory physiotherapy is offered to aid recovery and mucus clearance.
						Patients with interstitial lung disease receive long-term follow-up.</p>
				</div>
		</div>
		</div>
	</div>
</section>



<section class="section department-single" style="padding-top:0px">
	<div class="container">
		<div class="col-lg-12">
			<div class="row">
				<div class="col-lg-8">
					<div class="department-img">
						<img src="images/service/dept6.jpg" alt="" class="img-fluid" style="height:400px;width:800px">
					</div>
				</div>
				
				<div class="col-lg-4" style="padding-left:50px">
					<h3 class="">Services features</h3>
						<div class="divider my-4"></div><br>
							<ul class="list-unstyled department-service">
								<li><i class="icofont-check mr-2"></i>Menstrual Disorder Management</li>
								<li><i class="icofont-check mr-2"></i>Pregnancy & Prenatal Care</li>
								<li><i class="icofont-check mr-2"></i>Infertility Evaluation & Treatment</li>
								<li><i class="icofont-check mr-2"></i>Menopause & Hormonal Therapy</li>
								<li><i class="icofont-check mr-2"></i>PAP Smear & Cancer Screening</li>
								<li><i class="icofont-check mr-2"></i>Laparoscopic Gynecological Surgeries</li>
							</ul>
						    <a href="appoinment.py" class="btn btn-main-2 btn-round-full">Make an Appoinment<i class="icofont-simple-right ml-2  "></i></a>
				        </div>
			    </div>
		    
		</div>

		<div class="col-lg-12">
				<div class="department mt-5">
					<h3 class="text-md">Gynecology (Women's Health)</h3>
					<div class="divider my-4"></div>
					<p class="lead">Gynecology deals with women’s reproductive health, hormonal balance, and wellness.
						It covers conditions related to menstruation, fertility, pregnancy, and menopause.
						Menstrual issues such as irregular cycles, pain, or heavy bleeding are treated with medications or surgery.
						Prenatal care includes monitoring pregnancy, scans, and dietary guidance.
						High-risk pregnancies are managed by specialists with regular fetal monitoring.
						Ultrasound services help in pregnancy assessment and gynecological diagnosis.
						Infertility investigations include hormone tests, ultrasound, and laparoscopy.
						Contraceptive counseling is offered based on age and health status.</p>

					<p>PCOS and hormonal imbalances are treated with lifestyle and medication.
						PAP smears and HPV testing are done for early cervical cancer detection.
						Breast examinations and mammography help detect breast cancer early.
						Hysterectomy and fibroid removal surgeries are performed laparoscopically.
						Menopause management includes hormone therapy and lifestyle changes.
						Sexual health counseling is available for women of all ages.</p>
				</div>
		</div>
		</div>
	</div>
</section>



</body>
</html>
''')

import footer