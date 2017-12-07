from pymongo import MongoClient
import sys

client = MongoClient()
db = client['LogsUnitDB']
arguments = {
                'EventID' : 1,
                'TimeCreated': 2
            }

def insertRow():
    db.Logs.insert_one(
        {
            "EventId": sys.argv[arguments['EventID']],
            "Time": sys.argv[arguments['TimeCreated']]
        }
    )


if __name__ == '__main__':
    insertRow()
