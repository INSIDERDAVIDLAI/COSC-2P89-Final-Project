#!/usr/bin/python
from pymongo import MongoClient
import cgi, os, uuid #Note os and uuid added
username='jl17za' #Change this!
passwd='6344824' #Change this!
client=MongoClient('mongodb://'+username+':'+passwd+'@127.0.0.1/'+username)
db=client[username]
print "Content-Type: text/html"
print
print "<html><body>"
print """ 
<link rel="stylesheet" type="text/css" href="../style.css">
<meta name="viewport" content="width=device-width, initial-scale=1">"""
print"""
<html>
<script src="../function.js"></script>
<body onload="loadAll()">
<center><img src="../chip.png" alt="chip" width="40" height="20"></center>"""
#This is what we show when the user did something wrong
#It has an early termination, for simplicity's sake
def errornope():
 print "Content-Type: text/html"
 print
 print "<html><head><title>Bad!</title></head><body>"
 print """<script>
document.location="../failed2.php";
</script>"""
 print "</body></html>"
 exit()

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

fs=cgi.FieldStorage()
pid=fs.getfirst('pid')
pname=fs.getfirst('pname')
pimg=fs.getfirst('pimg')
pdesc=fs.getfirst('pdesc')
pPrice=fs.getfirst('pPrice')
tag=fs.getfirst('tag')
if check_admin():

	if pid!=None and pname!=None and pimg!=None and pdesc!=None and pPrice!=None and tag!=None :
		rec=db.products.find_one({"pid":pid})
		if rec==None:
			db.products.insert_one({"pid":pid,"pname":pname,"pimg":pimg,"pdesc":pdesc,"pPrice":pPrice,"tag":tag})
			print """<script>document.location="../success2.php";</script>"""
		else:
			errornope()

	else:
		errornope()

else:
	print "<center><p>FORBIDDEN/PROTECTED AREA</p></center>"
	print "<center><img src='../denied.png' alt='denied' width='60' height='60'></center>"
	print "<center><p>You don't have permission to access this site</p></center>"
	print "<center><p>Only administrator have access to view this page, check your identity</p></center>"
	print "<center><img src='../lai.png' ></center>"

