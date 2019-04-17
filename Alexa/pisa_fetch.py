import os
import requests

def status():
	if response.status_code == 200:
		print("200 OK")
		parseInputs()
	
	else:
		print("Bad Request")
		exit()

def parseInputs():
	response = requests.post(url,allow_redirects=False, data={
	'action': "detail",
	'class_data[:STRM]': "2192",
	'class_data[:CLASS_NBR]': "63107",
	'binds[:term]': "2192",
	'binds[:reg_status]': "all",
	'binds[:subject]': "CMPE"
	})


if __name__ == "__main__":
	url = "https://pisa.ucsc.edu/class_search/index.php"
	response = requests.get(url)
	status()
	json_response = response.json()

	print(response.content)