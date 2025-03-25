from pymongo import MongoClient
import uuid
import datetime
import os

key = os.environ.get("MONGO_KEY")
cluster = MongoClient(f'mongodb+srv://dbfoward:{key}@cluster0.9zntn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
books_db = cluster['book_data']
books_read = books_db['books_read']


class bookManage():
    def __init__(self, book_title, author, desc, page_count, key_words, genre, date, deviation):
       self.book_title = book_title
       self.author = author
       self.desc = desc
       self.page_count = page_count
       self.key_words = key_words
       self.genre = genre
       self.date = date
       self.deviation = deviation
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
        print("All modules dependent have retired...")
    
