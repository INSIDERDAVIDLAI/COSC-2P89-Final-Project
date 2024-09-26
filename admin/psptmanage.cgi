#!/usr/bin/python
from pymongo import MongoClient
import cgi, os, uuid #Note os and uuid added
username='jl17za' #Change this!
passwd='6344824' #Change this! 
client=MongoClient('mongodb://'+username+':'+passwd+'@127.0.0.1/'+username) 
db=client[username]
print "Content-Type: text/html"
print
print """ 
<link rel="stylesheet" type="text/css" href="../style.css">
<meta name="viewport" content="width=device-width, initial-scale=1">"""
print"""
<html>
<script src="../function.js"></script>
<body onload="loadAll()">
<center><img src="../chip.png" alt="chip" width="40" height="20"></center>"""
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

#def change_admin():
	#user=check_admin()
	#rec=db.users.find_one({'username':user})

	#if rec['admin']=='Y':
		#db.users.update_one({'username':user},{"$set":{"admin":"N"}})
	#else:
		#db.users.update_one({'username':user},{"$set":{"admin":"Y"}})

if check_admin():
	numProduct=db.products.count()
	allProduct=db.products.find()
	#rec=db.products.find_one({'pid':products})
	
	print """<ul>
				<li><a href="../home.cgi">Back to home</a></li>
				<li style="float:right"><a id="change" onclick="setTheme()">Change theme</a></li>
			</ul>"""
	print "<center><p>WEBSITE PRODUCT CONTORL AND PROTECTION</p></center>"
	print "<center><p>Total number of passports: "+str(numProduct)+"</p></center>"
	print "<a href='../post.html'><button>Post New Product</button></a>"
	for aProduct in allProduct:
		print "<p>Passport id: <b>"+aProduct['pid']+"</b><br>Passport name: <b>"+aProduct['pname']+"</b></p>" 
		print "<a href='delete_product.cgi?delete="+aProduct['pid']+"'><button>Delete Product</button></a>"
			
else:
	print "<center><p>FORBIDDEN/PROTECTED AREA</p></center>"
	print "<center><img src='../denied.png' alt='denied' width='60' height='60'></center>"
	print "<center><p>You don't have permission to access this site</p></center>"
	print "<center><p>Only administrator have access to view this page, check your identity</p></center>"
	print "<center><img src='../lai.png' ></center>"

#def cencel_admin():
#db.users.update_one({'username':user},{"$set":{"admin":"N"}})
	

#def set_admin():
#db.users.update_one({'username':user},{"$set":{"admin":"Y"}})
	
