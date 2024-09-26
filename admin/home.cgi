#!/usr/bin/python
from pymongo import MongoClient
import cgi, os, uuid #Note os and uuid added
username='jl17za' #Change this!
passwd='6344824' #Change this!
client=MongoClient('mongodb://'+username+':'+passwd+'@127.0.0.1/'+username)
db=client[username]

#This is what we show when the user did something wrong
#It has an early termination, for simplicity's sake
def errornope():
 print "Content-Type: text/html"
 print
 print "<html><head><title>Bad!</title></head><body>"
 print """<script>
document.location="../rejected.php";
</script>"""
 print "</body></html>"
 exit()

#If the user is successfully logging in, we need to create a new
#session id, put that into the database (under the correct user),
#and pass the same session id to the user via cookie
#Finally, redirect back to the original page
def create_session(username):
 sid=uuid.uuid1().hex
 db.users.update_one({'username':username},{'$set':{'usid':sid}})
 print "Set-Cookie: user="+username
 print "Set-Cookie: usid="+sid
 print "Location: ./home.cgi" #The redirect
 print
 exit()

#Used to determine if we're currently logged in
#If so, returns the username (just makes something else easier)
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

#Signing out is simple: remove the database's session id for this user
#If it doesn't exist, a cookie can't match it!
def actually_sign_out(username):
 db.users.update_one({'username':username},{'$unset':{'usid':''}})
 print "Location: ./home.cgi"

#What the 'login' box looks like when you're already logged in
def signoutbox():
 return "<a href='home.cgi?logout=yes'>Sign out</a>"

#Yes, this is a little messy
#When we *would* build the login box, we first check if it's even necessary
# to do so.
#It's mostly only the function's name that's odd (and even then, only
# because it determines what to put into the login box)
def userbox():
 #First, we'll check for posted 'login' form data:
 fs=cgi.FieldStorage()
 uname=fs.getfirst('uname')
 pw=fs.getfirst('passwd')
 if uname!=None and pw!=None: #If both have been provided...
 	uname=str(uname); pw=str(pw)
 	rec=db.users.find_one({'username':uname,'passwd':pw})
 	if rec==None: #If the provided credentials aren't valid...
 		errornope() #Present some sort of 'login failed'
 	else: #Actually worked!
 		create_session(uname)
 #We don't need an 'else', because both the above exit()
 #
 #Next, we check for the session cookie:
 user=check_logged_in() #If we're logged in, we'll also get the name back
 if user: #If we weren't logged in, it'd be None, which fails here
 	#If we're logged in, we're either using normally, or logging out
 	if fs.getfirst('logout')!=None: #If we're trying to log out...
 		actually_sign_out(user)
 	else:
 		return signoutbox()
 box="""<form action='#' method='post'>
 Username: <input type='text' name='uname'/><br/>
 Password: <input type='password' name='passwd'/>
 <br/><input type='submit' value='Sign in'/>
 </form>""" #The actual login box!
 return box
ub=userbox() #We these considerations before starting the header

print "Content-Type: text/html"
print

print """<html><head>
<style>
#user{float:right; border:1px solid black;padding:10px;text-align:right;}
</style></head><body>"""
print "<link rel='stylesheet' type='text/css' href='/~jl17za/A4/style.css'>"
print "<div id='user'>"+ub+"</div>"
print "<h1>Welcome!</h1>"
print "<p>This is just a placeholder page.</p>"
print "<p>Even when it's done, it'll simply have one of two states:</p>"
print "<ol><li>Logged out, showing fields for logging in</li>"
print "<li>Logged in, showing a link to log out</li></ol>"
print "</body></html>"