### INSTALLATION
1. install python [here](https://www.python.org/downloads/release/python-362/)
2. On windows, open command prompt with administrator rights. On mac open terminal and type sudo su
3. cd to CHAINSTACK directory (same directory as this README) in the command prompt or terminal
4. For windows, in command prompt, type .\venv\Scripts\activate.bat. For mac, in terminal, type source ./venv/Scripts/activate
5. On the same command prompt or terminal, type python manage.py runserver

### logging into administration
1. Open a web browser, go to http://localhost:8000/admin
2. type in chainstack@gmail.com as email
3. type in chainstack as password
4. press enter

### create user using administration
1. login to administration
2. click on '+Add' in the Users section
3. Fill in the form
4. click SAVE

### create resource using administration
1. login to administration
2. click on '+Add' in the Resource section
3. Fill in the form
4. click SAVE


### Change database
You can change the database by first install and running the database and then changing the DATABASES dictionary in CHAINSTACK/stack/settings.py

### Running the automated tests
1. After installation, control c to stop the server from running
2. on the same command prompt or terminal, type python manage.py test