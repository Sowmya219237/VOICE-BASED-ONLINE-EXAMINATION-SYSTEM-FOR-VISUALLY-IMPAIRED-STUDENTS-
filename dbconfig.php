<?php
    $conn = mysqli_connect('localhost','root','','bquiz');
    if($conn){
        //echo "connected";
    }
    else{
        // die("Failed to connect to the server");   
        echo "not connected";
    }
?>