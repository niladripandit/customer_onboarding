from get_request import get_http_request_info
from random import randint
import requests

ipaddress = 'localhost' # this can be changed according to server configuration

cust_id = randint(0, 1000)
cust_name = "Ellie"
cust_dob = 13071877
cust_status_code = 3
cust_gender = "F"
extra_string = "this string is of no use"

print ("The following customer details is going to be added: ")
print ("Name :",cust_name)
print ("ID :",cust_id)
print ("DOB :",cust_dob)
print ("Status Code :",cust_status_code)
print ("Gender :",cust_gender)

cust_info = 'cust_id'+'='+str(cust_id)+',cust_name'+'='+cust_name+',cust_dob'+'='+str(cust_dob)+',cust_status_code'+'='+str(cust_status_code)+',cust_gender'+'='+ cust_gender+extra_string

try:
	url = "http://"+ ipaddress + "/PHP_script/addnewcustdetails.php?"+cust_info
	print (url)
	r = requests.get(url)
	
	if ( int(r.status_code) == 100):
		print("The client should proceed to send the request body")
	elif( int(r.status_code) == 101):
		print("The requester has asked the server to switch protocols")
	elif( int(r.status_code) == 200):
		print("Standard response for successful HTTP requests")
		#print(r.text)
		#print(r.json)
		word = r.text
		if (word.find('Could not enter data') != -1):
			print ("Test CAS_004 FAILED ")
		else:
			print ("Test CAS_004 PASSED")
	elif( int(r.status_code) == 300):
		print("Indicates multiple options for the resource from which the client may choose")
	elif( int(r.status_code) == 400):
		print("The server cannot or will not process the request due to an apparent client error")
	elif( int(r.status_code) == 500):
		print("A generic error message, given when an unexpected condition was encountered")
	else: 
		print("Something wrong happened :)")
except requests.ConnectionError:
	print("Failed to connect")

