# BoostOS Colo(u)r Module
class Stl:
	reset     = "\x1b[0m"
	bold      = "\x1b[1m"
	underline = "\x1b[4m"
	inverse   = "\x1b[7m"

class Fg:
	black     = "\x1b[30m"
	red       = "\x1b[31m"
	green     = "\x1b[32m"
	yellow    = "\x1b[33m"
	blue      = "\x1b[34m"
	magenta   = "\x1b[35m"
	cyan      = "\x1b[36m"
	white     = "\x1b[37m"

class Bg:
	black     = "\x1b[40m"
	red       = "\x1b[41m"
	green     = "\x1b[42m"
	yellow    = "\x1b[43m"
	blue      = "\x1b[44m"
	magenta   = "\x1b[45m"
	cyan      = "\x1b[46m"
	white     = "\x1b[47m"

class FgStrong:
	black     = "\x1b[90m"
	red       = "\x1b[91m"
	green     = "\x1b[92m"
	yellow    = "\x1b[93m"
	blue      = "\x1b[94m"
	magenta   = "\x1b[95m"
	cyan      = "\x1b[96m"
	white     = "\x1b[97m"

class BgStrong:
	black     = "\x1b[100m"
	red       = "\x1b[101m"
	green     = "\x1b[102m"
	yellow    = "\x1b[103m"
	blue      = "\x1b[104m"
	magenta   = "\x1b[105m"
	cyan      = "\x1b[106m"
	white     = "\x1b[107m"

boost_accent = Fg.blue

def set_accent_color(color):
	global boost_accent
	boost_accent = color

def write(string):
	print(string + Stl.reset)

def error(string):
	write(Fg.red + Stl.bold + "[X]" + Stl.reset + Fg.red + " " + string)

def incorrect(string):
	write(Fg.red + string)

def note(color, string):
	print(color + Stl.bold + "[!]" + Stl.reset + color + " " + string)

def notice(string):
	write(Fg.yellow + Stl.bold + "[!]" + Stl.reset + Fg.yellow + " " + string)

def warning(string):
	write(Fg.red + Stl.bold + "[!]" + Stl.reset + Fg.red + " " + string)

def bright(string):
	return Stl.bright + string + Stl.reset

def underline(string):
	return Stl.underline + string + Stl.reset

def list_item(item_num, string):
	global boost_accent
	write(boost_accent + Stl.bold + "[" + str(item_num) + "]" + Stl.reset + Fg.white + " " + string)
