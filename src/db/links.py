from src.db.mongo import get_bucket, get_database
from bson import ObjectId

def update_bucket_id_in_link(id, bucket_id):
    db = get_database()
    coll = db['links']

    coll.update_one(
        {'_id': ObjectId(id)},
        {'$set' : {'bucket_id': bucket_id}} 
    )

def add_link_to_bucket(link):
    bucket = get_bucket()
    bucket_obj = bucket.put(link, filename='example.mp3', content_type='audio/mp3')
    print(bucket_obj)
    return bucket_obj


# if __name__ == "__main__":   
#    dbname = get_database()