# Changelog

All noteable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [In Beta]

- samrpf, AwesomePotatoLXS: Started boostscript project, avaiable at `beta.source`

## [1.5.0] - 2023-04-02

### Changed
- samr: Rebranded Boost Systems to BoostOS Team

### Fixed
- samr: Added `guide` command

## [1.4.0] - 2023-02-17

### Added

- samrpf: Added "boostos" to `inf.Internal.admins`
- samrpf: Added a check in `user_autosave` to always make sure the value exists on the database first before writing to it
- samrpf: Added supression for ^C on main command input to tell users to use the `close` command to properly close BoostOS
- samrpf: Reset function is now in `boost.pref`
- samrpf: Added `datetime` command to fetch the date and time

### Fixed

- samrpf: Changed all mentions of `system` package to `core`
- samrpf: Tabbed a comment that was causing some issues
- samrpf: Fixed all the `db["..."] in db.keys()` errors

### Changed

- samrpf: Renamed `exit` to `close`
- samrpf: Renamed `boost.math` to `math`
- samrpf: Renamed `boost.echo` to `echo`
- samrpf: Renamed `boost.info` to `system`
- samrpf: Reworked all of the help messages (changed order, fixed commands with changed names, etc.)
- samrpf: Changed to `echo` to not put single-quotes around your input
- samrpf: Renamed value `terminal_decoration` to `prompt`
- samrpf: Fixed `inf.System.copyright_notice` to say "Boost Systems" 

### Removed

- samrpf: Removed error handling for the autosave since it caused problems even when there were no actual problems
- samrpf: Removed the thing in `echo` where it banned you if you entered the admin password
- samrpf: Removed `boost.reset`; now available in `boost.pref`
- samrpf: Removed the printing of the time on every prompt, and instead opted for `datetime` command

## [1.3.0] - 2023-02-15

### Changed

- samrpf: In function `user_autosave`, renamed `should_i_care_if_the_user_is_a_guest` to `show_guest_message`
- samrpf: Changed `boost.math` message on forbidden string
- samrpf: Uppercased some inconsistent strings

### Removed

- samrpf: Removed `rickgonnagetu` and the corresponding function and message data
- samrpf: Removed `admin.bash` since it is virtually useless
- samrpf: Removed `stl.bright` from boostc since it is the same as `stl.bold`

## [1.2.4] - 2023-01-29

### Added

- samrpf: Added protection from user reading/writing from/to files names "secure.bsx". This filename is to be used for application to save important data that the user should not be able to access.

### Changed

- samrpf: Renamed `system` folder to `core`
- samrpf: Changed `boostscripts.samrpf.repl.co` to `boost-sys.github.io/scripts`

## [1.2.3] - 2023-01-21

### Added

- samrpf: Added a system so that usernames cannot contain any special symbols

### Changed

- samrpf: Renamed `username_text` variable to `terminal_decoration`
- samrpf: Moved some important things (autosave, ban-checking, etc.) before anything else in the main loop
- samrpf: Changed date format to HH:MM rather than HH:MM:SS
- samrpf: Made the random number range used for guest randomly generated names less extravagant (before: 1-99999, after: 1-999)
- samrpf: In `set_color` function, made the lowercasing more efficient and added space-stripping
- samrpf: Replaced all Colorama colours in main.py with boostc ones
- samrpf: Moved the `beta.help` notice from the user's main menu to only appear once the user logs into beta mode.
- samrpf: Replaced `boost.files` in favour of the `files.` category.
- samrpf: Changed `boost/reports.txt` to `system/reports.txt`.
- samrpf: Moved all items in `boost/` to `etc/`
- samrpf: Moved `music/` into `etc/`
- samrpf: Turned run action "malware.1" into its own functions, completely removing the run function
- samrpf: Replaced all run() calls with their proper functions

### Removed

- samrpf: Removed the comma in between the date and time display
- samrpf: **IMPORTANT!** Deleted beta.py; see `etc/notes/betamodel.txt`
- samrpf: Completely removed all "malware" (including `admin.malware` and `malware.py`) (except rickgonnagetu, start it with command `rickgonnagetu`)

## [1.2.2] - 2023-01-15

### Added

