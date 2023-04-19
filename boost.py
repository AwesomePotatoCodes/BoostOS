# Copyright (c) 2023 BoostOS Team
# See LICENSE.md for more information.

# print logo
from core import version as versionfile
print("\x1b[34m\x1b[1m██████╗░░█████╗░░█████╗░░██████╗████████╗  ░█████╗░░██████╗\n██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██╔════╝\n██████╦╝██║░░██║██║░░██║╚█████╗░░░░██║░░░  ██║░░██║╚█████╗░\n██╔══██╗██║░░██║██║░░██║░╚═══██╗░░░██║░░░  ██║░░██║░╚═══██╗\n██████╦╝╚█████╔╝╚█████╔╝██████╔╝░░░██║░░░  ╚█████╔╝██████╔╝\n╚═════╝░░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═════╝░")
print(f"\x1b[92m\x1b[1m[!] Version {versionfile.current}\n")

import os

def clear():
	os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def start_loading(loading_dots):
	clear()
	
	print("\x1b[34m\x1b[1m██████╗░░█████╗░░█████╗░░██████╗████████╗  ░█████╗░░██████╗\n██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██╔════╝\n██████╦╝██║░░██║██║░░██║╚█████╗░░░░██║░░░  ██║░░██║╚█████╗░\n██╔══██╗██║░░██║██║░░██║░╚═══██╗░░░██║░░░  ██║░░██║░╚═══██╗\n██████╦╝╚█████╔╝╚█████╔╝██████╔╝░░░██║░░░  ╚█████╔╝██████╔╝\n╚═════╝░░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═════╝░")
	print(f"\x1b[92m\x1b[1m[!] Version {versionfile.current}\x1b[0m\n")

	print(f"Loading [{loading_dots}]")

start_loading("•-----")

# basic imports
import time, random
from datetime import datetime
import sys, requests

# boost imports
import core.info as inf
from core.boostc import Stl as stl, Fg as fg, FgStrong as fgs, Bg as bg, BgStrong as bgs
from core.boostc import set_accent_color, list_item, error, incorrect, notice, warning, note
from core import boostscript

start_loading("••----")

# database imports
from replit import db

start_loading("•••---")

# ui imports
from getkey import getkey, keys
from colorama import init as colorama_init
# from playsound import playsound

start_loading("••••--")

with open('core/usr/logs.bsx', 'w') as logs:
	logs.write('') # clear all existing log history

colorama_init(autoreset=True) # autoreset foreground colours
banned = 0 # banned variable
not_allowed = [" ", "\t", "\\", "\n", "!", "@", "#", "$", "%", "*", "(", ")", "[", "]", "{", "}", "&", "`", "=", ":", ";", ",", "<", ">", "/", "|", "~"] # global version of not_allowed
tag = ""

clear()

start_loading("•••••-")

def set_color(is_setup=False):
	global color
	print("Pick an accent color:")
	print(fg.red      + "[1] Red")
	print(fg.blue     + "[2] Blue")
	print(fgs.green   + "[3] Green")
	print(fgs.cyan    + "[4] Cyan")
	print(fgs.magenta + "[5] Magenta")
	print(fgs.yellow  + "[6] Yellow")
	print(fg.white    + "[7] White")
	# print(fg.black+bg.white+stl.bold+"[8] Inverted")
	print()
	notice("Default is blue")
	option = input(">> ").lower().strip(" ")
	if option == ("1" or "red"):
		color = fg.red
		print("Set to: RED")
	elif option == ("2" or "blue"):
		color = fg.blue
		print("Set to: BLUE")
	elif option == ("3" or "green"):
		color = fgs.green
		print("Set to: GREEN")
	elif option == ("4" or "cyan"):
		color = fgs.cyan
		print("Set to: CYAN")
	elif option == ("5" or "magenta"):
		color = fgs.magenta
		print("Set to: MAGENTA")
	elif option == ("6" or "yellow"):
		color = fgs.yellow
		print("Set to: YELLOW")
	elif option == ("7" or "white"):
		color = fg.white
		print("Set to: WHITE")
	elif option == ("8" or "inverted"):
		color = fg.black+bg.white+stl.bold
		print("Set to: INVERTED")
	else:
		error("Invalid input.")
		if is_setup:
			print("Set to: BLUE")
			color = fg.blue
		else:
			print("Color change cancelled.")
			color = color

