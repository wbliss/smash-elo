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

    def __init__(self, user, character, rating):

        self.user = user
        self.character = character
        self.rating = rating

    def serialize(self):
        return { 
        'id' : self.id,
        'user' : self.user,
        'character' : self.character,
        'rating' : self.rating
        }

class Match(db.Model):
    __table_args__ = {'schema' : 'smash'}

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    w_user_id = db.Column(db.Integer, db.ForeignKey('smash.user.id'), index=True)
    l_user_id = db.Column(db.Integer, db.ForeignKey('smash.user.id'), index=True)
    w_char_id = db.Column(db.Integer, db.ForeignKey('smash.character.id'), index=True)
    l_char_id = db.Column(db.Integer, db.ForeignKey('smash.character.id'), index=True)
    w_pre_ov = db.Column(db.Integer)
    w_pre_char = db.Column(db.Integer)
    l_pre_ov = db.Column(db.Integer)
    l_pre_char = db.Column(db.Integer)
    w_post_ov = db.Column(db.Integer)
    w_post_char = db.Column(db.Integer)
    l_post_ov = db.Column(db.Integer)
    l_post_char = db.Column(db.Integer)
    w_user = db.relationship('User', foreign_keys=[w_user_id])
    l_user = db.relationship('User', foreign_keys=[l_user_id])
    w_char = db.relationship('Character', foreign_keys=[w_char_id])
    l_char = db.relationship('Character', foreign_keys=[l_char_id])

    def __init__(self, datetime, w_user_id, l_user_id, w_char_id, l_char_id, w_pre_ov, w_pre_char, l_pre_ov, l_pre_char, w_post_ov, w_post_char, l_post_ov, l_post_char):

        self.datetime = datetime
        self.w_user_id = w_user_id
        self.l_user_id = l_user_id
        self.w_char_id = w_char_id

        self.l_char_id = l_char_id
        self.w_pre_ov = w_pre_ov
        self.w_pre_char = w_pre_char
        self.l_pre_ov = l_pre_ov
        self.l_pre_char = l_pre_char
        self.w_post_ov = w_post_ov
        self.w_post_char = w_post_char
        self.l_post_ov = l_post_ov
        self.l_post_char = l_post_char

    def serialize(self):
        return { 
        'id' : self.id,
        'datetime' : self.datetime,
        'w_user_id' : self.w_user_id,
        'l_user_id' : self.l_user_id,
        'w_char_id' : self.w_char_id,
        'l_char_id' : self.l_char_id,
        'w_pre_ov' : self.w_pre_ov,
        'w_pre_char' : self.w_pre_char,
        'l_pre_ov' : self.l_post_ov,
        'l_pre_char' : self.l_pre_char,
        'w_post_ov' : self.w_post_ov,
        'w_post_char' : self.w_post_char,
        'l_post_ov' : self.l_post_ov,
        'l_post_char' : self.l_post_char
        }

class User(db.Model):
    __table_args__ = {'schema':'smash'}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    overall = db.Column(db.Integer)
    characters = db.relationship(UserCharacter)

    def __init__(self, name, overall):

        self.name = name
        self.overall = overall

    def serialize(self):
        return { 
        'id' : self.id,
        'name' : self.name,
        'overall' : self.overall
        }


     