# [In Development] Scripting

## Starting
AwesomePotato's already created [LolzScript](https://replit.com/@awesomepotatolxs/LolzScript?v=1), and I've (samrpf) already worked on my own instruction2,
so maybe we could make a built-in scripting system in BoostOS. Using the `edit` tool, users
can already write their own text files and save it with any file extension, so they can already
write scripts. All we need now is a way to run them.

I'm thinking something like

```
source local scripts/myscript.boost
```

where `scripts/myscript.boost` is the location of the script in `public/files`.

We could also create a way to run scripts from the internet, so developers can
kinds host their own apps while we're working out how to get the app submission process
set up. Something like

```
source web somecoolwebsite.com/scripts/coolapp.boost
```

It'll use the `requests` library to fetch the script from the internet.

The scripting language will be very limited, so no trying to bypass any restrictions
by getting access to the shell or to Python internals.

But almost all other features will be accessible. We will expose the userdata, such
as the user's username, their accent colour, and other small things like that. Scripts
will be able to edit files, as well.

We could have it so that scripts run from the internet are run in a container so they
can't touch anything outside without permission. They won't be able to edit files, change
information, stuff like that without explicit permission from the user. But only for scripts
from the internet, scripts written by the user will be run in trusted mode, since the user probably
knows what they're doing.

## Requests
I'm thinking we could do some sort of requests thing, where the script
is allowed to use GET or POST requests to get information from the internet.

```
requests myconnection get https://server.com/api input1=testing input2=othertesting
// the above line will connect to https://server.com/api?input1=testing&input2=othertesting
// and it will be saved under the name `myconnection`

// close connection
requests myconnection close
```

The only reason I'm suggesting this is because
I want to make a [postLit](https://github.com/postLit/postLit.js/blob/main/index.js) app,
since postLit uses very simple GET requests for actions.

## Console Styling
Create a way to style the console output in many different ways.
See:

```
console color red
console style underline
```

You could also use the user's accent colour:

```
console color accent
```

And finish it all off with a reset call:

```
console reset
```

## Preprocessing
Create a way to define important things before anything else
happens.

Kind of like how in C/C++, some lines that start with a `#`
are run before the compilation and before any of the other code
is read.

Preprocessing usually includes important information like the
version number, settings that the script writer would like to keep
throughout the whole script, and other things.

I think we should also start preprocessing requests with a #

```
#version 1.2.3
#immutable true
// the second line is for if the user wants to make
// their variables immutable
```

## Special Pre-defined Variables
We could have variables that start with `@` rather than `$`
which are pre-defined by the parser. We could have :

```
@username
@accent-color-string
@password
```

Or maybe leave out that last one. Which actually gives me another idea...

## Ask for Password Permission
Using a simple command like `password`, scripts can easily
use a password prompt where they have to insert their password
for an action to be made.

### Code

```
password do
	writeln Password input completed!
end

writeln This executes anyway.
```

### Output

#### Proper Input

```
[!] Please input your password.
$ ******
Pasword input completed!
This executes anyway.
```

#### Improper Input

```
[!] Please input your password.
$ ******
This executes anyway.
```

## ?math
The way users will be able to calculate math is using
the ?math keyword. Here is the syntax:

```
$myvar = ?math 2 + 3
$myothervar = ?math $myvar + 5
$evenmorevars = ?math $myvar + $myothervar
```

The spaces have to be there.

## Escapes
Wherever there is a string, the parser will now look for
escapes before compiling the string.

We will use the `^` character for escapes
rather than the usual `\`.

```
writeln Extra_newline!^n
```
