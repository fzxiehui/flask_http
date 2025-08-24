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

## auth

- register

```shell
# register
curl -X POST -H "Content-Type: application/json" -d '{"username": "root", "password": "root"}' http://127.0.0.1:5000/auth/register
```

- login

```shell
curl -X POST -H "Content-Type: application/json" -d '{"username": "root", "password": "root"}' http://127.0.0.1:5000/auth/login
# {"code":200,"data":{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJyb290IiwiZXhwIjoxNzU2MDQ5Mjg3fQ.ds-vDrLzAPIqICHur2ukoGLA9nghhc64KSPvs_dRr_Q","username":"root"},"msg":"ok"}
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJyb290IiwiZXhwIjoxNzU2MDQ5Mjg3fQ.ds-vDrLzAPIqICHur2ukoGLA9nghhc64KSPvs_dRr_Q"
curl -X POST -H "Content-Type: application/json" -d '{"username": "root", "password": "root"}' http://127.0.0.1:5000/auth/login_required
```
