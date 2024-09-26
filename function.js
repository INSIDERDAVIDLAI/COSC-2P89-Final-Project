
var theme = localStorage.getItem('theme');

function setTheme(){
    var theme = localStorage.getItem('theme');
    if(theme === 'gold'){ 
      document.body.style.backgroundColor = "black";
      localStorage.setItem("theme", "default");
      
    }else{  
      document.body.style.backgroundColor = "gold";
      localStorage.setItem("theme", "gold");
      
    }  
  }
    
function setGold(){
  document.body.style.backgroundColor = "gold";
  localStorage.setItem("theme", "gold");
}
function setDefault(){
    
    document.body.style.backgroundColor = "black";
    localStorage.setItem("theme", "default");

  }

  function check(){

    if(theme === 'gold'){ 
      setGold();
      
    }else{  
      setDefault();
    }  
  }
  function loadAll(){
    loginbtn();
    check();
  }

function getCookie(name) {
  var name = name + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return null;
}

function loginbtn(){
	if(getCookie("+user")==null){
		
	}else{
    var loginbtn= document.getElementById("loginbtn");
    loginbtn.innerHTML="Log Out";
    loginbtn.onclick=function(){
      logout();
    };
	};
};

function logout(){
    deleteCookie("yes");
    location.reload();
    
};

  function deleteCookie(name) {
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  };

function checkLogin(){
    var login = getCookie("yes");
    if(!isset($_COOKIE['yes'])){
        return true;
    }else{
        return false;
    }
  }
