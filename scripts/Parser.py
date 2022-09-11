#!/usr/bin/python3

try:
    from bs4 import BeautifulSoup, Comment
    from termcolor import colored
except ModuleNotFoundError as Error:
	print(Error)

def parse_all(content):
	parse_comment(content)
	parse_form(content)
	parse_script(content)
	parse_link(content, False)

def parse_comment(content):

	soup = BeautifulSoup(content, 'html.parser')
	comments = soup.find_all(string=lambda text: isinstance(text, Comment))

	## Show all comments 
	for elements in comments:
		print(elements)
		print()

	print(f"Comment(s) found : {colored(len(comments),'yellow')}")


def parse_script(content):

	soup = BeautifulSoup(content, 'html.parser')
	scripts = soup.find_all("script")

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

def parse_link(content, tree):
	
	all_links = []
	soup = BeautifulSoup(content, 'html.parser')
	links = soup.find_all("a", href=True)
	filtered = 0
	## Show all links 
	for elements in links:
		if len(elements['href']) > 1: ## Filtring for "#" and "/" links
			all_links.append(elements['href'])
			print(elements['href']) if tree == False else None
		else:
			filtered += 1
	if tree:
		return all_links
	else:
		print()
		print(f"Link(s) found : {colored(len(links)-filtered,'yellow')}")