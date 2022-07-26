from uvicorn import run
from application.main import app
from sys import argv
from os import _exit

run_port = 8000

try: 
    if len(argv) > 1:
        if argv[1] == 'help'.lower():
            print('You can change the port number by adding the port number after "python manage.py"')
            _exit(0) # normal termination of the program
        elif int(argv[1]) :
            run_port = argv[1]
except Exception as e:
    print('Error: ', e)
    print("You can use only 2 flags after 'python manage.py'")
    print("1. help. For e.g. python manage.py help")
    print("2. port number(int type value). For e.g. python manage.py 8002")

if __name__ == "__main__":
    print('Server running...')
    run(app, host="127.0.0.1", port=run_port)