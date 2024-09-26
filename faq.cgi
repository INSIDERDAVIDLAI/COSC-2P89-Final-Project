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
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="function.js"></script>
<body onload="loadAll()">


<html>
<body>
<center><img src="chip.png" alt="chip" width="40" height="20"></center>"""


print"""
<ul>
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
<center><p>PASSPORT TRADE CENTER FAQ</p></center>

<h1>Q: Can these passports pass Immigration branch or Airport E-Gate?</h1>
<p>A: Think so.</p>
<br>
<h1>Q: How is these passports made? Why you say these passports are real?</h1>>
<p>A: These passports are made by lost/stolen passports and we change the pictues and overwrite the chip.</p>
<br>
<h1>Q: What if I was caught and deported?</h1>
<p>A: Nobody cares.</p>
<br>

</body>

<footer class="site-footer">

<p>COPYRIGHT JIAYANG LAI, ALL RIGHT RESERVED.</p>
<p>Any questions please contact: <a href="mailto:jl17za@brocku.ca">jl17za@brocku.ca</a></p>
<center><img src="lai.png" alt="INSIDERDAVIDLAI"></center>

</footer>"""

print open('form.html','r').read()

print "</html>"