# BankingSystem APIs_Django_REST_Framework

This project about banking system which include two APIs:

## UserBalance_API

It's a REST API which take userID as an input and it returns the user information like username, accountID and account balance
to access this API

## UserTransfer_API

It's a REST API which take senderID, receiverID, transferAmount and currency after sending these data to the server if the senderID and receiverID are valid and the sender Balance is enough the transfer process will done succcessfully

## Installed apps and Packages

```install mysql server using workbench```

```python -m pip install Django```

```pip install djangorestframework```

```pip install mysqlclient```

## Database setup

publish database on localhost with port 3306

## django commands

```python manage.py makemigrations````

```python manage.py migrate```

```python manage.py runserver```

## Access userBalance_API

by using this url

<http://127.0.0.1:8000/banksystems/userbalance/{userID}/>

## Access userTransfer_API

by using this url

<http://127.0.0.1:8000/banksystems/usertransfer/>

add the request like

{
    "senderID":{},
    "receiverID": {} ,
    "transferAmount":{} ,
    "currecy": {}
}