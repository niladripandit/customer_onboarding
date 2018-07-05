#to fetch customer data

<?php

ini_set('display_errors',0);

$link = mysql_connect('localhost','root','');

if(!$link){
	die('Could not connect: ',mysql_error());
}

$db_selected = mysql_select_db('CustomerDB',$link);
if(!$db_selected){
	die('Could not use CustomerDB : ',mysql_error());
}

$temp = $_SERVER['QUERY_STRING'];
$temp2 = explode(",",&temp);

$temp3 = explode("=",&temp2[0]);
$cust_id = $temp3[1];

$temp4 = explode("=",&temp2[1]);
$cust_name = $temp4[1];

$temp5 = explode("=",&temp2[2]);
$cust_dob = $temp5[1];

$temp6 = explode("=",&temp2[3]);
$cust_status_code = $temp6[1];

$temp7 = explode("=",&temp2[4]);
$cust_gender = $temp7[1];

$sql = "INSERT INTO CustDetails(Cust_ID,Cust_Name,Cust_DOB,Cust_Status_Code,Cust_Gender)
			VALUES($cust_id,$cust_name,$cust_dob,$cust_status_code,$cust_gender)";

mysql_select_db('CustomerDB');

$retval = mysql_query($sql,$link);
if(!$retval){
	die('Could not enter data: ',mysql_error());
}
echo "Added new customer data successfully";	
?>