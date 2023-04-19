import os, random, time
from core.boostc import Stl, Fg, FgStrong
import requests

# used to print coloured error messages
def Error(errorval):
	print(f"{Fg.red}{Stl.bold}[Error]{Stl.reset}{Fg.red} {errorval}{Stl.reset}")

# used print coloured help messages
def Note(noteval):
	print(f"{FgStrong.yellow}{noteval}{Stl.reset}")

# error classes
class BoostUnrecognizedCommand(Exception):
	# used for unrecognized commands
	pass

class BoostTrustLow(Exception):
	# used if a low trust-level script (from the internet) tries to run a high-trust command
	pass

class BoostSyntaxError(Exception):
	# used if there is an error with the syntax of the code (whenever a required keyword is missing, use BoostSyntaxError)
	pass

# the actual parser
def Parse(lines, trust_level):
	# @param lines       : A list/array of the lines in the script
	# @param trust_level : The level of trust for the script: 1 is local, 2 is internet
	print()

	# reserved = ["?get", "?random"]
	# ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	vars = {}
	current_line = 0
	
	try:
		for raw_line in lines:
			line = raw_line.split(' ')
			parameters = line[1:]
			# parameters = line.pop(0)
		
			if line[0] == 'write':
				for item in parameters:
					if item.startswith('$'):
						print(vars[item], end='')
					else:
						print(item, end='')
					print(' ', end='')
				print('\b', end='')

			if line[0] == 'writeln':
				for item in parameters:
					if item.startswith('$'):
						print(vars[item], end='')
					else:
						print(item, end='')
					print(' ', end='')
				print('\b', end='\n')
			
			elif line[0] == 'console':
				if line[1] == 'color':
					if line[2] == 'red':
						print(Fg.red, end='')
					elif line[2] == 'blue':
						print(Fg.blue, end='')
					elif line[2] == 'white':
						print(Fg.white, end='')
				
				elif line[1] == 'style':
					if line[2] == 'bold':
						print(Stl.bold, end='')
					elif line[2] == 'underline':
						print(Stl.underline, end='')
					elif line[2] == 'inverse':
						print(Stl.inverse, end='')
				
				elif line[1] == 'reset':
					print(Stl.reset, end='')

			elif line[0] == 'clear':
				os.system('clear')

			elif line[0] == 'sleep':
				time.sleep(float(line[1]))

			elif line[0].startswith("$"):
				if line[1] and line[1] == "=":
					if line[2]:
						if line[2] != "?get" and line[2] != "?random":
							vars[line[0]] = line[2]
						elif line[2] == "?get":
							vars[line[0]] = input(line[3].replace("_", " "))
						elif line[2] == "?random":
							vars[line[0]] = random.randint(int(line[3]), int(line[4]))
					else:
						raise BoostSyntaxError()
				else:
					raise BoostSyntaxError()
						
			
			elif (not(raw_line)) or (line[0].startswith('//')):
				pass

			else:
				raise BoostUnrecognizedCommand()

			current_line += 1
	
	except BoostUnrecognizedCommand:
		Error(f"<UnrecognizedCommand> at line {current_line}: Command '{line[0]}' invalid.")
		
	except BoostSyntaxError:
		Error(f"<SyntaxError> at line {current_line}: Something is missing.")

		""" Keep commented out until released out of beta
		except:
			Error(f"<InternalError> at line {current_line}: There is an internal problem with the engine. Please contact us so that we can fix this problem.")
		"""
	
	finally:
		print()

# used to parse local files
def ParseFromFile(file):
	try:
		# open file
		with open(file, 'r') as script:
			# save lines
			lines = script.readlines()
		
		# send off for parsing
		Parse(lines, 1)
	except FileNotFoundError:
		Error("File not found.")

# used to parse files from the internet
def ParseFromWeb(url):
	print("Fetching file...")
	try:
		# fetch the remote
		remote = requests.get(url)
		# save the lines in the script as an array
		lines = remote.text.splitlines()

		# close connection
		remote.close()
		
		# send off for parsing
		Parse(lines, 2)
	except:
		Error("why")
