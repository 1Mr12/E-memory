from FlaskSite import app
from sys import argv

if len(argv) ==2:
	root = True
else:
	root = False

if __name__ == '__main__':
	if root:
		app.run(host="0.0.0.0",port=5000)
	else:
		app.run(debug=True)

"""

put it in .bachrc to make alias
alias em='cd /home/muhammed/E-memeory/E-memory-main/ && nohup python3 run.py &'
alias EM="cd /home/muhammed/E-memeory/E-memory-main/ && nohup python3 run.py 1 & "


"""
