from app import app, db

class Character(db.Model):
    __table_args__ = {'schema' : 'smash'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        
        self.name = name

    def serialize(self):
        return { 
        'id' : self.id,
        'name' : self.name
        }

class UserCharacter(db.Model):
    __table_args__ = {'schema' : 'smash'}

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('smash.user.id'), index=True)
    character = db.Column(db.Integer, db.ForeignKey('smash.character.id'), index=True)
    rating = db.Column(db.Integer)

    def __init__(self, user, character):

        self.user = user
        self.character = character
        self.rating = 1200

    def serialize(self):
        return { 
        'id' : self.id,
        'user' : self.user,
        'character' : self.character,
        'rating' : self.rating
        }

class MatchDetails(db.Model):
    __table_args__ = {'schema' : 'smash'}

    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('smash.match.id'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('smash.user.id'), index=True)
    char_id = db.Column(db.Integer, db.ForeignKey('smash.character.id'), index=True)
    pre_ov = db.Column(db.Integer)
    pre_char = db.Column(db.Integer)
    post_ov = db.Column(db.Integer)
    post_char = db.Column(db.Integer)
    user = db.relationship('User', foreign_keys=[user_id])
    char = db.relationship('Character', foreign_keys=[char_id])

    def __init__(self, match_id, user_id, char_id, pre_ov, pre_char, post_ov, post_char):

        self.match_id = match_id
        self.user_id = user_id
        self.char_id = char_id
        self.pre_ov = pre_ov
        self.pre_char = pre_char
        self.post_ov = post_ov
        self.post_char = post_char


    def serialize(self):
        return { 
        'id' : self.id,
        'match_id' : self.match_id,
        'user_id' : self.ser_id,
        'char_id' : self.char_id,
        'pre_ov' : self.pre_ov,
        'pre_char' : self.pre_char,
        'post_ov' : self.post_ov,
        'post_char' : self.post_char,
        }

class User(db.Model):
    __table_args__ = {'schema':'smash'}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    overall = db.Column(db.Integer)
    characters = db.relationship(UserCharacter)

    def __init__(self, name):

        self.name = name
        self.overall = 1200

    def serialize(self):
        return { 
        'id' : self.id,
        'name' : self.name,
        'overall' : self.overall
        }

class Match(db.Model):
    __table_args__ = {'schema':'smash'}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    datetime = db.Column(db.DateTime)
    winner = db.Column(db.Integer, db.ForeignKey('smash.user.id'), index=True)
    loser = db.Column(db.Integer, db.ForeignKey('smash.user.id'), index=True)
    details = db.relationship(MatchDetails)

    def __init__(self, datetime, winner, loser):

        self.datetime = datetime
        self.winner = winner
        self.loser = loser


     