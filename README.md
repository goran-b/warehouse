#  Discount Ascii Warehouse
Proxy server made in Django
Live version: https://warehouse-django-server.herokuapp.com/api/users

## Motivation
This is an exercise task. It is necessary to create a proxy server that responds to special queries and returns json files. This is the text of the task:

Exam

Overview
For this exam you will be building a backend for a new feature of the Discount Ascii Warehouse ecommerce platform.
Your application will produce a list of "Popular purchases", so customers can see who else bought the same products as them. To complete the exam your application will need to accept HTTP requests to /api/recent_purchases/:username and respond with a list of recently purchased products, and the names of other users who recently purchased them.
There is no frontend component to this exam, you're just building the backend.
Other requirements
●	your application must cache API requests so that it can respond as quickly as possible.
●	if a username is provided that cannot be found, the API should respond with "User with username of '{{username}}' was not found"
Where does the data come from?
Data about users, products and purchases is available to you via an API you can set up and host locally: https://github.com/x-team/daw-purchases/blob/master/README.md#api-reference

To work out the "Popular purchases":
●	fetch 5 recent purchases for the user: GET /api/purchases/by_user/:username?limit=5
●	for each of those products, get a list of all people who previously purchased that product: GET /api/purchases/by_product/:product_id
●	at the same time, request info about the products: GET /api/products/:product_id
●	finally, put all of the data together and sort it so that the product with the highest number of recent purchases is first.
Example response:
[
  {
    "id": 555622,
    "face": "｡◕‿◕｡",
    "price": 1100,
    "size": 27,



    "recent": [
      "Frannie79",
      "Barney_Bins18",
      "Hortense6",
      "Melvina84"
    ]
  },
  ...
]

## Code style

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)
 
## Screenshots

![Users](https://github.com/goran-b/warehouse/blob/master/screenshot-users.PNG)
![Popular purchases](https://github.com/goran-b/warehouse/blob/master/screenshot-popular-purchases-by-user.PNG)


## Tech/framework used

<b>Built with</b>
- [Django](https://www.djangoproject.com/)
- [Django rest framewok](https://www.django-rest-framework.org/)



## Features
This rest service receives data from the server(https://github.com/x-team/daw-purchases/blob/master/README.md#api-reference).
There are two endpoints that return the requested data.
Users: who returns a list of ten generated users and 
The Popular purchase: that returns an json file with information about the last purchases of a certain user and the name of other users who bought those products.


## Installation
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/goran-b/warehouse.git
$ cd warehouse
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd warehouse
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/`.

or live version : https://warehouse-django-server.herokuapp.com/api/


## API Reference

### GET users

- response (json):

```
{
  "users": [
    {
      "username": (string),
      "email": (string)
    },
    ...
  ]
}
```

### GET recent_purchases/:username 

- params:
  - username (string)

- response (json):

```
[    
    {
        "id": (string),
        "face": (string),
        "price": (number),
        "size": (number),
        "recent": [
            (string),
            (string),
            ...
        ]
    },
    ...
]
```




## Tests
//to do




MIT © [goran-b]()
