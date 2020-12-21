# Team Management

## Setup

For debian based linux

###  Clone the repo
```sh
git clone https://github.com/shobhitvashistha/team.git
```

### Install MySQL and create database

```sh
sudo apt install python3-dev
sudo apt install libmysqlclient-dev default-libmysqlclient-dev
sudo apt install mysql-server
```
Open MySQL shell as root user
```sh
sudo mysql -u root
```
Create a database named `team_db`
```mysql
CREATE DATABASE team_db;
```
Create user
```mysql
CREATE USER 'team_user'@'%' IDENTIFIED WITH mysql_native_password BY 'team_db_pass';
```
Grant privileges
```mysql
GRANT ALL ON team_db.* TO 'team_user'@'%';
```
```mysql
FLUSH PRIVILEGES;
```
Edit `my.cnf` file to add credentials
```sh
sudo vim /etc/mysql/my.cnf
```
add following to the end of the file
```
[client]
database = team_db
user = team_user
password = team_db_pass
default-character-set = utf8
```
Restart MySQL service
```sh
sudo systemctl daemon-reload
sudo systemctl restart mysql
```

### Setup virtual environment

Install packages that may be needed for a stable python3 environment
```sh
sudo apt-get install python3-pip
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt-get install python3-venv
```
Create a virtual environment
```sh
python3 -m venv env
```
Activate it
```sh
source env/bin/activate
```
Navigate to `team/` i.e. root directory of the project and install packages from `requirements.txt` using `pip`
```sh
pip install -r requirements.txt
```
Apply migrations to the database
```sh
python manage.py migrate
```
Start the development server
```sh
python manage.py runserver
```
Development server should now be running at http://127.0.0.1:8000/

## API Usage

### Creating a team member

`POST /api/v1/team-members`

```sh
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/api/v1/team-members -d '
{"first_name": "John", "last_name": "Wick", "phone_number": "+19999988888",
"email": "johnwick@excommunicado.com", "role": "admin"}'
```
Status
```
HTTP/1.1 201 Created
```
Response Body
```json
{
  "id":1,
  "first_name":"John",
  "last_name":"Wick",
  "phone_number":"+19999988888",
  "email":"johnwick@excommunicado.com",
  "role":"admin"
}
```

### Listing all team members

`GET /api/v1/team-members`

```sh
curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/api/v1/team-members
```
Status
```
HTTP/1.1 200 OK
```
Response Body
```json
[
  {
    "id":1,
    "first_name":"John",
    "last_name":"Wick",
    "phone_number":"+19999988888",
    "email":"johnwick@excommunicado.com",
    "role":"admin"
  }
]
```

### Getting details a team member with given id

`GET /api/v1/team-members/:id`
```sh
curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/api/v1/team-members/1
```
Status
```
HTTP/1.1 200 OK
```
Response Body
```json
{
  "id":1,
  "first_name":"John",
  "last_name":"Wick",
  "phone_number":"+19999988888",
  "email":"johnwick@excommunicado.com",
  "role":"admin"
}
```

### Editing team member details

`PUT /api/v1/team-members/:id`

```sh
curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/api/v1/team-members/1 -d '
{"first_name": "Keanu", "last_name": "Reeves", "phone_number": "+19999977777"}'
```
Status
```
HTTP/1.1 200 OK
```
Response Body
```json
{
  "id":1,
  "first_name":"Keanu",
  "last_name":"Reeves",
  "phone_number":"+19999977777",
  "email":"johnwick@excommunicado.com",
  "role":"admin"
}
```

### Deleting a team member

`DELETE /api/v1/team-members/:id`

```sh
curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/api/v1/team-members/1
```
Status
```
HTTP/1.1 204 No Content
```
Response Body (empty)
```json
```