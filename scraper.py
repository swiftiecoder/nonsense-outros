import requests
from bs4 import BeautifulSoup

# Define the URL of the website
url = "https://genius.com/Genius-lists-list-of-sabrina-carpenter-nonsense-outros-annotated"

# Fetch the web page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the nonsense outros on the page
# Adjust the selector based on the actual HTML structure
outros = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
print(outros)

# Open a file called outros.txt to write the HTML content
with open('./nonsense outros/outros.txt', 'w', encoding='utf-8') as file:
    for outro in outros:
        file.write(str(outro))
        file.write('\n')  # Add a newline for separation between outros
