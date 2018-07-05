import requests
ipaddress = 'localhost' # this can be changed according to server configuration

def get_http_request_info(url):

	try:
		url = "http://"+ ipaddress + "/nil/addnewcustdetails.php"
		print (url)
		r = requests.get(url)
		#if ( int(r.status_code) == 200):
		#    print("if loop print 200 OK")
		if ( int(r.status_code) == 100):
			print("The client should proceed to send the request body")
		elif( int(r.status_code) == 101):
			print("The requester has asked the server to switch protocols")
		elif( int(r.status_code) == 200):
			print("Standard response for successful HTTP requests")
			#print(r.text)
			with open('body.txt','w') as fp:
				for line in r.text:
					fp.write(line)
			print(r.json)
		elif( int(r.status_code) == 300):
			print("Indicates multiple options for the resource from which the client may choose")
		elif( int(r.status_code) == 400):
			print("The server cannot or will not process the request due to an apparent client error")
		elif( int(r.status_code) == 500):
			print("A generic error message, given when an unexpected condition was encountered")
		else: 
			print("Something wrong happened :)")
		#return r
	except requests.ConnectionError:
		print("Failed to connect")
	