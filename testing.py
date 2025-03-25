import datetime
import random
import matplotlib.pyplot as plt
import numpy
from db import books_read
trending_fantasy = [
    # High Fantasy
    "The Hobbit",
    "The Fellowship of the Ring",
    "A Game of Thrones",
    "The Name of the Wind",
    "The Lies of Locke Lamora",
    "The Final Empire",
    "The Once and Future King",
    "The Way of Kings",
    "The Last Wish",
    "The Priory of the Orange Tree",

    # Urban & Contemporary Fantasy
    "American Gods",
    "Neverwhere",
    "The Night Circus",
    "The House in the Cerulean Sea",
    "The Magicians",
    "Daughter of Smoke and Bone",
    "An Ember in the Ashes",
    "City of Stairs",
    "The Dresden Files: Storm Front",
    "Small Gods",

    # Mythology-Inspired Fantasy
    "Circe",
    "The Song of Achilles",
    "Lore",
    "Norse Mythology",
    "Ariadne",

    # Science Fiction (with Fantasy Elements)
    "Dune",
    "Ender’s Game",
    "The Left Hand of Darkness",
    "The Long Way to a Small, Angry Planet",
    "Hyperion",

    # Historical Fiction (with or without fantasy elements)
    "The Shadow of the Wind",
    "The Book Thief",
    "Jonathan Strange & Mr. Norrell",
    "The Nightingale",
    "All the Light We Cannot See",

    # Horror (with Fantasy or Gothic Elements)
    "Dracula",
    "Frankenstein",
    "The Haunting of Hill House",
    "The Shadow of the Wind",
    "Coraline",
    
    # Mystery/Thriller (with Fantasy or Supernatural Elements)
    "The 7 ½ Deaths of Evelyn Hardcastle",
    "The Girl with the Dragon Tattoo",
    "The Silent Patient",
    "Big Little Lies",
    
    # Classic Literature (with some fantasy or magical realism)
    "One Hundred Years of Solitude",
    "The Master and Margarita",
    "Alice’s Adventures in Wonderland",
    "The Picture of Dorian Gray",
    "Fahrenheit 451",
    
    # Non-Fiction (with themes related to fantasy, mythology, or storytelling)
    "Sapiens: A Brief History of Humankind",
    "The Hero with a Thousand Faces",
    "The Immortal Life of Henrietta Lacks",
    "Mythos",
    "Born a Crime"
]

trending_nonfic = [
    # History & Biographies  
    "Sapiens: A Brief History of Humankind",  
    "The Immortal Life of Henrietta Lacks",  
    "Born a Crime",  
    "The Devil in the White City",  
    "The Wright Brothers",  
    "Team of Rivals",  
    "The Splendid and the Vile",  
    "The Radium Girls",  
    "Catherine the Great: Portrait of a Woman",  
    "The Warmth of Other Suns",  

    # Science & Psychology  
    "Thinking, Fast and Slow",  
    "The Gene: An Intimate History",  
    "Behave: The Biology of Humans at Our Best and Worst",  
    "The Emperor of All Maladies",  
    "Why We Sleep",  
    "The Body: A Guide for Occupants",  
    "Grit: The Power of Passion and Perseverance",  
    "Atomic Habits",  
    "Stiff: The Curious Lives of Human Cadavers",  
    "The Extended Mind",  

    # Philosophy & Society  
    "Meditations" ,  
    "The Myth of Sisyphus",  
    "The Righteous Mind",  
    "Outliers",  
    "Freakonomics",  
    "Nickel and Dimed",  
    "The Sixth Extinction",  
    "Amusing Ourselves to Death",  
    "The Structure of Scientific Revolutions",  
    "Between the World and Me",  

    # Memoirs & Essays  
    "Educated",  
    "The Glass Castle",  
    "When Breath Becomes Air",  
    "I Know Why the Caged Bird Sings",  
    "Men Explain Things to Me",  
    "On Writing",  
    "A Moveable Feast",  
    "What I Talk About When I Talk About Running",  
    "Notes of a Native Son",  
    "Heavy",  

    # Literary Fiction  
    "To Kill a Mockingbird",  
    "The Great Gatsby",  
    "Beloved",  
    "The Road",  
    "Pachinko",  
    "The Remains of the Day",  
    "A Gentleman in Moscow",  
    "The Night Watchman",  
    "Circe",  
    "Homegoing",  
    "The Shadow of the Wind",  
    "One Hundred Years of Solitude",  
    "The Overstory",  
    "Lincoln in the Bardo",  
    "The Goldfinch",  

    # Adventure & Nature Writing  
    "Into the Wild",  
    "Into Thin Air",  
    "Desert Solitaire",  
    "A Walk in the Woods",  
    "The Lost City of Z",  
    "Endurance: Shackleton’s Incredible Voyage",  
    "The Call of the Wild",  
    "In the Heart of the Sea",  
    "West with the Night",  
    "The Old Man and the Sea",  
]

