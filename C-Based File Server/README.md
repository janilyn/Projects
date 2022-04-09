Level of Implementation: 'Level 3'

RUNNING THE PROGRAM:

To run the file_server, compile the program by entering**:
	'gcc file_server.c -lpthread -o file_server -std=c99'

After that, run the executable by entering**:
	'./file_server'

** remove the single quotes

----

IMPORTANT NOTE:	Be sure to wait for a couple of seconds before you exit the file server.
				Not waiting long enough might result to the worker threads exiting
				prematurely and unable to execute their commands. The waiting time
				is relative to the amount of commands entered. Exit at your own risk.

USER INPUT FORMAT:
•	Write:	'write <path/to/file/> <string>'
		NOTE: 	It is expected for the path to file to not have speces in between. 
				The characters at the right of the second space will be treated as
				part of the string.

•	Read:	'read <path/to/file/>'
•	Empty:	'empty <path/to/file/>'
		NOTE: 	It is expected for the path to file to not have speces in between. 	
				If there is a second space in the read/empty command entered, the said
				space and the characters on its right will be disregarded.

<path/to/file/> FORMAT:
•	when you want to do operations in the same file directory as the file server:
	./file.txt
	file.txt
	/absolute/path/to/file.txt

•	when you want to do operations to a file in the parent directory:
	../file.txt
	/absolute/path/to/file.txt

•	when you want to do operations to a different directory in the parent directory:
	../path/to/file/file.txt
	/absolute/path/to/file.txt

NOTE:	cannot create new directories when write wants to access a non-existent directory

