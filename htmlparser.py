#!/usr/bin/python3 


__description__ = "This tool is used to analyze the source code of an html page by recovering tags and comments"
__version__ = "1.5.0"
__author__ = "Anataar"


try:
	import optparse
	from scripts import MakeTree, Parser, Request

except ModuleNotFoundError as Error:
	print(Error)


def Main():
	## Menu options
	Menu = optparse.OptionParser(usage='python %prog [options] <url>', version='%prog ' + __version__)
	Menu.add_option("-a", "--all", action="store_true",dest="all",  help="Parse with all options (-c, -s, -f, -l)")
	Menu.add_option("-c", "--comment", action="store_true",dest="comment",  help="Find all comments")
	Menu.add_option("-s", "--script", action="store_true",dest="script", help="Find all scripts")
	Menu.add_option("-f", "--form", action="store_true",dest="form", help="Find all forms")
	Menu.add_option("-l", "--link", action="store_true",dest="link", help="Find all links")
	Menu.add_option("-t", "--tree", action="store_true",dest="tree", help="Make a tree of the website directories")
	
	
	(options, args) = Menu.parse_args()

	Examples = optparse.OptionGroup(Menu, "Examples", """python htmlparser.py -a <url>
														 python htmlparser.py -c <url>
                                                         python htmlparser.py -s <url>
														 python htmlparser.py -f <url>
														 python htmlparser.py -l <url>
														 python htmlparser.py -t <url>
														 """)													 
	Menu.add_option_group(Examples)

	## For wrong or none arguments
	if len(args) == 0 or options == {'all':None, 'comment':None, 'script':None, 'form':None, 'link':None, 'tree':None}:
		Menu.print_help()
		print("\n" +__description__)

	## --all option 
	if options.all == True and len(args) != 0 and len(args) < 2:
		Parser.parse_all(Request.GET_request(args[0]))
	elif options.all == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.all == True and len(args) == 0:
		print("\nNo url detected !")

	## --comment option 
	if options.comment == True and len(args) != 0 and len(args) < 2:
		Parser.parse_comment(Request.GET_request(args[0]))
	elif options.comment == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.comment == True and len(args) == 0:
		print("\nNo url detected !")

	## --script option
	if options.script == True and len(args) != 0 and len(args) < 2:
		Parser.parse_script(Request.GET_request(args[0]))
	elif options.script == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.script == True and len(args) == 0:
		print("\nNo url detected !")

	## --form option
	if options.form == True and len(args) != 0 and len(args) < 2:
		Parser.parse_form(Request.GET_request(args[0]))
	elif options.form == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.form == True and len(args) == 0:
		print("\nNo url detected !")

	## --link option
	if options.link == True and len(args) != 0 and len(args) < 2:
		Parser.parse_link(Request.GET_request(args[0]), False)
	elif options.link == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.link == True and len(args) == 0:
		print("\nNo url detected !")

	## --tree option
	if options.tree == True and len(args) != 0 and len(args) < 2:
		#parse_link(GET_request(args[0]))
		tree = MakeTree.URLTree(args[0], Parser.parse_link(Request.GET_request(args[0]), True))
		tree.generate()
	elif options.tree == True and len(args) > 1:
		print("\nError: too many argmuments !")
	elif options.tree == True and len(args) == 0:
		print("\nNo url detected !")

if __name__ == "__main__":
	try:
		Main()
	except KeyboardInterrupt:
		print()
		print("Aborting...")
		print()