def stringify_color(color):
	if color == fg.red:
		return "Red"
	elif color == fg.blue:
		return "Blue"
	elif color == fgs.green:
		return "Green"
	elif color == fgs.cyan:
		return "Cyan"
	elif color == fgs.magenta:
		return "Magenta"
	elif color == fgs.yellow:
		return "Yellow"
	elif color == fg.white:
		return "White"
	elif color == (fg.black + bg.white + stl.bold):
		return "Inverted"
	else:
		return "Unknown"

def start_setup():
	#----SETUP SCRIPT----#
	clear()
	
	print(stl.bold + fg.blue + "BoostOS Setup")
	lines = '-' * (os.get_terminal_size().columns - 2)
	print(stl.bold + fgs.blue + lines)
	
	# fetch all globals
	global username
	global password
	global autosave
	global color
	global gtn_high
	global money
	global data
	data = db.keys()
	db["gtnhighs"] = 0
	db["moneyhck"] = 0
	db["isbanned"] = 0
	db["autosave"] = 0
	not_allowed = [" ", "\t", "\\", "\n", "!", "@", "#", "$", "%", "*", "(", ")", "[", "]", "{", "}", "&", "`", "=", ":", ";", ",", "<", ">", "/"]
	username = input("Username: ").lower()
	for not_allowed_item in not_allowed:
		username = username.replace(not_allowed_item, "-")
	if username in inf.Internal.admins and inf.Internal.realname not in inf.Internal.admins:
		error("Sorry, but your name isn't allowed!")
		time.sleep(5)
		clear()
		start_setup()
	password = input("Password: ")
	autosave = input("Autosave? (y/n): ")
	gtn_high = 0
	money = 0
	if autosave == "y":
		autosave = True
		db["autosave"] = autosave
		print(fgs.green+"[✓] Autosave enabled!")
	elif autosave == "n":
		autosave = False
		db["autosave"] = autosave
		error("Autosave disabled.")
	else:
		autosave = False
		print("Invalid input, autosave is off.")
		print()
	db["username"] = username
	db["password"] = password
	set_color(True) # run color script

def user_autosave(show_guest_message):
	if status != "guest":
		db["username"] = username
		db["password"] = password
		db["usrcolor"] = color
		db["gtnhighs"] = db["gtnhighs"] + int(gtn_high)
		db["moneyhck"] = int(money)
		db["isbanned"] = banned
	elif status == "guest" and show_guest_message:
		error("Saving isn't available to guests.")

def user_reset():
	try:
		if "username" in db.keys():
			del db["username"]
		
		if "password" in db.keys():
			del db["password"]

		if "usrcolor" in db.keys():
			del db["usrcolor"]

		if "gtnhighs" in db.keys():
			del db["gtnhighs"]

		if "moneyhck" in db.keys():
			del db["moneyhck"]

		if "isbanned" in db.keys():
			del db["isbanned"]
					
		print("Deleted all data.")
		quit(1)
	except:
		print("Error with resetting.")

def alert_bell():
	print("\a", end="")

def shutdown(autosave):
	clear()
	if autosave:
		user_autosave(False)
	print("Closed session.")
	sys.exit(0)

#------------------ START OF SETUP -------------------#

start_loading("••••••")

username = "Null"
color = fg.blue
inf.Shell.prefix = "BoostOS"

prompt = color + str(username) + "@" + inf.Shell.prefix + fg.white + "$ "

clear()
print(inf.Shell.logo)

try:
	banned = db["isbanned"]
except:
	# Not banned
	pass

if banned == True:
	error("Your account has been banned. Press Enter to continue...")
	hehe = input()
	if hehe == str(os.environ["BanBypass"]):
		print(fgs.green + "[✓] You're Unbanned :)")
	else:
		quit(1)

