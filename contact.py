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
          <h1><span class="text-white">Contact Us</span><h1><br>
          <P style="font-size:18px;color:white">"You’re not just a patient — you’re a story we’re ready to hear. Connect with our experts today"</P>

          <!-- <ul class="list-inline breadcumb-nav">
            <li class="list-inline-item"><a href="home.py" class="text-white">Home</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">Contact Us</a></li>
          </ul> -->
        </div>
      </div>
    </div>
  </div>
</section>
<!-- contact form start -->

<section class="section contact-info pb-0">
    <div class="container">
         <div class="row">
            <div class="col-lg-4 col-sm-6 col-md-6">
                <div class="contact-block mb-4 mb-lg-0">
                    <i class="icofont-live-support"></i>
                    <a href="tel:" ><h5>Call Us</h5></a>
                     +91  9766086582
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-md-6">
                <div class="contact-block mb-4 mb-lg-0">
                    <i class="icofont-support-faq"></i>
                    <a href="mailto:piyapatil@gmail.com"><h5>Email Us</h5></a>
                     contact@mail.com
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-md-6">
                <div class="contact-block mb-4 mb-lg-0">
                    <i class="icofont-location-pin"></i>
                    <a href="#google-map"><h5>Location</h5></a>
                     Ratnagiri , Mahaeashtra , India
                </div>
            </div>
        </div>
    </div>
</section>

<section class="contact-form-wrap section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-6">
                <div class="section-title text-center">
                    <h2 class="text-md mb-2">Contact us</h2>
                    <div class="divider mx-auto my-4"></div>
                    <p class="mb-5" style ="color:black;font-weight:bold;font-size:17px">"Modern audiology. Personalized care. A world of sound waiting for you contact us today."</p>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12 col-md-12 col-sm-12">
                <form id="contact-form" method="post" action="contactbackend.py">
                 <!-- form message -->
                    <div class="row">
                        <div class="col-12">
                            <div class="alert alert-success contact__msg" style="display: none" role="alert">
                                Your message was sent successfully.
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-lg-6">
                            <div class="form-group">
                                <input name="fullname" id="fullname" type="text" class="form-control" placeholder="Your Full Name" class1="form-control" required="">
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="form-group">
                                <input name="email" id="email" type="email" class="form-control" placeholder="Your Email ID" required="">
                            </div>
                        </div>
                         <div class="col-lg-6">
                            <div class="form-group">
                                <input name="phone" id="mobno" type="text"  class="form-control" placeholder="Your Phone No" required="">
                            </div>
                            
                        </div>
                         <div class="col-lg-6">
                            <div class="form-group">
                                <input name="address" id="address" type="text" class="form-control" placeholder="Your Address" required="">
                            </div>
                        </div>
                    </div>

                    <div class="form-group-2 mb-4">
                        <textarea name="message" id="message" class="form-control" rows="8" placeholder="Your Message" required=""></textarea>
                    </div>

                    <div class="text-center">
                        <input class="btn btn-main btn-round-full" name="submit" type="submit" value="Send Messege"></input>
                    </div>
                </form>
            </div>
        </div>
    </div>
</section>


 <div class="google-map">
 
 <iframe src="https://www.google.com/maps/embed?pb=!1m12!1m8!1m3!1d30524.92313265281!2d73.2945022!3d16.9934585!3m2!1i1024!2i768!4f13.1!2m1!1saudiologisy%20diagnostic%20center%20in%20ratnagiri%20maharashtra!5e0!3m2!1sen!2sin!4v1752467626737!5m2!1sen!2sin" width="1700" height="500" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    
</div>

</body>
</html>
''')

import footer