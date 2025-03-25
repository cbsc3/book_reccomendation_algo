from pymongo import MongoClient
import uuid
import datetime
import os
from cache import cache_init

key = os.environ.get("MONGO_KEY")
cluster = MongoClient(f'mongodb+srv://dbfoward:{key}@cluster0.9zntn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
books_db = cluster['book_data']
books_read = books_db['books_read']

#Retrieves the last book in the database - which will be employed after the quota has been 
def retrieve_last_book():
   all_books_stored = books_read.find({"reading":True})
   tracker = 0
   query_buffer = []
   for i in all_books_stored:
      tracker += 1
      query_buffer.append(i)
   return query_buffer[tracker - 1]

class bookManage():
    def __init__(self, book_title, author, desc, page_count, key_words, genre, date, deviation, references):
       self.book_title = book_title
       self.author = author
       self.desc = desc
       self.page_count = page_count
       self.key_words = key_words
       self.genre = genre
       self.date = date
       self.deviation = deviation
       self.references = references
    def add_book(self):
     try:
        book = {
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
        books_read.insert_one(book)
        return book
     except TypeError as llm_malfunction:
        print("All modules dependent have retired...attempting a redis overflow")
        last_retrieved = retrieve_last_book()['book_title']
        place_keeper = 0
        for reference in self.references:
           place_keeper += 1
           if last_retrieved == reference:
              next_book = self.references[place_keeper + 1]
              print(next_book)
      

    