trending_fourth = [
    "To Kill a Mockingbird",
    "The Great Gatsby",
    "The Picture of Dorian Gray",
    "Brave New World",
    "The Catcher in the Rye",
    "Crime and Punishment",
    "One Hundred Years of Solitude",
    "The Bell Jar",
    "Slaughterhouse-Five",
    "Mrs. Dalloway",
    "The Stranger",
    "The Road",
    "Blood Meridian",
    "Beloved",
    "The Underground Railroad",
    "Homegoing",
    "Pachinko",
    "The Night Watchman",
    "A Gentleman in Moscow",
    "The Remains of the Day",
    "The Goldfinch",
    "Lincoln in the Bardo",
    "The Overstory",
    "The Shadow of the Wind",
    "Cloud Atlas",
    "Middlesex",
    "The Secret History",
    "The Nightingale",
    "The Book Thief",
    "The House of Spirits",
    "Things Fall Apart",
    "A Fine Balance",
    "Americanah",
    "The Sympathizer",
    "The Orphan Master's Son",
    "The Brief Wondrous Life of Oscar Wao",
    "The Amazing Adventures of Kavalier & Clay",
    "White Teeth",
    "Never Let Me Go",
    "The Namesake",
    "A Visit from the Goon Squad",
    "Station Eleven",
    "The Road",
    "Norwegian Wood",
    "Kafka on the Shore",
    "1Q84",
    "Infinite Jest",
    "A Little Life",
    "The Goldfinch",
    "We Need to Talk About Kevin"
]

trending_third = [
    "Dune",
    "Neuromancer",
    "The Left Hand of Darkness",
    "Snow Crash",
    "The Three-Body Problem",
    "Hyperion",
    "Children of Time",
    "The Long Way to a Small, Angry Planet",
    "A Canticle for Leibowitz",
    "The Dispossessed",
    "Foundation",
    "I, Robot",
    "Do Androids Dream of Electric Sheep?",
    "The Man in the High Castle",
    "Ubik",
    "Brave New World",
    "1984",
    "Fahrenheit 451",
    "The Stars My Destination",
    "Rendezvous with Rama",
    "The Moon is a Harsh Mistress",
    "Stranger in a Strange Land",
    "The Lathe of Heaven",
    "Permutation City",
    "Blindsight",
    "The Quantum Thief",
    "Altered Carbon",
    "The Expanse: Leviathan Wakes",
    "Red Mars",
    "The Windup Girl",
    "The Water Knife",
    "The Ministry for the Future",
    "Annihilation",
    "A Fire Upon the Deep",
    "A Deepness in the Sky",
    "To Sleep in a Sea of Stars",
    "The Space Between Worlds",
    "All Systems Red",
    "Artificial Condition",
    "Exit Strategy",
    "Network Effect",
    "The Murderbot Diaries",
    "Old Man’s War",
    "The Forever War",
    "The Road",
    "Parable of the Sower",
    "Parable of the Talents",
    "Kindred",
    "The Book of the New Sun",
    "The Player of Games",
    "Consider Phlebas",
    "Use of Weapons",
    "The Algebraist",
    "The Collapsing Empire",
    "Seveneves",
    "The Diamond Age"
]

