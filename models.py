import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_name = "castingagency"
#database_path = "postgres://localhost:5432/castingagency"


database_path ='postgresql://postgres@localhost:5432/castingagency'

#database_path = os.environ['DATABASE_URL']



#database_path = os.environ.get('DATABASE_URL', 'postgres://iyrlacsqgsgzhw:7761bbdc56821fabff1b0a90b793bcd503b8a10d3a41d89931eb16423fe9c673@ec2-34-194-198-176.compute-1.amazonaws.com:5432/d60pq1ui1787g6')



db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)


# def db_drop_and_create_all():
#     db.drop_all()
#     db.create_all()
#     new_movie = Movie(title='King Kong', release_date='12/2019')
#     new_movie.insert()
#     new_actor = Actor(name='John', age=25, gender='male')
#     new_actor.insert()
    




# actors_movies = db.Table(
#   'actors_movies',  db.Model.metadata,
#   db.Column('actor_id', db.Integer,
#             db.ForeignKey('actors.id'), primary_key=True),
#   db.Column('movie_id', db.Integer,
#             db.ForeignKey('movies.id'), primary_key=True))
'''
Movies

'''

class Movie(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String(), nullable=False, default='')
  release_date = Column(String(), nullable=False, default='')
  # actors = db.relationship(
  #     'Actor',
  #     secondary=actors_movies,
  #     backref=db.backref('association', lazy='joined'))


  
  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date
    

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date,
      #'actors': [x.name for x in self.actors]
    }

'''
Actors

'''
class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String(), nullable=False, default='')
  age = Column(String(), nullable=False, default='')
  gender = Column(String(), nullable=False, default='')

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
    

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
      #'movies': [x.name for x in self.movies]
    }
