#!/usr/bin/python
from pymongo import MongoClient
import cgi
username='jl17za' #Change this!
passwd='6344824' #Change this!
client=MongoClient('mongodb://'+username+':'+passwd+'@127.0.0.1/'+username)
db=client[username]
print "Content-Type: text/html"
print
print "<html><body>"
print """ 
<link rel="stylesheet" type="text/css" href="style.css">
<meta name="viewport" content="width=device-width, initial-scale=1">"""
#Our script will go here:
fs=cgi.FieldStorage()
if 'passport' in fs:
 course=fs['passport'].value
 #First, let's request the record:
 rec=db.passport.find_one({'code':course})
 #If the code is wrong, we could have None
 if rec==None:
 	print "Ha ha. Nice try.</body></html>"
 	exit()
 #If we're still here, we're good to go!
 print "<h1>"+rec['code']+"</h1>"
 print "<h2>"+rec['title']+"</h2>"
 print "<p>"+rec['desc']+"</p>"
 if len(rec['prereqs'])==0: #Length of prereqs list?
 	print "<div><b>No prerequisites</b></div>"
 else:
 	print "<div><b>Prequisites:</b>"
 	for pr in rec['prereqs']: print pr
else:
 print 'nope'
#Our script ends here!
print "</body></html>"