- samrpf: Added a date and time indicator for the command prompt screen (note that it's in GMT)
- AwesomePotatoLXS, samrpf: Added system/usr/logs.bsx for command logging purposes
- samrpf: Added a loading screen before defining everything
- samrpf: Added a toolbar to the `edit` tool
- samrpf: Created boostc functions `incorrect`, `warning`, and `note` and replaced applicable print statements
- samrpf: Replaced excalamation points in places where they shouldn't really be.
- samrpf: Replaced as many raw coloured print statements (`print(fore.[...] + "[...]")`) with boostc alternatives
- samrpf: Removed the "This will save your data!" message from `beta.login` because it doesn't really matter
- samrpf: Created `shutdown` function to keep `exit` more consistent
- samrpf: Added "Are you sure you want to shutdown?" message to `exit`

### Changed

- samrpf: Made the line go across the whole screen in the setup
- samrpf: Created a `clear` function and replaced every use of `os.system('clear')` with `clear()`
- samrpf: Renamed `boost.say` to `boost.echo`
- samrpf: Turned most run() functions into actual functions and replaced their applicable calls

## [1.2.1] - 2023-01-15

### Added

- samrpf: Added `inf.Shell.username_text_character` and `inf.Shell.username_text_character_unicode`
- samrpf: Started `inf.Collections`
- samrpf: Added `inf.Collections.shapes`
- samrpf: Command correction

### Changed

- samrpf: Replaced all spaces with tabs because I'm tired of `IndentationError: unindent does not match any outer indentation level`
- samrpf: Fixed the random colour selection for guests; originally went 1-7, even though lists are 0-indexed and it should have been 0-6

### Removed

- samrpf: **IMPORTANT!** Completely removed poetry for package installation because I just don't like it. Use `pip install` to install packages from now on, Replit's built-in Packager won't work
- samrpf: Removed the message telling guests about randomness since I don't really find a use for it

## [1.2.0] - 2023-01-14

### Added

- samrpf: Added boostc module for internal use of colours; still using colorama for most purposes, but we will fade it out over time in favour of boostc
- samrpf: Added info module to keep all important information required by the system that isn't changed during runtime.
- samrpf: Added stringify_color function to easily get the string value of a colour
- samrpf: Added message on startup telling guests that some things were chosen randomly for them since they chose to be a guest
- samrpf: Added "[X] Access denied." text if user is not admin to `admin.script`
- samrpf: Added a `bell` tool to activate a bell (make a little noise through the computer speaker)
- samrpf: Added a `credits` tool to see the credits for the BoostOS team

### Changed

- samrpf: Replaced all manually-created list items with a simple list_item function from boostc
- samrpf: Added back the `text_editor` tool as `edit` with a feature to save files
- samrpf: Changed the command prompt to remove the ":~" part, as it usually implies the directory path even though Boost OS is not a directory oriented OS, and added a mode feature for indicating whether user is in beta or admin mode
- samrpf: Changed `admin.math` to `boost.math` with lots of safety, not evaluating the expression if words like "os", "AdminPass", or "eval" are in the expression
- samrpf: Renamed variable `keys` in `boost.lolzdb` to `dbkeys` to stop interference with `getkey.keys`
- samrpf: Removed setting to change the sleep time since it doesn't work and instead opted with having the user hit enter to go to the next screen
- samrpf: Changed `admin.beta` to `beta.login` since it isn't protected by admin features
- samrpf: Added more options for random colour picker for guests
- samrpf: Turned boost/rickroll.txt into `inf.Messages.rickroll`

### Removed

- samrpf: Removed `admin.files` since it functions the same as `boost.files`
- samrpf: Removed action "Exit Admin Mode" from `admin.cmds` since it functions the same as `admin.exit`
- samrpf: Removed `admin.del` since it functions the same as `boost.reset`
- samrpf: Removed Ascii Art app since it causes the system to crash, probably will be added back later once code is fixed (find code in boost/scraps/AsciiArt.txt)
- samrpf: Removed action "Test Beta Features" from `admin.cmds` since beta testing is now open to the public
- samrpf: Removed `admin.cmds` since all of the actually useful features were moved out (you'd already know the secret code if you were admin, and how would you get to the change ban record screen if you're banned?)

### Security

- samrpf: Added protection for `admin.bash`; before this update, users that were not admins could _access the shell_. This vulnerability has been fixed now.
