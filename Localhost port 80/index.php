<?php
sleep(3);
$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);

socket_connect($sock, "8.8.8.8", 53);

socket_getsockname($sock, $name); // $name passed by reference



$localAddr = $name;

$me="http://".$localAddr.":5000/login";
$video="http://".$localAddr.":5000/video";
?>

<html> 

   <body>    
  <iframe width="40%" height="80%"

<?php echo "src='$video'>"; ?>

</iframe>		
  
<?php
   echo  "<form action ='$me'  method = 'post'>"; 
     ?>
      <input onmouseover="window.stop();" type = "submit" name="capture" value = "capture" />
     
 </form>       

   </body> 

</html> 
