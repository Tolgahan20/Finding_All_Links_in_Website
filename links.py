import requests
from bs4 import BeautifulSoup

# Here is the target website
url = input("Enter the Website URL: ")

res = requests.get(url).content
soup = BeautifulSoup(res, 'html.parser')

# finding all anchor elements ( <a></a> )
links = soup.find_all('a')

for link in links:
    print(link['href'])
