#!/usr/bin/python3 


__version__ = "0.0.1"

try:
	import optparse
	import requests
	from bs4 import BeautifulSoup, Comment
	from termcolor import colored
	import re

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

def parse_all(content):
	parse_comment(content)
	parse_form(content)
	parse_script(content)
	parse_link(content)

def parse_comment(content):

	soup = BeautifulSoup(content, 'html.parser')
	comments = soup.find_all(string=lambda text: isinstance(text, Comment))

	## Show all comments 
	for elements in comments:
		print(elements)
		print()

	print(f"Comment(s) found : {colored(len(comments),'yellow')}")


def parse_script(content):

	# php = re.compile("<\?([//\*\-\+\s|\w\(\)\.,:@<>$?;='\"\\\{\[\]`\}!&^%#]*)\?>")
	soup = BeautifulSoup(content, 'html.parser')
	scripts = soup.find_all("script")
	# result_php = php.search(str(soup))


	## Show all scripts 
	for elements in scripts:
		elements.name = colored(elements.name, "red")
		print(elements.prettify())
		print()

	print(f"Script(s) found : {colored(len(scripts),'yellow')}")

def parse_form(content):

	soup = BeautifulSoup(content, 'html.parser')
	forms = soup.find_all("form")

	## Show all forms
	for elements in forms:
		elements.name = colored(elements.name, "red")
		print(elements.prettify())
		print()

	print(f"Form(s) found : {colored(len(forms),'yellow')}")	

def parse_link(content):
	
	soup = BeautifulSoup(content, 'html.parser')
	links = soup.find_all("a", href=True)

	## Show all links 
	for elements in links:
		if len(elements['href']) > 1: ## Filtring for "#" and "/" links
			print(elements['href'])
	print()
		
	print(f"Link(s) found : {colored(len(links),'yellow')}")

def Main():
	## Menu options
	Menu = optparse.OptionParser(usage='python %prog [options] <url>', version='%prog ' + __version__)
	Menu.add_option("-a", "--all", action="store_true",dest="all",  help="Parse with all options (-c, -s, -f, -l)")
	Menu.add_option("-c", "--comment", action="store_true",dest="comment",  help="Find all comments")
	Menu.add_option("-s", "--script", action="store_true",dest="script", help="Find all scripts")
	Menu.add_option("-f", "--form", action="store_true",dest="form", help="Find all forms")
	Menu.add_option("-l", "--link", action="store_true",dest="link", help="Find all links")
	
	
	(options, args) = Menu.parse_args()

	Examples = optparse.OptionGroup(Menu, "Examples", """python htmlparser.py -a <url>
														 python htmlparser.py -c <url>
                                                         python htmlparser.py -s <url>
														 python htmlparser.py -f <url>
														 python htmlparser.py -l <url>
														 """)													 
	Menu.add_option_group(Examples)

	## For wrong or none arguments
	if len(args) == 0 or options == {'comment':None, 'script':None}:
		Menu.print_help()

	## --all option 
	if options.all == True and len(args) != 0 and len(args) < 2:
		parse_all(GET_request(args[0]))
	elif options.all == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.all == True and len(args) == 0:
		print("\nNo url detected !")

	## --comment option 
	if options.comment == True and len(args) != 0 and len(args) < 2:
		parse_comment(GET_request(args[0]))
	elif options.comment == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.comment == True and len(args) == 0:
		print("\nNo url detected !")

	## --script option
	if options.script == True and len(args) != 0 and len(args) < 2:
		parse_script(GET_request(args[0]))
	elif options.script == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.script == True and len(args) == 0:
		print("\nNo url detected !")

	## --form option
	if options.form == True and len(args) != 0 and len(args) < 2:
		parse_form(GET_request(args[0]))
	elif options.form == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.form == True and len(args) == 0:
		print("\nNo url detected !")

	## --link option
	if options.link == True and len(args) != 0 and len(args) < 2:
		parse_link(GET_request(args[0]))
	elif options.link == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.link == True and len(args) == 0:
		print("\nNo url detected !")

if __name__ == "__main__":
	try:
		Main()
	except KeyboardInterrupt:
		print()
		print("Aborting...")
		print()
