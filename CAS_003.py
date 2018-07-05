from get_request import get_http_request_info
from random import randint
import requests

ipaddress = 'localhost' # this can be changed according to server configuration

cust_id = randint(0, 1000)
cust_name = "Ashok"
cust_dob = 1307
cust_status_code = 3
cust_gender = "M"

print ("The following customer details is going to be added: ")
print ("Name :",cust_name)
print ("ID :",cust_id)
print ("DOB :",cust_dob)
print ("Status Code :",cust_status_code)
print ("Gender :",cust_gender)

if(len(str(cust_dob))<8):
	print("Invalid DOB entered")
	print ("Test CAS_003 PASSED ")
else:
	print ("Test CAS_003 FAILED")