print(f"{fgs.green}{stl.bold}[!] Version {inf.System.version}")
print(stl.reset)

list_item(1, "Import data | Restore your previous data")
list_item(2, "New account | Create a new BoostOS account")
list_item(3, "Guest mode* | *WARNING, this doesn't save.\n")
option = input(prompt)
if option == "1":
	try:
		print("Starting...")
		username = db["username"]
		password = db["password"]
		color    = db["usrcolor"]
		gtn_high = db["gtnhighs"]
		money    = db["moneyhck"]
		autosave = db["autosave"]
	except:
		print("\nNo data found.\nContinuing with new account.")
		print("Press Enter to continue... ")
		input()
		start_setup()
	finally:
		status = "user"

elif option == "2":
	status = "user"
	start_setup()

elif option == "3":
	status         = "guest"
	inf.Shell.mode = "guest"
	username       = "guest-" + str(random.randint(1, 999))
	colorpalette   = [fg.red, fg.blue, fgs.green, fgs.cyan, fgs.magenta, fgs.yellow, fg.white]
	color          = colorpalette[random.randint(0, 6)]
	autosave       = False
	gtn_high       = 0
	money          = 0
	# print("PASSWORD: guestpassword")
	# password = "guestpassword"
	# Guest password doesn't work... weird.

else:
	error("Invalid input.")
	quit(1)
#------------------- END OF SETUP --------------------#

clear()
print("type 'help' for default commands.")

system_running = True


