# exit_elegantly
some methods to exit elegantly from a program in python

# ways to think
* to create a thread to check/set a flag periodically
* to use a special file to represent a flag
* to use a database item to represent a flag

# pratical method
* to use asyncio loop
* to catch SystemExit/KeyboardInterrupt exception thrown from sys.exit()/SIGINT
* to maintain a global flag in redis
* to create a file to indicate that system should exit instantly
