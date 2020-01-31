import os
import json

class DB_json:

    @staticmethod
    def read():
        path = '/home/murilo/Desktop/Estudos/Web/Python/restful-app/db/'
        filename = 'db.json'
        db = os.path.join(path, filename)

        with open(db, 'r') as read:
            DB = json.load(read)
        return DB

    @staticmethod
    def save(hotel):
            path = '/home/murilo/Desktop/Estudos/Web/Python/restful-app/db/'
            filename = 'db.json'
            db = os.path.join(path, filename)
            with open(db, 'w', encoding='utf8') as write:
                json.dump(hotel, write, indent=4)