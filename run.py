from FlaskSite import app
from sys import argv # to take input arguments from script 

# run it as admin if you gave it any tow input argu
if len(argv) ==2:
	root = True
else:
	root = False

if __name__ == '__main__':
	if root:
		app.run(host="0.0.0.0",port=5000) # this tell the framework to run it on privte ip
	else:
		app.run(debug=True) # run it on localhost with debug mode on



"""
This is the server alias 
put it in .bachrc to make alias
alias em='cd /home/muhammed/E-memeory/E-memory-main/ && nohup python3 run.py &'
alias EM="cd /home/muhammed/E-memeory/E-memory-main/ && nohup python3 run.py 1 & "


"""

