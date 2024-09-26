#!/usr/bin/python
from pymongo import MongoClient
import cgi, os, uuid, hashlib #Note os and uuid added

username='jl17za' #Change this!
passwd='6344824' #Change this! 
client=MongoClient('mongodb://'+username+':'+passwd+'@127.0.0.1/'+username) 
db=client[username]

fs=cgi.FieldStorage()
uname=fs.getfirst('user')
spw=fs.getfirst('password')
m=hashlib.md5()
spw=str(spw)
m.update(spw)
pw=m.hexdigest()
def create_session(username):
 sid=uuid.uuid1().hex
 db.users.update_one({'username':username},{'$set':{'usid':sid}})
 print "Set-Cookie: user="+username
 print "Set-Cookie: usid="+sid
 print "Location: granted.php" #The redirect
 print
 exit()


if uname!=None and pw!=None: #If both are exist
	#uname=str(uname)
    #pw=str(pw)
    userinfo = {'username':uname,'passwd':pw}
    rec=db.users.find_one(userinfo)

if rec!=None:
    create_session(uname)
else:
    print "Content-Type: text/html"
    print
    print """<script>document.location="rejected.php";</script>"""
     
    

