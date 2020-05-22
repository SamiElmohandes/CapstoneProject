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

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

## API Documentation

### Introduction

* Base URL:  This application's backend is hosted at http://127.0.0.1:5000/
* Authentication: This API does not require authentication.

### Error Handling
Errors are returned in JSON format as following:

 
    {
      "success": False,
      
      "error": 404,
      
      "message": "not found"
    }
    
    {
      "success": False,
      "error": 422,
      "message": "unprocessable "
    }
    
    {
      "success": False,
      "error": 400,
      "message": "bad request"
    }
    
    {
      "success": False,
      "error": 500,
      "message": "Internal Server Error"
    }
    


The API will return the following error types:

* 400: bad request
* 404: resource not found
* 422: unable to process request
* 500: internal server error

### Endpoints
#### GET /categories
* Fetches a dictionary of all available categories
* Request arguments: None
* Curl Sample: curl http://127.0.0.1:5000/categories
* Sample Response   
   
           {
            "categories": [
            "Science",
            "Art",
            "Geography",
            "History",
            "Entertainment",
            "Sports"
              ],
            "success": true

        }

#### GET /questions
* Fetches a dictionary of all questions from all categories
* Request arguments: None
* Curl Sample: curl http://127.0.0.1:5000/questions OR http://127.0.0.1:5000/questions?page=[number]
* Sample Response   
   
           {
          "answer": "Agra",
          "category": 3,
          "difficulty": 2,
          "id": 15,
          "question": "The Taj Mahal is located in which Indian city?"

            }, 
             "success": true,
             "totalQuestions": 27

             }
             
             
             
#### DELETE /questions/<question_id>
* Deletes the question with the specified ID
* Request arguments: question_id
* Curl Sample: curl -X "DELETE" http://localhost:5000/questions/<question_id>
* Sample Response

         {
           "deleted": 2,
           "success": true

             }
             
             
#### POST /questions
* Adds a new question 
* Request arguments: question_question , question_answer , question_difficulty , question_category
* Curl Sample: curl -X POST -H "Content-Type: application/json" -d '{"question":"value1","answer":"value2","difficulty":"2","category":"3"}' http://localhost:5000/questions

* Sample Response

         {
           "success": true
            
            }
             
#### SEARCH /questions    
* Searches for a question with the keyword provided 
* Request arguments: SearchTerm
* Curl Sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "beetle"}'
* Sample Response

         {
           "questions": [
         {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
       }
       ],
       "success": true,
       "totalQuestions": 1
       }
   
   
#### GET QUESTIONS BY CATEGORY /categories/<int:id>/questions
* Searches for questions within the specified category. 
* Request arguments: Category ID
* Curl Sample: curl http://127.0.0.1:5000/categories/(category_id)/questions
* Sample Response

      {
      "currentCategory": "Science"
      "questions": [
        {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
       },
      {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
       },
       {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
      }
      ],
      "success": true,
      "totalQuestions": 3
       }
        
        
#### POST QUIZ /quizzes
* Play the quiz . 
* Request arguments: previous_questions , quiz_category
* Curl Sample Example: curl curl -X POST http://localhost:5000/quizzes -d'{"previous_questions": [5,9], "quiz_category": {"id": 4, "type":   "History"}}' -H "Content-Type: application/json"


* Sample Response

      {
      "question": {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
       },
      "success": true
        }
        
        
        
