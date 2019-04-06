### INSTALLATION
1. install python [here](https://www.python.org/downloads/release/python-362/)
2. On windows, open command prompt with administrator rights. On mac open terminal and type sudo su
3. install git [here](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
4. on the command prompt or terminal, type git clone https://github.com/puaykaipoh/CHAINSTACK.git
5. cd to CHAINSTACK directory (same directory as this README) in the command prompt or terminal
6. For windows, in command prompt, type .\venv\Scripts\activate.bat For mac, in terminal, type source ./venv/Scripts/activate
7. On the same command prompt or terminal, type python manage.py runserver

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

### Testing the REST API for logging in
1. install [curl](https://help.ubidots.com/how-to-with-ubidots/learn-how-to-install-run-curl-on-windowsmacosxlinux)
2. On windows, open command prompt with administrator rights. On mac open terminal and type sudo su
3. type curl -d "email=chainstack@gmail.com&password=chainstack" -H "Content-Type: application/x-www-form-urlencoded" http://localhost:8000/users/api/login press enter
4. you will get a token, example {"token":"4e3a5af99d7bfd93bf5b97eed6c8e61467060c25"}, save the token (4e3a5af99d7bfd93bf5b97eed6c8e61467060c25) somewhere

### Testing list resources
1. install [curl](https://help.ubidots.com/how-to-with-ubidots/learn-how-to-install-run-curl-on-windowsmacosxlinux)
2. On windows, open command prompt with administrator rights. On mac open terminal and type sudo su
3. type curl -H "Authorization: Token <insert your token here>" http://localhost:8000/resources/ , example: curl -H "Authorization: Token 4e3a5af99d7bfd93bf5b97eed6c8e61467060c25" http://localhost:8000/resources/
4. you will get a list of resource ids

### Testing create resources
1. install [curl](https://help.ubidots.com/how-to-with-ubidots/learn-how-to-install-run-curl-on-windowsmacosxlinux)
2. On windows, open command prompt with administrator rights. On mac open terminal and type sudo su
3. type curl -X PUT -H "Authorization: Token <insert your token here>" http://localhost:8000/resources/ , example: curl -X PUT -H "Authorization: Token 4e3a5af99d7bfd93bf5b97eed6c8e61467060c25" http://localhost:8000/resources/
4. you will get the resource id that was created

### Testing delete resource
1. install [curl](https://help.ubidots.com/how-to-with-ubidots/learn-how-to-install-run-curl-on-windowsmacosxlinux)
2. On windows, open command prompt with administrator rights. On mac open terminal and type sudo su
3. curl -X DELETE -H "Authorization: Token <insert your token here>" -d "id=<insert resource id>" http://localhost:8000/resources/, example: curl -X DELETE -H "Authorization: Token 4e3a5af99d7bfd93bf5b97eed6c8e61467060c25" -d "id=a94a817b-2011-47a1-bc33-261a0f54fc9a" http://localhost:8000/resources/
4. you should get the outcome out deletion

### Change database
You can change the database by first install and running the database and then changing the DATABASES dictionary in CHAINSTACK/stack/settings.py
You may want to change database if you wish to have a dedicated database server or multiple database servers

### Running the automated tests
1. After installation, control c to stop the server from running
2. on the same command prompt or terminal, type python manage.py test