while system_running:
	# Ban user if bypassing restrictions
	if inf.Internal.realname not in inf.Internal.admins and status == "admin":
		status = "banned"
		db["isbanned"] = True
		incorrect("You've been banned.")
		quit()

	# autosave
	if autosave == True:
		user_autosave(False)
	
	# Set accent colour for boostc
	set_accent_color(color)
	
	# Set the beginning of the terminal prompt
	if tag != "":
		prompt = f"{fg.red}[{fg.white}{str(tag)}{fg.red}]{fg.white} " + color + str(username) + "@" + inf.Shell.prefix
	else:
		prompt = color + str(username) + "@" + inf.Shell.prefix

	# If there is a mode set, add that to the terminal prompt
	if inf.Shell.mode:
		if tag != "":
			prompt += f"[{tag}] " + fg.white + ":" + color + inf.Shell.mode
		else:
			prompt += fg.white + ":" + color + inf.Shell.mode

	# Finally, add the $ at the end of the terminal prompt
	prompt += fg.white + "$ "
	
	# --------- #
	# GET INPUT #
	# --------- #
	try:
		request = input(prompt).lower().strip(" ")
	except KeyboardInterrupt:
		print()
		error("Please use `close` to properly close your session.")
		request = "<^c>"

	# save to log
	with open('core/usr/logs.bsx', 'a') as logs:
		current_date = datetime.today().strftime("%B %d %Y")
		current_time = datetime.now().strftime("%H:%M")
		logs.write(f'`{request}` @ {current_date}, {str(current_time)}\n')

	# if the request is not a valid command
	if request not in inf.Shell.commands and request != "<^c>":
		error(f"Command '{request}' not found.\nType 'help' for a list of commands.")
		# corrector
		if len(request) <= 10:
			for item in inf.Shell.commands:
				if item in request:
					print(fg.red + stl.bold + f"Correction: Did you mean: '{item}'?")
					break
				check = 0
				iteml = list(item)
				for subject in iteml:
					if subject in request:
						check += 1
				if check == len(iteml) or check == len(iteml) - 1:
					print(fg.red + stl.bold + f"Correction: Did you mean: '{item}'?")
					break
	
	if request == "help":
		print(stl.underline + stl.bold + "Boost OS Commands")
		print(inf.Messages.help)

	elif request == "clear":
		clear()

	elif request == "bell":
		alert_bell()
	
	elif request == "close":
		if status != "guest":
			# Is not guest
			print("Are you sure?")
			option = input("(y/n): ").lower().strip(" ")

			if option == "y":
				# Decides to shutdown
				print("Would you like to save?")
				option = input("(y/n): ").lower().strip(" ")
				
				if option == "y":
					# Would like to save
					shutdown(autosave=True)
				
				elif option == "n":
					# Would not like to save
					print("Are you sure?")
					option = input("(y/n): ")
					if option == "y":
						# Confirms not wanting to save
						shutdown(autosave=False)
					
					elif option == "n":
						# Confirms they want to save after all
						shutdown(autosave=True)
					
					else:
						# Invalid input
						error("Invalid input.")
				else:
					# Invalid input
					error("Invalid input.")
			
			elif option == "n":
				# Decides to not shutdown
				pass

			else:
				# Invalid input
				error("Invalid input.")
		
		else:
			# Is guest
			print("Are you sure? Remember that your data is not saved.")
			option = input("(y/n): ")
			
			if option == "y":
				shutdown(autosave=False)
			elif option == "n":
				pass
			else:
				error("Invalid input.")

	elif request == "boost.help":
		print(stl.underline + stl.bold + "Boost OS Commands")
		print(inf.Messages.boosthelp)

	elif request == "admin.help":
		print(stl.underline + stl.bold + "Admin Commands")
		notice("These commands can only be used by admins.")
		print(inf.Messages.adminhelp)
	
	elif request == "guide":
		if os.path.exists("core/guide.txt"):
			with open("core/guide.txt", "r") as help:
				try:
					print(help.read())
				except:
					pass
		else:
			error("Help file not found.")

	elif request == "echo":
		option = input("Message: ")
		print(f"{option}")

	elif request == "boost.lolzdb":
		warning("This autosaves no matter what.")
		list_item(1, "Read")
		list_item(2, "Write")
		list_item(3, "Settings")
		value = input(">>> ")
		if value == "1":
			print("Choose a slot.")
			list_item(1, "Slot")
			list_item(2, "Slot")
			list_item(3, "Slot")
			value = input("read>>> ")
			if value == "1":
				try:
					slot1 = db["key1"]
					print(slot1)
					input("... ")
				except:
					print("Error.")
			elif value == "2":
				try:
					slot2 = db["key2"]
					print(slot2)
					input("... ")
				except:
					print("Error.")
			elif value == "3":
				try:
					slot3 = db["key3"]
					print(slot3)
					input("... ")
				except:
					print("Error.")
		elif value == "2":
			print("Write to?")
			list_item(1, "Slot")
			list_item(2, "Slot")
			list_item(3, "Slot")
			value = input("write>>> ")
			if value == "1":
				print("Writing to Slot 1.")
				db["key1"] = input("write/slot1>>> ")
				input("... ")
			elif value == "2":
				print("Writing to Slot 2")
				db["key2"] = input("write/slot2>>> ")
				input("... ")
			elif value == "3":
				print("Writing to Slot 3")
				db["key3"] = input("write/slot3>>> ")
				input("... ")
		elif value == "3":
			list_item(1, "Reset all data (BROKEN)")
			list_item(2, "Back to Menu")
			value = input("settings>>> ")
			if value == "1":
				if "key1" in db.keys():
					del db["key1"]
				if "key2" in db.keys():
					del db["key2"]
				if "key3" in db.keys():
					del db["key3"]
				print("Data Reset")
				input("... ")
			elif value == "2":
				pass
	
	elif request == "boost.pref":
		print("Preferences Menu")
		list_item(1, "Accent Color")
		list_item(2, "Username")
		list_item(3, "Password")
		list_item(4, "Autosave")
		list_item(5, "Reset")
		option = input("\nChoose an option: ")
		if option == "1":
			set_color() # Run colour script
		
		elif option == "2":
			if status == "guest":
				error("Name changing is disabled for guests.")
			else:
				print("Change your name.")
				prev_username = username
				username = input("New username: ")
				if username == "" and " ":
					username = prev_username
					print("Cancelling change.")
				else:
					print("Name changed.")

		elif option == "3":
			if status == "guest":
				error("Passwords aren't available to guest accounts.")
			else:
				print("Confirm who you are.")
				confirm = input("Password: ")
				if password == confirm:
					print("Change your password.")
					prev_password = password
					password = input("New password: ")
					if password == "" and " ":
						password = prev_password
						print("Cancelling change.")
					else:
						print("Password changed.")
				else:
					error("Incorrect password.")
		
		elif option == "4":
			if status == "guest":
				error("Guests can't save.")
			else:
				if autosave == True:
					print("\nAutosave is currently: " + fg.green + "ON")
				else:
					print("\nAutosave is currently: " + fg.red + "OFF")
			
			list_item(1, "Turn on save")
			list_item(2, "Turn off save")
			list_item(3, "Delete my data")
			option = input("\nChoose an option: ")
			if option == "1":
				autosave = True
				print("Autosave is on.")
			elif option == "2":
				autosave = False
				print("Autosave is off.")
			elif option == "3":
				print("Please enter your password to confirm.")
				option = input("Password: ")
				if option == password:
					user_reset()
					system_running = False
				else:
					error("Incorrect.")

		elif option == "5":
			warning("Are you sure?")
			option = input("(y/n): ")
			if option == "y":
				time.sleep(5)
				start_setup()
			elif option == "n":
				pass
			else:
				error("Invalid input. Cancelling.")
					
	elif request == "system":
		print(color + stl.bold + stl.underline + "\nBoostOS Info")
		print(f"OS Version: {inf.System.version}")
		print(f"Computer name: {inf.Shell.prefix}")
		print(color + stl.bold + stl.underline + "\nUser Info")
		print(f"User Status: {status}")
		print(f"Account Name: {username}")
		print(f"Accent Color: {color}{stringify_color(color)}")
		print()

    # todo: make this functional by allowing users to open apps from /public/apps - as well as include a functional devkit to help people make their own apps with ease.
	elif request == "boost.apps":
		print("Please run 'list' for a list of apps\nOr 'help' for information\n")
		app_command = input("apps> ")
		if app_command == "list":
			app_dir = os.listdir('public/apps/')
			num = 0
			for app in app_dir:
				if app != "devkit": num=+1; list_item(num, app)
					
		elif app_command == "help":
			print("list           List all apps")
			print("run [app]      Run an app")
			print("devkit         Get a link to the dev docs")

		elif app_command == "run":
			split = app_command.split(" ")
			os.system(f"python3 {split[1]}")
			print("Done")
			
	elif request == "admin.login":
		password = input(fgs.green+"Admin Password: ")
		if password == os.environ['AdminPass'] and inf.Internal.realname in inf.Internal.admins:
			print(fgs.green + "[✓] Hello admin!")
			inf.Shell.mode = "admin"
			status = "admin"
		elif password != os.environ["AdminPass"]:
			error("Incorrect.")
		elif inf.Internal.realname not in inf.Internal.admins:
			error("Access denied.")
			print("Nice try.")
	
	elif request == "admin.exit":
		if status == "admin":
			status = "user"
			inf.Shell.mode = ""
			print("Logged out of admin mode.")
		else:
			error("Access denied.")
	
	elif request == "beta.login":
		print("Are you sure you want to enter beta mode?")
		print("Remember, these features may break your account.")
		option = input("(y/n): ")
		if option == "y":
			inf.Shell.mode = "beta"
			user_autosave(False)
			note(fgs.green, "Use beta.help to find work-in-progress features.")

	elif request == "beta.help":
		print(stl.underline + stl.bold + "Beta Help")
		print(inf.Messages.betahelp)
	
	elif request == "beta.report":
		if inf.Shell.mode == "beta":
			with open("core/reports.txt", "a") as bug:
				bug.write(input(color + "report>>> " + stl.reset) + "\n")
		else:
			error("Please login to beta mode first.")

	elif request == "math":
		print("Run a math equation.")
		equation = input("> ").lower()
		if not ("os" or "environ" or "print" or "adminpass" or "banbypass" or "admin" or "import" or "from" or "try" or "except" or "def" or "time" or '"' or "'" or "if" or "elif" or "else" or "with" or "as" or "eval") in equation:
			try:
				print(eval(equation))
			except ArithmeticError:
				error("Something went wrong calculating, please check for errors.")
		else:
			error("Sorry, this calculation contains a forbidden string.")
	
	elif request == "admin.script":
		if status == "admin" and inf.Internal.realname in inf.Internal.admins:
			print("Run a Python script.")
			print("Use ';' to break commands.")
			script = input("> ")
			exec(script)
		else:
			error("Access denied.")
	
	elif request == "edit":
		text = ""
		editingText = True
		file_location = ""
		while editingText:
			clear()

			padding = ' ' * (os.get_terminal_size().columns - 31 - len(file_location))
			
			print(' ' + stl.inverse + f' Editing public/{file_location}{padding}ESC to close ' + stl.reset + ' ')
			
			print(text, end='')
			keyPress = getkey()
			
			if keyPress == keys.ESC:
				editingText = False
				
			elif keyPress == keys.BACKSPACE:
				text = text[:-1]
				
			else:
				text += str(keyPress)

		print("\n")
		file_location = input("save as: public/")
		if file_location:
			if not "secure.bsx" in file_location:
				if not os.path.exists("public/" + file_location):
					with open("public/" + file_location, "x") as file:
						file.write(str(text))
						print("Saved.")
				else:
					error("File already exists.")
			else:
				error("Cannot save to a protected file.")
		else:
			print("Not saved.")

	elif request == "credits":
		print(inf.Shell.logo)
		print(inf.System.copyright_notice)
		print(inf.Messages.credits)
	
	elif request == "beta.source":
		if inf.Shell.mode == "beta":
			print("Is the file local or from the internet?")
			filefrom = input("[local/web]: ").lower().strip(" ")
			if filefrom == "local":
				note(fgs.green, "You can use the edit tool to write your own scripts.")
				boostscript.ParseFromFile(("public/" + input("File Location: public/")))
			elif filefrom == "web":
				note(fgs.green, "Try our online archive of scripts at <boostos.github.io/scripts>!")
				boostscript.ParseFromWeb(input("File URL: "))
		else:
			error("Please login to beta mode first using beta.login.")

	elif request == "files.help":
		print(stl.underline + stl.bold + "Filesystem Help")
		print(inf.Messages.fileshelp)
	
	elif request == "files.list":
		print("Choose a folder to read from: ")
		dir_location = input("public/")
		print()
		try:
			for child in os.listdir('public/' + dir_location):
				print(child)
		except:
			error("Error reading from directory. Make sure you spelled the name correctly.")

	elif request == "files.read":
		print("Choose a file to read from:")
		file_location = "public/" + input("public/")
		print()
		if not "secure.bsx" in file_location:
			try:
				with open(file_location, 'r') as file_handle:
					file_contents = file_handle.read()
	
				if file_contents.strip(" ").strip("\t").strip("\n") == "":
					print("[empty]")
				else:
					print(file_contents)
					
			except FileNotFoundError:
				error("The file requested does not exist. Make sure you spelled the filename correctly.")
			except:
				error("Error reading from file.")
		else:
			error("Cannot save to a protected file.")

	elif request == "datetime":
		# Get date and time
		current_time = datetime.now().strftime("%H:%M")
			
		current_date = datetime.today().strftime("%B %d %Y")
			
		current_day = datetime.today().isoweekday()
		if current_day == 1: current_day = "Monday"
		if current_day == 2: current_day = "Tuesday"
		if current_day == 3: current_day = "Wednesday"
		if current_day == 4: current_day = "Thursday"
		if current_day == 5: current_day = "Friday"
		if current_day == 6: current_day = "Saturday"
		if current_day == 7: current_day = "Sunday"
	
		# Print date and time
		print(f"@ {fgs.magenta}{stl.underline}{current_day}, {current_date} {str(current_time)}")

	elif request == "log":
		with open('core/usr/logs.bsx', 'r') as logs:
			print(logs.read())

	elif request == "tag":
		notice("(Say None for no tag)")
		tag = input("Name: ")
		if tag == "None": tag = ""
		if len(tag) > 15: error("Must be less than 15 characters.") ; tag = ""
		