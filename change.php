
#!/usr/bin/php-cgi

<?php
function changeList(){
$myfile = fopen("wishlist.list", "w") or die("Unable to open file!");
$txt = "Trash\n";
fwrite($myfile, $txt);
$txt = "Grabage\n";
fwrite($myfile, $txt);
fclose($myfile);
}
?>
