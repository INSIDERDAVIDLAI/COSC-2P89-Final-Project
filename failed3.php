#!/usr/bin/php-cgi

<!--AUTHOR JIAYANG LAI  BROCK ID 6344824-->
<link rel="stylesheet" type="text/css" href="style.css">
<body onload="count()"></body>
<meta name="viewport" content="width=device-width, initial-scale=1">


<script>
    var time = 2;
    function count(){     
        if(time<0){
            window.location = "/~jl17za/A4/product.cgi";
        }else{
            document.getElementById("count").innerHTML = time ; 
            window.setTimeout("count()", 1000);
        }
        time = time - 1;
    }

</script>
<html>
<center><img src="chip.png" alt="chip" width="40" height="20"></center>

<br>
<br>
<br>
<br>
<center><img src="failed.png" width="280" height="280"></center>
<center><p>Wishlist update failed</p></center>
<center><p>For all to wishlist error:Your wishlist may already included this item</p></center>
<center><p>For remove wishlist error:Your wishlist may not included this item</p></center>
<center><p>You will be redirected within <span id="count"> 2 </span> seconds...</p></center>

<footer class="site-footer">

<center><img src="lai.png" alt="INSIDERDAVIDLAI"></center>
</footer>
</html>
