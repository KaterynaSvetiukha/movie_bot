import json

def get_films(db:str = 'data.json', film_id:int|None = None):
    with open(db, 'r') as file:
        films = json.load(file)

        if film_id != None and film_id < len(films):
            return films[film_id]

        return films
