import requests

def getClassFile(url):
	response = requests.post(url,allow_redirects=False, data={
	'action': "detail",
	'class_data[:CLASS_NBR]': "63107",
	'class_data[:STRM]': "2192",
	'binds[:term]': "2192",
	'binds[:reg_status]': "all",
	'binds[:subject]': "CMPE",
	'binds[:catalog_nbr_op]': "=",
	'binds[:instr_name_op]': "=",
	'binds[:crse_units_op]': "=",
	'rec_start': "0",
	'rec_dur': "25"
	})
	return response.content

if __name__ == '__main__':
	url = "https://pisa.ucsc.edu/class_search/index.php"
	response = requests.get(url)

	if response.status_code == 200:
		print("200 OK")
		contents = parseInputs(url)
		file = open("index.html","w")
		file.write(str(contents))

	else:
		printf("Bad Request")
		exit()
