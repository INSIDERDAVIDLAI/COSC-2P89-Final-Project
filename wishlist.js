//MR . JIAYANG LAI 6344824 jl17za@brocku.ca BROCKU COSC 2P89


/*loadStates get wishlist array from local storage*/
function loadStates() {
    if (localStorage.getItem('wishList')) {
        wishList = JSON.parse(localStorage.getItem('wishList'));
    } else {
        wishList = [];
    }
    return wishList;
}

function setServerList(list){
    req=new XMLHttpRequest();
    if (this.readyState==4 & this.status==200) {

    }
    req.open("POST","setList.php");
    req.setRequestHeader("Content-Type","applicatio/json");
    req.send(JSON.parse(list));
}

function delServerList(list){
    req=new XMLHttpRequest();
    if (this.readyState==4 & this.status==200) {

    }
    req.open("POST","delList.php");
    req.setRequesHeader("Content-Type","applicatio/json");
    req.send(JSON.parse(list));
}
/*loadList expand array element to the textnode and build a wishlist*/
function loadList() {
    var wishList = loadStates();
    var i;
    for (i = 0; i < wishList.length; i++) {
        if (wishList != null) {
            newElement(wishList[i]);
            console.log(wishList[i]);
        } else {
            alert("NO ITEM");
        }
    }
}

var myList = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myList.length; i++) {
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myList[i].appendChild(span);

}

var close = document.getElementsByClassName("close");
var i;

function newElement(item) {
    var li = document.createElement("li");
    li.classList.add("subitem");
    var t = document.createTextNode(item);
    li.appendChild(t);
    document.getElementById("myUL").appendChild(li);

    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function () {
            var div = this.parentElement;
            var length = div.textContent.length;
            console.log(length);
            var item = div.textContent.substr(0, length - 1);
            console.log(item);
            removeFromList(item);
            div.style.display = "none";
        }
    }

}

function removeFromList(item) {

    if (wishList.includes(item) == false) {
        alert("WARNING! YOUR LOCAL WISHLIST DOES NOT INCLUDE THIS ITEM");
    } else {
        for (i = 0; i < wishList.length; i++) {
            if (wishList[i] == item) {
                wishList.splice(i, 1);
                alert("YOUR LOCAL WISHLIST ITEM REMOVED");

            }
        }
        localStorage.setItem("wishList", JSON.stringify(wishList));
        location.reload();
    }

}

function addToList(item) {

    if (wishList.includes(item) == true) {

        alert("WARNING! DO NOT ADD MULTIPLE SAME PRODUCT");
    } else {
        wishList.push(item);
        alert("ITEM ADDED");
        localStorage.setItem("wishList", JSON.stringify(wishList));
        setServerList(JSON.stringify(wishList));
        newElement(item);
        location.reload();

    }
}

function checkExist(item){
	  
	for (i = 0; i < wishList.length; i++) {
		if (wishList[i]==item){
			return true;
		}
	}
	return false;
}

