import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie 
#, db_drop_and_create_all


executive_producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR5WE5VaEJIWmxFaDRVYmVMOTJzLSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMTUxMTI0MGZhNTYwYzc1NjQ2ZDBlIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTU5MDAxMTk4OCwiZXhwIjoxNTkwMDk4Mzg4LCJhenAiOiJpUkRSRFczSnNKVjJ2S1FFN3EwMklqVnpRdEpZekIwUSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.W2aA_HJHQCjQSCVwtEGtcIsDP9397_EfFXF0SiCdzzRrMiF1jCW68vZDXPryoAkR1JbNd2Mk9K_qS5Renf4fSlfOQwE1HOpBn7GWvHfKIscDcQwUyZ3mnoielhtOU1zbWhD0cUO7zz3f0lOSBF7cm9E41-o1vmBiqQIApqPXBRg-cDS63JyxlSjAs_NlOLbUCB-bL5nwhdkw5kVSOJarkwdUenJsddZ6O02gBLwmF5Op9BP5f_URjoyYEC6xwET-EeNDG7Qv2DY8HsWw7KEWOhwzGPWX5JyoDKRIIK9RE4OhSWxCpU5fa5Vst5m43E0CLaMvcFjmjUmivKm2Y-xnTw'
casting_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR5WE5VaEJIWmxFaDRVYmVMOTJzLSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMTRlMjY0NTNlMjMwYzcxZDkyN2EyIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTU5MDAxMjA4MCwiZXhwIjoxNTkwMDk4NDgwLCJhenAiOiJpUkRSRFczSnNKVjJ2S1FFN3EwMklqVnpRdEpZekIwUSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.h_m3sDMZRjSktVIytsDml67udfAL2WsJxYFGhoe3r2dic0Ckl6VF_fdgTsTm8ZTsv2BvcX0Gg83x0jZXE8HAzjOP73h5mfnkzYqvuRoc82MjybTLJONqDWyQZ_HCjoyLWGX8H9xcp7slqr4h5LEzXRD2g4HHWPeYcI_67KiaeukTcbQ2YOYgnKTnFI7vmWKqOxlYqwBnRZ6FuqxQLnTo7fQUh83uQN3yJVR1_OS0uTvWTo8kQJiSv0yIHCHJFTLp4KXFD8y1EJj70NsXK61pNGJ58avRRD4pe4VI23Y8shCtbwq42mLuHLw_nbXOM2QgwFtYeLHxfOqtfbq0M2SZ7Q'
casting_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR5WE5VaEJIWmxFaDRVYmVMOTJzLSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMTRmZjM0MGZhNTYwYzc1NjQ2YjI0IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTU5MDAxMjIwNSwiZXhwIjoxNTkwMDk4NjA1LCJhenAiOiJpUkRSRFczSnNKVjJ2S1FFN3EwMklqVnpRdEpZekIwUSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.AEOiI0_32LqbNeVz5agVCimNwCQuMo_axkTJolsG57eWY2v8rJuto0nJfS64u1PC-GSCqla6wscP0YbRCx3D3iLvl-igBm8aGaY4Q44haMUHsODZblfeC_qXNF4S-zOi2jziVuemLEYR85cn0a33DZ9BiZ84dKLx1UzBEsY6Q8UFkKk4Pbf4FF4EZrakhLm2pMq_KhWIyRAAecaOo8K4-oWBCUvrTEQoHC6mLR-7K2E2JfIbWxV933J0DtkiDq2i0noW7C0jMXIraMz09ZEcbzXjlmTcf1Dj-VJAjtduDgnmnRtZ30lKSVTwL7asT1_pBAy68qTCQihvl7pV-EIBgQ'
class CapstoneTest(unittest.TestCase):
    def setUp(self):
        #self.token_assistant = os.environ['assistant_token']
        #self.token_director = os.environ['director_token']
        #self.token_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR5WE5VaEJIWmxFaDRVYmVMOTJzLSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMTRlMjY0NTNlMjMwYzcxZDkyN2EyIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTU4OTgzODYxNywiZXhwIjoxNTg5ODQ1ODE3LCJhenAiOiJpUkRSRFczSnNKVjJ2S1FFN3EwMklqVnpRdEpZekIwUSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.LFyJYwy9y7gyyXqOii5QNU1q-a5IbbwzPN2IjPRx_E10pHatXxk_rPeh6Ynb_Lzk8noWAVynXwukHZsudOO8jjH71kSF_2H1VyNvv4y7pmkbv6YOtKiHjTTEOqiej-C1l3EtBWjc1dUtSwSWryyt_nq7xiTalHYkB9THIwUFyb7CEs59RXsBMHk8hwDQ3MCd1D1zIq2PHqY4S_LjFrcdI8NIeq5KKKU5V3RFzp-9dSEqKmZC_W2AfxQIbaaSO43vIk3x08CeR4GxIHdu_ynSrDPIPclfLSodk9EaFMsc5zJ73WvV8KnNHZtlCntYygU7hWOCbdlVMMLgRGbaFSjfzg'
        #self.token_producer = os.environ['producer_token']
        # executive_producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR5WE5VaEJIWmxFaDRVYmVMOTJzLSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMTUxMTI0MGZhNTYwYzc1NjQ2ZDBlIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTU4OTgzOTE0MSwiZXhwIjoxNTg5ODQ2MzQxLCJhenAiOiJpUkRSRFczSnNKVjJ2S1FFN3EwMklqVnpRdEpZekIwUSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.eUdqiJBqmiNGQzSgfcXLHW-D6c6qMwnQR-rPbTlaBV8Kmjh44fRav_zmrWzbdq_4YAkzOK43BQ7FavGDbtc9PT-sstQIRRMdgEyH9zCgPFMr4VnU7TuMOd6yRnpLM-iiBNDGuJ9hK1OvX0h6zgGXtfmICu8JzJDf_x9ZBJ7lYs7lzQFah99dQsWibpf-ex4yuF3qx0TVZpNpv2AZ3XYu9GPu8UK8MU6_wvy0HrebHo2AaLrqp2RjnL5gHKlQHg4ZZgvy7QEtnB8waRwyQUwfa3D0tQJSGmtG6EZso_jxQk36-5QJ2v_Ex7MLOVEhkkrhamajEF9ykcsRvtnNWuGf2A'
        #self.token_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR5WE5VaEJIWmxFaDRVYmVMOTJzLSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMTRmZjM0MGZhNTYwYzc1NjQ2YjI0IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTU4OTgzOTQyMiwiZXhwIjoxNTg5ODQ2NjIyLCJhenAiOiJpUkRSRFczSnNKVjJ2S1FFN3EwMklqVnpRdEpZekIwUSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.c5EdHPjA3PuIvG2TBuQ_o0joeVzAfz4bHww9LRTE3E4JEOWbn11DNu26TeX6rX1WFeFFOLebf9jQX90F2yUSvHURCKGsm4qYvhUBZADwMh_6TwRuT5qMtf4CeCPZSsdlSbmc_AO9-6Ft1dO16kNXTfUnKgvnshUIUw1vTIDW-YGxa_LKvHqXNYTW_P3PQlpkkz1YfYy3KZQKgEB3ZxGXpi0qJT0i5yZzJUSVyrvHUxbKUj-EFN_g32RuVC668fmtxcSrkUlaCT2g1vBPHE2vqNlnraIi3gZMON6NY-OXY7X8YZenYgLuObaIa-YitEIgi9ThQvKn188VmdEDcCFONw'
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = 'postgresql://postgres@localhost:5432/capstone_test'
        #db_drop_and_create_all()
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'New Year',
            'release_date': '6/2019',
            # 'actor_ID' : '1'
        }

        self.new_actor = {
            'name': 'Daleeee',
            'age': '25',
            'gender': 'Male',
            # 'movie_ID' : '3'
        }
      
      
      
      
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    
    
    
    def test_create_Actor(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor ,
            headers={"Authorization": 'Bearer '+executive_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success '], True)    
   
   

    def test_create_Movie(self):
        res = self.client().post(
            '/movies',
            json={
                "title": "johnn",
                "release_date": "10/2010",
                 },
            headers={"Authorization": 'Bearer '+executive_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success '], True)




    def test_get_Actors(self):
        res = self.client().get('/actors', headers={
            "Authorization": 'Bearer '+casting_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success '], True)

    def test_get_Movies(self):
        res = self.client().get('/movies', headers={
            "Authorization": 'Bearer '+ casting_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success '], True)

    
    def test_delete_Actor(self):
        res = self.client().delete('/actors/1', headers={
            "Authorization": 'Bearer '+executive_producer})
        body = json.loads(res.data)
        actor = Actor.query.filter_by(id=1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success '], True)
        self.assertEqual(actor, None)

    
    def test_404_Wrong_ID_delete_Actor(self):
        res = self.client().delete('/actors/1000', headers={
            "Authorization": 'Bearer '+executive_producer})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success '], False)

    def test_401_Unauthorized_Permission_delete_Actor(self):
        res = self.client().delete('/actors/2', headers={
            "Authorization": 'Bearer '+casting_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success '], False)
    

    def test_delete_Movie(self):
        res = self.client().delete('movies/1', headers={
            "Authorization": 'Bearer '+executive_producer})
        body = json.loads(res.data)
        movie = Movie.query.filter_by(id=1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success '], True)
        self.assertEqual(movie, None)




 
    def test_401_Unauthorized_Permission_create_Actor(self):
        res = self.client().post(
            '/actors',
            json={
                "name": "johnnnnnnyn",
                "age": "10",
                "gender": "Male"
               },
            headers={"Authorization": 'Bearer '+casting_assistant}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success '], False)




    


    def test_update_Movies(self):
        res = self.client().patch(
            '/movies/2',
            json={
                "name": "Sameha",
                "release_date": "12-12-2012"
                },
            headers={"Authorization": 'Bearer '+executive_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success '], True)


    def test_update_Actors(self):
        res = self.client().patch(
            '/actors/2',
            json={
                "name": "Amir karara",
                "age": "100",
                "gender": "Sa3qaa"
                   },
            headers={"Authorization": 'Bearer '+executive_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success '], True)


if __name__ == "__main__":
    unittest.main()