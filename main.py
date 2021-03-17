# --- import needed libraries
from bs4 import BeautifulSoup
import requests
import get_skills as gs
import data_base as db

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

# --- replace '\u200c' in persian font to a space
temp = []
for skill in skills:
    temp1 = []
    for j in skill:
        temp2 = j.replace('\u200c', " ")
        temp1.append(temp2)
    temp.append(temp1)

skills = temp

# --- check based on my Skills
my_skills = gs.my_skills_list
indexes = []
for index, skill in enumerate(skills):
    for i in my_skills:
        if i in skill:
            indexes.append(index)
            break

# --- make new links list, titles list and  id
push_name = []
push_links = []
for i in indexes:
    push_name.append(titles[i])
    push_links.append(links[i])

push_id = []
for link in push_links:
    push_id.append(int(link[27:33]))

# --- Push all this data if they are new in Database
for index, id_l in enumerate(push_id):
    db.write_data(id_l, push_name[index], push_links[index])
