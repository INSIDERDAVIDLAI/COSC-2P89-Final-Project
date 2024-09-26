#!/usr/bin/php-cgi

<?php
include 'form.html';

?>
<!--AUTHOR JIAYANG LAI  BROCK ID 6344824-->
<link rel="stylesheet" type="text/css" href="style.css">
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>
function guest(){
  window.location.href = "home.cgi";
}
</script>

<center><img src="chip.png" alt="chip" width="40" height="20"></center>
<br>
<center><img src="tor.png" alt="tor" width="400" height="220"></center>
<br>
<body>
<center><p>Use Tor browser to ensure you connection is private and secure,then click the log in button.</p></center>
<center><button onclick="document.getElementById('register').style.display='block'" style="width:auto;">Sign up for new account</button></center>
<center><button onclick="document.getElementById('login').style.display='block'" style="width:auto;">Login with exist account</button></center>
<center><p>Login or Sign up, your choice</p></center>
<center><button style="width:auto;" onclick="guest()">Go to home page directly</button></center>
</body>

<footer class="site-footer">
<center><img src="lai.png" alt="INSIDERDAVIDLAI"></center>
</footer>





</html>