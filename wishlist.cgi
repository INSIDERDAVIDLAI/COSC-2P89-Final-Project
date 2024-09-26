#!/usr/bin/python

from pymongo import MongoClient
import cgi, os, uuid #Note os and uuid added
username='jl17za' #Change this!
passwd='6344824' #Change this!
client=MongoClient('mongodb://'+username+':'+passwd+'@127.0.0.1/'+username)
db=client[username]
def check_logged_in():
 if os.environ.has_key('HTTP_COOKIE'):
 	user=None #Assume doesn't exist
 	usid=None # until proven otherwise
 	cookies=os.environ['HTTP_COOKIE'].split(';')
 	for cookie in cookies:
 		if cookie.split('=')[0].strip()=='user':
 			user=cookie[cookie.find('=')+1:] #Is this one understandable?
 		elif cookie.split('=')[0].strip()=='usid':
 			usid=cookie[cookie.find('=')+1:]
 	if user and usid: #If we have cookies for a username/sesionid
 		rec=db.users.find_one({'username':user,'usid':usid})
 		if rec!=None: #If the database records match the user
 			return user #I know, a little weird to not return True
 return None

def check_admin():
 if os.environ.has_key('HTTP_COOKIE'):
 	user=None #Assume doesn't exist
 	usid=None # until proven otherwise
 	cookies=os.environ['HTTP_COOKIE'].split(';')
 	for cookie in cookies:
 		if cookie.split('=')[0].strip()=='user':
 			user=cookie[cookie.find('=')+1:] #Is this one understandable?
 		elif cookie.split('=')[0].strip()=='usid':
 			usid=cookie[cookie.find('=')+1:]
 	if user and usid: #If we have cookies for a username/sesionid
 		rec=db.users.find_one({'username':user,'usid':usid})
 		if rec!=None: #If the database records match the user
 			if rec['admin']=='Y':
				return user
 return None
print"""
<!--AUTHOR JIAYANG LAI  BROCK ID 6344824-->
<link rel="stylesheet" type="text/css" href="style.css">
<link rel="stylesheet" type="text/css" href="print.css" media="print">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="function.js"></script>
<script src="wishlist.js"></script>
<body onload="loadAnything()">
<script>
function loadAnything(){
	loadAll();
	loadList();
}
</script>

<html>
<body>
<center><img src="chip.png" alt="chip" width="40" height="20"></center>"""

print"""
<ul id="nav">
<li><a href="home.cgi">Home</a></li>
<li><a href="product.cgi">Product</a></li>
<li><a href="wishlist.cgi">Wishlist</a></li>
<li><a href="faq.cgi">FAQ</a></li>
<li><a href="contact.cgi">Contact</a></li>
<li><a href="about.cgi">About</a></li>"""
if check_admin():
  print """<li style="float:right"><a class="active" href="admin/usrmanage.cgi">User Manage</a></li>"""
  print """<li style="float:right"><a class="active" href="admin/psptmanage.cgi">Product Manage</a></li>"""
if check_logged_in()==None:
  print """<li style="float:right"><a class="active" id="signupbtn" onclick="document.getElementById('register').style.display='block'">Sign Up</a></li>
  <li style="float:right"><a class="active" id="loginbtn" onclick="document.getElementById('login').style.display='block'">Login</a></li>"""
else: 
  print """<li style="float:right"><a href='admin/logout.cgi?name="""+check_logged_in()+"""'>Log Out</a></li>"""

print """<li style="float:right"><a id="change" onclick="setTheme()">Change theme</a></li>
</ul>"""

print"""
<div id="myDIV" class="header" align="center">
  <p>Items in your Wishlist</p>"""
if check_logged_in():
  		username=check_logged_in()
		fs=cgi.FieldStorage()
		pname=fs.getfirst('pname')
		rec=db.users.find_one({"username":username})

		if rec['wishlist']==None:
			print"""<span>YOUR WISHLIST IS EMPTY</span>"""
		else:
			for pname in rec['wishlist']:
				print"""<div id="wishlist">""""<p>"+pname+"</p></div>"
				#print"""<center><a href="poplist.cgi?pname="""+rec['pname']+""""><button onclick="removeFromList(\'"""+rec['pname']+"""')" style="width:20%;">Remove from Wishlist</button></a></center>"""
		print"""<button onclick="window.print();">Print your wishlist as PDF and Share your Wishlist</button>
<p>VIEW MODE ENABLED! YOU CAN ONLY REMOVE PRODUCTS FROM HERE!</p>
</div>"""


else:
	print"""<p>WISHLIST UNAVALIABLE: YOU ARE NOT LOGGED IN</p>"""

print"""
<ul id="myUL"></ul>

<footer class="site-footer">

<p>COPYRIGHT JIAYANG LAI, ALL RIGHT RESERVED.</p>
<p>Any questions please contact: <a href="mailto:jl17za@brocku.ca">jl17za@brocku.ca</a></p>
<center><img src="lai.png" alt="INSIDERDAVIDLAI"></center>

</footer>"""

print open('form.html','r').read()

print "</html>"