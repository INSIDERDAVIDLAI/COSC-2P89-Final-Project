#!/usr/bin/python
from pymongo import MongoClient
import cgi, os, uuid, hashlib #Note os and uuid added

username='jl17za' #Change this!
passwd='6344824' #Change this! 
client=MongoClient('mongodb://'+username+':'+passwd+'@127.0.0.1/'+username) 
db=client[username]
print "Content-Type: text/html"
print
fs=cgi.FieldStorage()
uname=fs.getfirst('user')
answer=fs.getfirst('answer')
spw=fs.getfirst('password')
m=hashlib.md5()
spw=str(spw)
m.update(spw)
pw=m.hexdigest()
if uname!=None and answer!=None: #If both are filled
	
    userinfo = {{"username":uname},{"answer":answer}}
    find = db.users.find_one(userinfo)

    if find!=None:
        print """<script>document.location="../signed.cgi";</script>"""

    else:
        #Override redirect to enter new password page.
        #Override
        #Override
        db.users.update_one({{'username':username},{'passwd':pw}})
        #rec=db.users.insert_one({"username":uname,"passwd":pw,"admin":"N","wishlist":[],"answer":answer}) 
        
        print """
        <link rel="stylesheet" type="text/css" href="../style.css">

        <meta name="viewport" content="width=device-width, initial-scale=1">
        <html>
        <center><img src="../chip.png" alt="chip" width="40" height="20"></center>
        <br>
        <center><img src="../done.png" alt="Done" width="248" height="344"></center>
        <br>
        <center><p>ACCOUNT SUCCESSFULLY REGISTERED</p></center>
        <center><a href="/~jl17za/A4/index.php"><button style="width:auto;">GO BACK TO MAIN PAGE AND LOG IN</button></a></center>
        <footer class="site-footer">

        <center><img src="../lai.png" alt="INSIDERDAVIDLAI"></center>
        </footer>
        </html>"""
    
