from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    """ 
    class modelling the users 
    """
    __tablename__='users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_hash,password)
    
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




    all_pitches=[]
    def __init__(self,pitch_id,pitch_title,postedOn):
        self.pitch_id=pitch_id
        self.pitch_title=pitch_title
        self.postedOn=postedOn
        
        
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls, category):
        pitches = Pitch.query.filter_by(pitch_category=category).all()
        return pitches
        # response = []

        # for pitch in cls.all_pitches:
        #     if pitch.pitch_title == pitch_title:
        #         response.append(pitch)

        # return response

    # @classmethod
    # def displayPitches():
# class Comments(db.Model):
#     """
#     comment model for each pitch 
#     """
#     __tablename__ = 'comments'

#     # add columns
#     id = db.Column(db.Integer, primary_key=True)
#     opinion = db.Column(db.String(255))
#     time_posted = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

#     def save_comment(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_comments(self, id):
#         comment = Comments.query.order_by(
#             Comments.time_posted.desc()).filter_by(pitches_id=id).all()
#         return comment




            

   
