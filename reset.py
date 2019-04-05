from models import *
import csv

def import_characters():
    
    character_reader = csv.reader(open('characters.csv'))
    for row in character_reader:
       db.session.add(Character(row[0]))

    db.session.commit()

def main():
    db.drop_all()
    db.create_all()
    import_characters()

if __name__ == '__main__':
    main()

