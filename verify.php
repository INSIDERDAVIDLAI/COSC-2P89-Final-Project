#!/usr/bin/php-cgi

<?php
$cookie_loggedin = "yes";
$cookie_notloggedin = "no";
$url="";
if($_POST['user'] == "1" && $_POST['password'] == "1"){
  
  $url="/~jl17za/A4/granted.php";
  setcookie($cookie_loggedin,"yes", time() + (86400 * 30),"/");
// this cookie yes is a global variable and if user is logged in, this cookie will exist.


}else{
 
  $url="/~jl17za/A4/rejected.php";
  setcookie($cookie_notloggedin,"no", time() + (86400 * 30),"/");
} 

header('Location: '.$url);
?>