import base64
import os
from google import genai
from google.genai import types

#os.environ.get("GEMINI_KEY")
client = genai.Client(
        api_key=os.environ.get("GEMINI_KEY"),
    )

def key_word_extractor(summary):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Given the synopsis of a book, return key words. Avoid parenthesis, explanations, author names, bullets or other adornments, and words that only pertain to that book; only give five words:{summary}",
        config=types.GenerateContentConfig(
            
            temperature=.5
        )
    )
    return response.text

def genre_abstractor(genre):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"I am going to give you numbers to assign to broad genres of books. If the genre fits the broad genre, assign the real number such: Fiction (1), Romance (2), Non-Fiction (3), Fantasy (4), Sci-Fi (5), Mystery (6), Thriller (7), Historical Fiction (8), Adventure (9), Horror (10), Young Adult (YA) (11), Children's (12), Biography/Autobiography (13), Self-Help (14), Poetry (15), Classic (16). If the broad genre has one more adjective add a value of .03 to the real number assigned; do this for each adjective. If it goes to the next number STOP. ONLY RETURN THE NUMBER. The genre is:{genre}",

config=types.GenerateContentConfig(
            
            temperature=.5
        )
    )
    return response.text


print(genre_abstractor("Dark Magical Fantasy"))

