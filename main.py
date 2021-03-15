# --- import needed libraries
from bs4 import BeautifulSoup
import requests
import get_skills as gs

# --- request to a website
html_text = requests.get('https://ponisha.ir/search/projects/skill-%D8%B1%DB%8C%D8%A7%DA%A9%D8%AA-%D9%86%DB%8C%D8%AA%DB%8C%D9%88/currency-IRR/status-open/sort-newest').text

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

skills []
skills = temp


#
# my_skills = gs.my_skills_list
#
# for index, skill in enumerate(skills):
#     for i in my_skills:
#         if i in skill:
#             print(index)
#             break
