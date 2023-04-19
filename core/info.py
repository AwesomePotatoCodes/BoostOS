# Extra system information
import os
from core import version as versionfile

# SYSTEM #
class System:
	version = versionfile.current
	copyright_notice = """\
Copyright © 2023 BoostOS Team
See LICENSE.md for more information.
"""

# INTERNAL #
class Internal:
	admins = ["boostos", "AwesomePotatoLXS", "LunaLeEpix", "samrpf"]
	realname = os.environ["REPL_OWNER"]

# SHELL #
class Shell:
	logo = "\x1b[34m\x1b[1m██████╗░░█████╗░░█████╗░░██████╗████████╗  ░█████╗░░██████╗\n██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██╔════╝\n██████╦╝██║░░██║██║░░██║╚█████╗░░░░██║░░░  ██║░░██║╚█████╗░\n██╔══██╗██║░░██║██║░░██║░╚═══██╗░░░██║░░░  ██║░░██║░╚═══██╗\n██████╦╝╚█████╔╝╚█████╔╝██████╔╝░░░██║░░░  ╚█████╔╝██████╔╝\n╚═════╝░░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═════╝░"
	prefix = "BoostOS"
	mode = ""
	username_text_character = "\ueea7"
	username_text_character_unicode = ""
	commands = [
		'help', 'clear', 'echo', 'close', 'bell', 'credits', 'math', 'system', 'datetime', 'log', 'guide',
		'boost.help', 'boost.lolzdb', 'boost.pref', 'boost.apps',
		'files.help', 'files.list', 'files.read',
		'admin.help', 'admin.login', 'admin.script', 'admin.exit',
		'beta.help', 'beta.login', 'beta.source'
	]

# COLLECTIONS #
class Collections:
	shapes = ['🟧', '🟥', '🟨', '🟩', '🟦']

# MESSAGES #
class Messages:
	help = """\
HELP         List of commands
CLEAR        Clear console
ECHO         Make the system echo text
EDIT         Text editor
MATH         Run math expressions
DATETIME     Fetch the current date and time
GUIDE        Basic guide to BoostOS
SYSTEM       General system info
LOG          Read the current shell input log
BELL         Ring a bell
CREDITS      See credits for BoostOS
CLOSE        Close your session
FILES.HELP   List of filesystem commands
BOOST.HELP   BoostOS help
ADMIN.HELP   Admin help
BETA.LOGIN   Test beta features"""
	fileshelp = """\
FILES.LIST   List the contents of a directory
FILES.READ   Read the contents of a file"""
	boosthelp = """\
BOOST.LOLZDB   Access your LolzDB account
BOOST.PREF     Terminal settings and other preferences
BOOST.APPS     Run programs, apps, games"""
	adminhelp = """\
ADMIN.LOGIN    Enables admin mode
ADMIN.SCRIPT   Run Python scripts
ADMIN.EXIT     Leave admin mode"""
	betahelp = """\
BETA.SOURCE   Try out the new scripting engine"""
	credits = """\
    DEVELOPERS
- AwesomePotatoLXS
- samrland

    DEBUGGERS
- LunaLeEpix"""
