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
<link rel="stylesheet" type="text/css" href="style.css">
<meta name="viewport" content="width=device-width, initial-scale=1">"""
print"""
<html>
<script src="function.js"></script>
<script src="wishlist.js"></script>
<body onload="loadAnything()">
<script>
function loadAnything(){
	loadAll();
	loadStates();
}
</script>
<center><img src="chip.png" alt="chip" width="40" height="20"></center>"""
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
	
if check_logged_in():

	username=check_logged_in()
	fs=cgi.FieldStorage()
	pname=fs.getfirst('pname')
	rec=db.users.find_one({"username":username})
	if pname in rec['wishlist']:
		print """<script>document.location="wishlist.cgi";</script>"""
	else:	
		db.users.update_one({'username':username},{'$push':{"wishlist":pname}})
		print """<script>document.location="wishlist.cgi";</script>"""


else:
	print"""<center><p>Log in for further action</p></center>"""