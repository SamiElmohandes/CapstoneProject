import os
from flask import Flask, request, abort, jsonify , render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie 
#, db_drop_and_create_all
import json
from auth import AuthError, requires_auth


#Test for deploying 
#Test
#Test
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


  @app.after_request
  def after_request(response):
     response.headers.add('Access-Control-Allow-Headers','Content-Type ,Authorization')
     response.headers.add('Access-Control-Allow-Methods','GET, POST ,PATCH , DELETE ,OPTIONS')
     #response.headers.add('Access-Control-Allow-Origin' ,  'http://localhost:3000')
     return response


  @app.route('/')
  def index():
    return jsonify({'message' : 'Hello'})
  

  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(payload):
   try:
    selection = Actor.query.all()
    actors = [actor.format() for actor in selection]
    return jsonify({
      'success ': True ,
      'Actors': actors,
      'Total_no_of_actors' : len(actors)
        }),200
   except:
    abort(500)


  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):
   try:
     selection = Movie.query.all()
     movies = [movie.format() for movie in selection]

     return jsonify({
      'success ': True ,
      'movies': movies,
      'no_of_movies' : len(movies)
        }),200
   except:
     abort(500)

  

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def create_actor(payload):
   
   body = request.get_json()
   new_name = body.get('name', None)
   new_age = body.get('age', None)
   new_gender = body.get('gender', None)
   existing_actor = Actor.query.filter(Actor.name == new_name).one_or_none()

   if existing_actor: 
    abort (400)
   
   
   try:
    
    actor = Actor(name=new_name, age=new_age, gender=new_gender)
    # movies = Movie.query.filter(Movie.id == body['movie_ID']).one_or_none()
    # actor.movies = [movies]
    actor.insert()
    return jsonify({
                'Existinggg': existing_actor,
                'success ': True
            }),200

   except:
    abort(422)





  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def create_movie(payload):
   try:
    body = request.get_json()
    new_title = body.get('title', None)
    new_release_date = body.get('release_date', None)
    existing_movie = Movie.query.filter(Movie.title == new_title).one_or_none()
    if existing_movie:
      abort (400)
    movie = Movie(title=new_title, release_date=new_release_date)
    # actors = Actor.query.filter(
    #             Actor.id == body['actor_ID']).one_or_none()
    # movie.actors = [actors]
    movie.insert()
    return jsonify({
                'success ': True
            }),200

   except:
    abort(422)


  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(payload,actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
        abort(404)
    
    actor.delete()

    return jsonify({
                'success ': True,
                'deleted': actor_id,
            }),200


  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload,movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
        abort(404)
    
    movie.delete()

    return jsonify({
                'success ': True,
                'deleted': movie_id,
            }),200


  
  
  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def patch_actors(payload, id):
    body = request.get_json()
    try:
        patch_name = body.get('name')
        patch_age = body.get('age')
        patch_gender = body.get('gender')
        if patch_name is None and patch_age is None and patch_gender is None :
            abort(400)
        # check if id is already present
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor is None:
            abort(404)
        
        if patch_name:  
            actor.name = patch_name

        if patch_age:
            actor.age = patch_age
        
        if patch_gender:
            actor.gender = patch_gender

        actor.update()
        return jsonify({
            'success ': True,
            'actor': actor.format()
        }), 200
    except Exception:
        abort(422)

  

  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def patch_movies(payload, id):
    body = request.get_json()
    try:
        # check if id is already present
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if movie is None:
            abort(404)
            
        patch_title = body.get('title')
        patch_release_date = body.get('release_date')

        if patch_title is None and patch_release_date is None :
            abort(400)
        
        if patch_title:
            movie.title = patch_title

        if patch_release_date:
            movie.release_date = patch_release_date
        


        movie.update()
        return jsonify({
            'success ': True,
            'movie': movie.format()
        }), 200
    except Exception:
        abort(422)






  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success ": False,
      "error": 404,
      "message": "not found"
    }), 404

  @app.errorhandler(422)
  def unprocessable_entity(error):
    return jsonify({
      "success ": False,
      "error": 422,
      "message": "unprocessable "
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success ": False,
      "error": 400,
      "message": "bad request"
    }), 400
  
  @app.errorhandler(500)
  def not_allowed(error):
    return jsonify({
      "success ": False,
      "error": 500,
      "message": "Internal Server Error"
    }), 500


  @app.errorhandler(AuthError)
  def auth_error(error):
    return jsonify({
                    "success ": False, 
                    "error": error.status_code,
                    "message": error.error['description']
                    }), error.status_code





  return app





app = create_app()

if __name__ == '__main__':
  #app.run(host='0.0.0.0', port=5000, debug=True)
  app.run(host='127.0.0.1', port=5000, debug=True)