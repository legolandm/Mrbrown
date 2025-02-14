import webbrowser

# List of keywords you want to search
keywords = ["Marilyn Monroe", "Michael Jackson", "Kurt Cobain", "Whitney Houston", "River Phoenix", "Chris Farley", "Lindsey Lohan", "Amy Winehouse", "Heath Ledger", "Shannen Doherty", "Brad Pitt", "Britney Spears", "Robert Downey Jr.", "Justin Bieber", "Tommy Lee", "Lady Gaga", "Prince", "Eminem", "Drew Barrymore", "Jim Morrison", "Kanye West", "Charlize Theron", "Justin Timberlake", "Angelina Jolie", "Johnny Depp", "Tupac Shakur", "Ben Affleck", "Courtney Love", "Michael Buble", "Selena Gomez", "Beyoncé", "Ariana Grande", "Kylie Jenner", "Rihanna", "Kesha", "Madonna", "Shia LaBeouf", "Paris Hilton", "Tyler Perry", "Keanu Reeves", "Jared Leto", "Drake", "Dwayne The Rock Johnson", "Mariah Carey", "Will Smith", "Tom Cruise", "Natalie Portman", "Victoria Beckham", "Kim Kardashian", "Leonardo DiCaprio"


]

# Base search URL (Google in this case)
search_engine = "https://www.google.com/search?q="

# Open a new tab for each keyword
for keyword in keywords:
    webbrowser.open(search_engine + keyword)




from User


import webbrowser

# Base search URL (Google in this case)
search_engine = "https://www.google.com/search?q="

# Ask the user for keywords
user_input = input("Enter the keywords separated by commas: ")

# Split the input into a list of keywords
keywords = [keyword.strip() for keyword in user_input.split(",")]

# Open a new tab for each keyword
for keyword in keywords:
    webbrowser.open(search_engine + keyword)

print("Tabs opened for the given keywords!")

