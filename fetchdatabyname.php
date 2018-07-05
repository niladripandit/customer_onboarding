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
$cust_name = $temp3[1];

$query = "SELECT * from CustDetails WHERE CustID = '".$cust_name."'";
$result = mysql_query($query);

while ($row = mysql_fetch_assoc($result)){
	echo "CustID:".$row['Cust_ID'],"";
	echo "CustName:".$row['Cust_Name'],"";
	echo "CustDOB:".$row['Cust_DOB'],"";
	echo "CustStatusCode:".$row['Cust_Status_Code'],"";
	echo "CustGender:".$row['Cust_Gender'],"";
	print("All data fetched succesfully")
?>