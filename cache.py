import redis
cache = redis.Redis(host="localhost", port=6379, decode_responses=True)

"""
Schema: book = {
            "book_title":self.book_title,
            "author":self.author,
            "desc":self.desc,
            "page_count":self.page_count,
            "key_words":self.key_words,
            "genre":self.genre,
            "uuid":str(uuid.uuid4()),
            "date_added":self.date,
            "deviation":float(self.deviation),
            "reading":True
        }

"""
def cache_init(mongo_schema):
    cache.mset(mongo_schema)
    return mongo_schema
