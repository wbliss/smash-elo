from app import app, db
from models import Character, User, UserCharacter, Match
from elo import calculate_elo

from flask import flash, g, redirect, render_template, request, session, jsonify, escape
from datetime import datetime
from sqlalchemy import and_

@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        
        name = request.form.get('name')
        wuser = request.form.get('wuser')
        wchar = request.form.get('wchar')
        luser = request.form.get('luser')
        lchar = request.form.get('lchar')

        if name:
            user = User.query.filter_by(name=name).first()
            if not user:
                user = User(name)
                db.session.add(user)
                db.session.commit()
        
        #if new match add match and calculate elo
        if wuser and wchar and luser and lchar and (wuser != luser):
            
            winner_user = User.query.filter_by(id=wuser).first()
            loser_user = User.query.filter_by(id=luser).first()

            winner_userchar = UserCharacter.query.filter(and_(UserCharacter.user == wuser, UserCharacter.character == wchar)).first()
            if not winner_userchar:
                winner_userchar = UserCharacter(wuser, wchar)
            
            loser_userchar = UserCharacter.query.filter(and_(UserCharacter.user == luser, UserCharacter.character == lchar)).first()
            if not loser_userchar:
                loser_userchar = UserCharacter(luser, lchar)

            w_pre_ov = winner_user.overall
            l_pre_ov = loser_user.overall
            w_pre_char = winner_userchar.rating
            l_pre_char = loser_userchar.rating

            new_elos_ov = calculate_elo(w_pre_ov, l_pre_ov, 32,32)
            new_elos_char = calculate_elo(w_pre_char, l_pre_char, 32,32)
            
            winner_user.overall = new_elos_ov.get('winner')
            loser_user.overall = new_elos_ov.get('loser')
            winner_userchar.rating = new_elos_char.get('winner')
            loser_userchar.rating = new_elos_char.get('loser')
            new_match = Match(datetime.now(), wuser, luser, wchar, lchar, w_pre_ov, w_pre_char, l_pre_ov, l_pre_char, winner_user.overall, winner_userchar.rating, loser_user.overall, loser_userchar.rating)
            db.session.add(winner_user)
            db.session.add(loser_user)
            db.session.add(winner_userchar)
            db.session.add(loser_userchar)
            db.session.add(new_match)
            db.session.commit()
            
    users = User.query.all()
    characters = Character.query.all()  
    
    return render_template('index.html', users=users, characters=characters) 

if __name__ == "__main__":
    app.run()