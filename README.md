# Full Stack API Final Project

## Casting Agency

Udacity is invested in creating bonding experiences for its employees and students. It has been an honor and quite an interesting challenge working on this course where I got exposed to great course content and projects.

This is the final project in the course where we were tasked with building a web app for a casting agency where users can add movies and actors. This project uses python, flask and postgresql for it's backend and is hosted on heruko.

1) The code such as (app.py , models.py , test_app.py) adheres to PIP8 style guidelines

2) No frontend is developed for this app, you can use it using Curl or Postman

3) Database modeling with postgres & sqlalchemy (see models.py)

4) API to performance CRUD Operations on database with Flask (see app.py)

5) Automated testing with Unittest (see test_app)

6) Authorization RBAC with Auth0 (see auth.py)

7) Postman Collection of Endpoints tests (see CapstoneCollection.postman_collection)

8) Deployment on Heroku (access this app through the following link --> https://finalfsndagency.herokuapp.com/ )



## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for the platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the API Locally 

It is important to make sure the virtual environment is activated with all the dependencies installed and in place in the directory .

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app.py
flask run --reload
```
Note : The command `source setup.sh` sets some environment variables used by the app.

Testing
To run the tests, run

```bash 
$ python test_app.py
```
It should give this response if everything went fine:

```bash
$ python test_app.py
...........
----------------------------------------------------------------------
Ran 11 tests in 15.376s

OK

```


## API Documentation

### Introduction

* Base URL:  https://finalfsndagency.herokuapp.com/

* Authentication: This app has 3 users. Each has his own token which are provided in setup.sh file. Details about each user privlages are provided below.

### Error Handling
Errors are returned in JSON format as following:

 
    {
      "success ": False,
      
      "error": 404,
      
      "message": "not found"
    }
    
    {
      "success ": False,
      "error": 422,
      "message": "unprocessable "
    }
    
    {
      "success ": False,
      "error": 400,
      "message": "bad request"
    }
    
    {
      "success ": False,
      "error": 500,
      "message": "Internal Server Error"
    }


The last error handler uses AuthError which is set in the auth.py file .

    {
      "success ": False,
      "error": error.status_code,
      "message": error.description
    }



The API will return the following error types:

* 400: bad request
* 404: resource not found
* 422: unable to process request
* 500: internal server error

If the error stems from the Authorization or Authentication (auth.py)
* 400: bad request
* 401: Unauthorized Error


### Endpoints

- GET '/actors'
- GET '/movies'
- POST '/actors'
- POST '/movies'
- PATCH '/actors/<int:id>'
- PATCH '/movies/<int:id>'
- DELETE '/actors/<int:id>'
- DELETE '/movies/<int:id>'


Following is the demonstration of each endpoint.

#### GET /actors
```bash
$ curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X GET https://finalfsndagency.herokuapp.com/actors
```
  - Return a list of actors, number of actors, success value

```js
{
  "Actors": [
      {
        "age": 25,
        "gender": "Male",
        "id": 1,
        "name": "Sami Elmohandes"
      }
  ],
  "Total_no_of_actors": 1
  "success ": true,
}
```
#### GET /movies
```bash
$ curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X GET https://finalfsndagency.herokuapp.com/movies
```
  - Return a list of movies, number of movies, success value

```js
{
  "movies": [
      {
        "id": 1,
        "release_date": "8/2008",
        "title": "The Dark Knight",
      }
  ],
  "no_of_movies": 1
  "success ": true,
}
```

#### POST /actors
```bash
$ curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' -d '{"name":"Amir","age":24,"gender":"male"}' https://finalfsndagency.herokuapp.com/actors
```

  - Create a new actor using the submitted name, age, and gender. Return Existing parameter(null if success or else if another actor with the same name exists the existing actor record ), success value.


```js
{
  "Existing": null
  "success ": true,
}

```




#### POST /movies
```bash
$ curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' -d '{"title":"Hello All","release_date":"21/2121"}' https://finalfsndagency.herokuapp.com/movies
```

  - Create a new movie using the submitted title and release_date. Return Existing parameter(null if success or else if another actor with the same name exists the existing actor record ), success value.


```js
{
  "Existing": null
  "success ": true,
}

```

#### PATCH /actors
```bash
$ curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X PATCH -H 'Accept: application/json' -H 'Content-Type: application/json' -d '{"name":"Sam","age":24,"gender":"male"}' https://finalfsndagency.herokuapp.com/actors/1
```


  - Update the actor of the given ID if it exists using the submitted name, age, and gender. Returns the actor record modified and the success value.



```js
{
  "actor": 
      {
        "age": 24,
        "gender": "male",
        "id": 1,
        "name": "Sam"
      } ,
  "success ": true,
}
```


#### PATCH /movies
```bash
$ curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X PATCH -H 'Accept: application/json' -H 'Content-Type: application/json' -d '{"title":"Toy Story","release_date":"3/1994"}' https://finalfsndagency.herokuapp.com/movies/2
```


  - Update the movie of the given ID if it exists using the submitted title and release_date . Returns the movie record modified and the success value.



```js
{
  "actor": 
      {
        "id": 1,
        "title": "Toy Story",
	"release_date": "3/1994"
      } ,
  "success ": true
}
```


#### DELETE /actors

```bash
$ curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X DELETE https://finalfsndagency.herokuapp.com/actors/1
```


  - Deletes the actor of the given ID if it exists. Returns  deleted actor id and success value.


```js
{
  "deleted": 1
  "success": true,
  
}

```


#### DELETE /movies

```bash
$ curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X DELETE https://finalfsndagency.herokuapp.com/movies/1
```


  - Deletes the movie of the given ID if it exists. Returns  deleted movie id and success value.


```js
{
  "deleted": 1
  "success": true,
  
}

```


### Users

This app has 3 users. each user has his own privileges.

- Casting Assistant
	- Can view actors and movies

- Casting Director
	- All permissions of a Casting Assistant.
	- Add or delete an actor from the database
	- Modify actors or movies

- Executive Producer
	- All permissions of a Casting Director.
	- Add or delete a movie from the database

Please Note, to use any endpoint, you must send the request with user access token in Authorization header, which are provided in `setup.sh`.
