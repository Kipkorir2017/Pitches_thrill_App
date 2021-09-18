from . import db
from datetime import datetime


class User(db.Model):
    """ 
    class modelling the users 
    """
    __tablename__='users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
    



class Pitch(db.Model):
    """
    List of pitches  
    """

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_category = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)




    # all_pitches=[]
    # def __init__(self,pitch_id,pitch_title,postedOn):
    #     self.pitch_id=pitch_id
    #     self.pitch_title=pitch_title
    #     self.postedOn=postedOn
        
        
    def save_pitch(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls,pitch_title):

        response = []

        for pitch in cls.all_pitches:
            if pitch.pitch_title == pitch_title:
                response.append(pitch)

        return response

    # @classmethod
    # def displayPitches():




            

   
