from get_request import get_http_request_info
from random import randint
import requests

ipaddress = 'localhost' # this can be changed according to server configuration

cust_name = "Amita"
cust_id = 13567899

print ("The following customer details is going to be fetched: ")
print ("Name :",cust_name)

try:
	url = "http://"+ ipaddress + "/PHP_script/fetchdatabyname.php?"+Cust_Name=cust_name
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
		if (word.find('All data fetched succesfully') != -1):
			print ("Test CAS_010 PASSED ")
		else:
			print ("Test CAS_010 FAILED")
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

