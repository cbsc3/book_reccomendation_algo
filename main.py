import requests
from llm import key_word_extractor, genre_abstractor
from db import bookManage
import re
from testing import trending_fantasy, trending_first, trending_second, trending_third, trending_fourth, time_line_generator
import time


#Extracting important information from the API Call

def new_book(book_name):
    google_books = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book_name}' )
    try:
        book_title = google_books.json()['items'][0]['volumeInfo']['title']
        author=  google_books.json()['items'][0]['volumeInfo']['authors']
        desc = google_books.json()['items'][0]['volumeInfo']['description']
        page_count = google_books.json()['items'][0]['volumeInfo']['pageCount']
        genre = google_books.json()['items'][0]['volumeInfo']['categories']
        #print(book_title, author, desc, page_count, key_word_extractor(desc))
        key_words = key_word_extractor(desc)
        regex_key_words= re.split(r"\W", str(key_words))
        key_words_parsed = []
        for regex_key_word in regex_key_words:
            if regex_key_word != '':
                key_words_parsed.append(regex_key_word)
        add_book = bookManage(book_title, author, desc, page_count, key_words_parsed, genre, time_line_generator(), genre_abstractor(genre)).add_book()

            
        #new_book = bookManage(book_title, author, desc, page_count).add_book()
    except KeyError as book_not_found:
        print("The book does not exist")




for i in trending_fantasy:
        new_book(i)


    
