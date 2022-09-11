#!/usr/bin/python3

try:
    import requests
except ModuleNotFoundError as Error:
	print(Error)

def GET_request(url):
	## Send GET request to the website and retrieve the answer
	try:
		page_content = requests.get(url)
		return page_content.text
		
	except requests.ConnectionError as Error:
		print(Error)

	except requests.ConnectTimeout as Error:
	    print(Error)