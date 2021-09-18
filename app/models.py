class User:
    '''
    User class to define user objects
    '''
    



class Pitch:

    all_pitches=[]
    def __init__(self,pitch_id,pitch_title,postedOn):
        self.pitch_id=pitch_id
        self.pitch_title=pitch_title
        self.postedOn=postedOn
        
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




            

   
