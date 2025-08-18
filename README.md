# http demo


## Init

```shell
# Creating a virtual environment
make venv

# Install project dependencies
make install

# Initialize or create a database
make migrate
```


## Start

```shell
# start server
make run

# new user
curl -X POST -H "Content-Type: application/json" -d '{"username": "value1"}' http://127.0.0.1:5000/test/adduser

# get users
curl -X GET http://127.0.0.1:5000/test/users
```
