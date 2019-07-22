# exit_elegantly
some methods to exit elegantly from a program in python

# ways to think
* to create a thread to check/set a flag periodically
* to use a special file to represent a flag
* to use a database item to represent a flag

# pratical method
* use asyncio loop
* catch SystemExit exception thrown from sys.exit()
