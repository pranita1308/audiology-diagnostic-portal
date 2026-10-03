#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()

#print('''
 #     <script>
   #    var username = localStorage.getItem("User_Name");
    #   if (username === null || username === "") {
     #      alert("Login first");
      #     window.location.href = "login.py";
       #}
      #</script>''')

print("Content-Type: text/html\n")

homehtml = '''<header>
	<div class="header-top-bar">
		<div class="container">
			<div class="row align-items-center">
				<div class="col-lg-6">
					<ul class="top-bar-info list-inline-item pl-0 mb-0">
						<li class="list-inline-item"><a href="mailto:piyapatil@gmail.com"><i class="icofont-support-faq mr-2"></i>support@medico.com</a></li>
						<li class="list-inline-item"><a href="contact.py"><i class="icofont-location-pin mr-2"></i>Address :-Ratnagiri , Maharashtra ,India</li></a>
					</ul>
				</div>
				<div class="col-lg-6">
					<div class="text-lg-right top-right-bar mt-2 mt-lg-0">
						<a href="tel:" >
							<span>Call Now : </span>
							<span class="h6">9766086582</span>
						</a>
					</div>
				</div>
			</div>
		</div>
	</div>
	<nav class="navbar navbar-expand-lg navigation" id="navbar">
		<div class="container">
		 	 <a class="navbar-brand" href="home.py">
			  	<img src="images/medico.png" alt="" class="img-fluid" style="height:50px;width:180px">
			  </a>

		  	<button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#navbarmain" aria-controls="navbarmain" aria-expanded="false" aria-label="Toggle navigation">
			<span class="icofont-navigation-menu"></span>
		  </button>
	  
		  <div class="collapse navbar-collapse" id="navbarmain">
			<ul class="navbar-nav ml-auto">
			  <li class="nav-item active">
				<a class="nav-link" href="home.py">Home</a>
			  </li>
			   <li class="nav-item"><a class="nav-link" href="about.py">About</a></li>


                <li class="nav-item dropdown">
					<a class="nav-link dropdown-toggle" href="service.py" id="dropdown05" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Services <i class="icofont-thin-down"></i></a>
					<ul class="dropdown-menu" aria-labelledby="dropdown05">
						<li><a class="dropdown-item" href="service.py">Our Services</a></li>
                        <li><a class="dropdown-item" href="blog-sidebar.py">Blog with Sidebar</a></li>
						<li><a class="dropdown-item" href="blog-single.py">Blog Single</a></li>
					</ul>
			  	</li>
			    

			    <li class="nav-item dropdown">
					<a class="nav-link dropdown-toggle" href="department.py" id="dropdown02" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Department <i class="icofont-thin-down"></i></a>
					<ul class="dropdown-menu" aria-labelledby="dropdown02">
						<li><a class="dropdown-item" href="department.py">Departments</a></li>
						<li><a class="dropdown-item" href="department-single.py">Department Single</a></li>
					</ul>
			  	</li>

			  	<li class="nav-item dropdown">
					<a class="nav-link dropdown-toggle" href="doctor.py" id="dropdown03" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Doctors <i class="icofont-thin-down"></i></a>
					<ul class="dropdown-menu" aria-labelledby="dropdown03">
						<li><a class="dropdown-item" href="doctor.py">Doctors</a></li>
						<li><a class="dropdown-item" href="doctor-single.py">Doctor Single</a></li>
						<li><a class="dropdown-item" href="appoinment.py">Appoinment</a></li>
                        <li><a class="dropdown-item" href="questions.py">Test</a></li>
					</ul>
			  	</li>
				
                <li class="nav-item"><a class="nav-link" href="contact.py">Contact</a></li>

                <li class="nav-item" style="background-color: rgb(223, 45, 45); color:white; border-radius:50px; margin-right:5px">
                    <a class="nav-link" href="" data-toggle="modal" aria-pressed="false" data-target="#exampleModal">Login/Register</a>
                </li>

			</ul>
		  </div>
		</div>
	</nav>
</header>

<!-- Login Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Login</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form action="loginbackend.py" method="post">
                    <div class="form-group">
                        <label for="user_name" class="col-form-label">Username</label>
                        <input type="text" class="form-control" placeholder="Email" name="user_name" id="user_name" required="">
                    </div>
                    <div class="form-group">
                        <label for="user_psw" class="col-form-label">Password</label>
                        <input type="password" class="form-control" placeholder="Password" name="user_psw" id="user_psw" required="">
                    </div>
                    <div class="right-w3l">
                        <input type="submit" class="form-control serv_bottom" style="background-color: rgb(223, 45, 45); color:white;" value="Login">
                    </div>
                    <div class="row sub-w3l my-3">
                        <div class="col sub-agile">
                            <input type="checkbox" id="brand1" value="">
                            <label for="brand1" class="text-secondary">
                                <span></span>Remember me?
                            </label>
                        </div>
                        <div class="col forgot-w3l text-right">
                            <a href="#" class="text-secondary">Forgot Password?</a>
                        </div>
                    </div>
                    <p class="text-center text-secondary">Don't have an account?
                        <a href="#" data-toggle="modal" data-target="#exampleModal1" class="text-dark font-weight-bold">Register Now</a>
                    </p>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Register Modal -->
<div class="modal fade" id="exampleModal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel1" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel1">Register</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form action="registerbackend.py" method="post">
                    <div class="form-group">
                        <label for="name" class="col-form-label">Name</label>
                        <input type="text" class="form-control" name="name" id="name" required="">
                    </div>
                    <div class="form-group">
                        <label for="email" class="col-form-label">Email</label>
                        <input type="email" class="form-control" name="email" id="email" required="">
                    </div>
                    <div class="form-group">
                        <label for="password" class="col-form-label">Password</label>
                        <input type="password" class="form-control" name="password" id="password" required="">
                    </div>
                    <div class="form-group">
                        <label for="cpassword" class="col-form-label">Confirm Password</label>
                        <input type="password" class="form-control" name="cpassword" id="cpassword" required="">
                    </div>
                    <div class="sub-w3l">
                        <div class="sub-agile">
                            <input type="checkbox" id="brand2" value="">
                            <label for="brand2" class="mb-3">
                                <span></span>I Accept the Terms & Conditions
                            </label>
                        </div>
                    </div>
                    <div class="right-w3l">
                        <input type="submit" class="form-control serv_bottom" style="background-color: rgb(223, 45, 45); color:white;" value="Register">
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

'''
