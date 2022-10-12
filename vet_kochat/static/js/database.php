<?php

$host = "aai-rds.cicyr4glvvx9.ap-northeast-2.rds.amazonaws.com";
$user =  "admin";
$pass = "abcd1234";
$databaseName = "aai";
$tableName = "predict_diagnosis";
$port = "3306"
$con = mysql_connect($host,$user,$pass,$databaseName);

?>