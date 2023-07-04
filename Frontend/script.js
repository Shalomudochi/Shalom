function validateForm() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
  
    // Validate the email and password
    if (email === "gabriel@gmail.com" && password === "password") {
      // Successful login, redirect to the dashboard
      window.location.href = "dashboard.html";
      return false;
    } else {
      // Display error message
      document.getElementById("error").innerHTML = "Invalid credentials";
      return false;
    }
  }
  
  function logout() {
    // Redirect to the login page after signing out
    window.location.href = "login.html";
  }
  