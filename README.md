# BetterBatch V1.0.0
BetterBatch is a Interpreter wich executes Console commands of the current OS and it also has custom commands like
- WaitS [time: int]: Wait a specified time (Seconds)
- WaitMS [time: int]: Wait a specified time (Milliseconds)
- var [varname] [vartext(string)]: define a Variable wich can be used by example echo $varname;
- epy [command]: executes python code
# Example
i have this in `test.bbatch`
```
^ This is a comment, it is ignored by the Interpreter
var name Max; echo $name; ^ defines the variable name wich can be used by $name
echo The name is $name;
waitS 3; ^ Waits 3 seconds,
waitMS 1000; ^ Waits 1000 Milliseconds
cls; ^ clears the console (on windows)
epy import random;
epy print(str(random.randint(0, 10)));
echo finished;
```
execute this by typing `py bbatch.py test.bbatch` into the console.
A full Documentation will be available soon.