trending_second = [
    "Sapiens: A Brief History of Humankind",
    "Guns, Germs, and Steel",
    "The Gene: An Intimate History",
    "Behave: The Biology of Humans at Our Best and Worst",
    "Why We Sleep",
    "The Sixth Extinction",
    "The Emperor of All Maladies",
    "The Body: A Guide for Occupants",
    "Stiff: The Curious Lives of Human Cadavers",
    "The Immortal Life of Henrietta Lacks",
    "A Brief History of Time",
    "The Selfish Gene",
    "The Demon-Haunted World",
    "The Elegant Universe",
    "Physics of the Impossible",
    "Astrophysics for People in a Hurry",
    "The Hidden Reality",
    "The Fabric of the Cosmos",
    "The Grand Design",
    "Your Inner Fish",
    "The Omnivore’s Dilemma",
    "Salt: A World History",
    "Big History",
    "The Wright Brothers",
    "The Splendid and the Vile",
    "Team of Rivals",
    "The Warmth of Other Suns",
    "Nickel and Dimed",
    "Freakonomics",
    "Outliers",
    "The Righteous Mind",
    "The Structure of Scientific Revolutions",
    "Superforecasting",
    "The Art of Thinking Clearly",
    "Nudge",
    "Thinking, Fast and Slow",
    "The Black Swan",
    "Fooled by Randomness",
    "Antifragile",
    "The Signal and the Noise",
    "Skin in the Game",
    "Quiet: The Power of Introverts in a World That Can’t Stop Talking",
    "Grit",
    "Drive",
    "The Power of Habit",
    "Atomic Habits",
    "Dare to Lead",
    "The 48 Laws of Power",
    "Extreme Ownership",
    "Can’t Hurt Me",
    "Make Your Bed",
    "Deep Work",
    "Digital Minimalism",
    "The Shallows",
    "The Coddling of the American Mind",
    "The Death of Expertise",
    "Amusing Ourselves to Death"
]

trending_first = [
    "The Night Circus",
    "The Starless Sea",
    "Piranesi",
    "The Ocean at the End of the Lane",
    "The Invisible Life of Addie LaRue",
    "Jonathan Strange & Mr Norrell",
    "Alice’s Adventures in Wonderland",
    "The House in the Cerulean Sea",
    "The Ten Thousand Doors of January",
    "The Once and Future Witches",
    "The Midnight Library",
    "Howl’s Moving Castle",
    "The Hazel Wood",
    "The Strange Library",
    "The Bear and the Nightingale",
    "Uprooted",
    "Spinning Silver",
    "The Girl Who Circumnavigated Fairyland in a Ship of Her Own Making",
    "Stardust",
    "Coraline",
    "Lud-in-the-Mist",
    "The Golem and the Jinni",
    "The Paper Menagerie and Other Stories",
    "The Night Watch",
    "The Goblin Emperor",
    "Thorn",
    "A Winter’s Promise",
    "Tress of the Emerald Sea",
    "Neverwhere",
    "The Bone Clocks",
    "Strange the Dreamer",
    "Muse of Nightmares",
    "The Priory of the Orange Tree",
    "The Drowned Cities",
    "The Library at Mount Char",
    "The Book Thief",
    "The Shadow of the Wind",
    "The Reader",
    "The Book of Lost Things",
    "The Historian",
    "The Thirteenth Tale",
    "The Physick Book of Deliverance Dane",
    "The Miniaturist",
    "The Secret History of Witches",
    "The Paper Magician",
    "The Magicians",
    "The Night Manager",
    "The Shadow Cabinet",
    "The Strange Case of the Alchemist’s Daughter",
    "The Rook",
    "Sorcery of Thorns",
    "Vicious",
    "Vengeful",
    "The Atlas Six",
    "The Midnight Bargain",
    "The Mask of Mirrors",
    "The Unspoken Name",
    "The Queen of the Tearling",
    "The City We Became",
    "A Darker Shade of Magic",
    "The Invisible Library"
]



def time_line_generator():
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

    month = random.choice(months)
    day = random.choice(days)
    try:
        day = random.choice(days)
        return datetime.datetime(2025, month, day)
    except ValueError as date_out_of_range:
        day = 29
        return datetime.datetime(2025, month, day)

def plot_date_genre():
    all_books = books_read.find({"reading":True})



    dates = []
    genres = []


    for book in books_read.find({"reading": True}):
        date_obj = book['date_added']  # Assuming this is already a datetime object
        dates.append(date_obj)
        genres.append(book['deviation'])


    # Sort by date
    sorted_data = sorted(zip(dates, genres))  # Zip and sort by date
    dates, genres = zip(*sorted_data)  # Unzip into separate lists

    # Convert dates and genres to lists (if needed, depending on your plotting method)
    dates = list(dates)
    genres = list(genres)

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.scatter(dates, genres, marker="o")  # Scatter plot for categorical genres
    plt.xlabel("Date")
    plt.ylabel("Genre")
    plt.title("Genre with Respect to Date")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(True)

    plt.show()

