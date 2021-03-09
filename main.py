# --- import needed libraries
from bs4 import BeautifulSoup
import requests

# --- request to a website
html_text = requests.get('https://ponisha.ir/search/projects').text

# --- instance soup
soup = BeautifulSoup(html_text, 'lxml')

# --- get each project
projects = soup.find_all('li', class_='item relative')

# --- getting skills and titles
titles = []
skills = []
links = []
for project in projects:
    titles.append(project.find('h4').text)
    links.append(project.find('a', class_='no-link')['href'])
    temp = project.find_all('a', class_='no-link-inherit')
    skills.append([i['title'] for i in temp])

print(titles[1])
print(skills[1])

