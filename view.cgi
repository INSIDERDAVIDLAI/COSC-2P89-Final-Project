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
fs=cgi.FieldStorage()
pid=fs.getfirst('pid')
if pid!=None:
	rec=db.products.find_one({"pid":pid})
	if rec!=None:
		print """<ul>
					<li><a href="product.cgi">Back to Product Page</a></li>
					<li style="float:right"><a id="change" onclick="setTheme()">Change theme</a></li>
				</ul>""" 	
		print """<center><img id="image2" class="imgcontainer" src=\""""+rec['pimg']+"""\" width="200" height="280"></center>"""
		print """<center><p>"""+rec['pname']+"""</p></center>"""
		print """<center><p>"""+rec['pdesc']+"""</p></center>"""
		print """<center><p>"""+rec['pPrice']+"""</p></center>"""
		print """<center><a href="setlist.cgi?pname="""+rec['pname']+""""><button onclick="addToList(\'"""+rec['pname']+"""')" style="width:20%;">Add to Wishlist</button></a></center>"""
		print """<center><a href="poplist.cgi?pname="""+rec['pname']+""""><button onclick="removeFromList(\'"""+rec['pname']+"""')" style="width:20%;">Remove from Wishlist</button></a></center>"""
		print "</body></html>"
	else:
		print """<ul>
					<li><a href="product.cgi">Back to Product Page</a></li>
					<li style="float:right"><a id="change" onclick="setTheme()">Change theme</a></li>
				</ul>""" 	
		print """<center><img src="lbnpspt.png" id="image2" class="imgcontainer" width="200" height="280"></center>"""
		print """<center><p>SPECIAL PASSPORT SALE</p></center>"""
		print """<center><p>Lebanon diplomatic passport</p></center>"""
		print """<center><p>Enjoy diplomatic privalige</p></center>"""
		print """<center><p>$10000</p></center>"""
		print """<center><button style="width:20%;">Sold Out</button></center>"""
		print "</body></html>"

else:
	print """<script>document.location="failed4.php";</script>"""
	



print """ <footer class="site-footer">

<p>COPYRIGHT JIAYANG LAI, ALL RIGHT RESERVED.</p>
<p>Any questions please contact: <a href="mailto:jl17za@brocku.ca">jl17za@brocku.ca</a></p>
<center><img src="lai.png" alt="INSIDERDAVIDLAI"></center>

</footer>"""
