# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:50:26 2021

@author: Collin
"""

#Import the get() function from the requests module
#Assign the address of the web page to a variable named url
#Request the server the content of the web page by using get(), and store the server’s response in the variable response
#Print a small part of response‘s content by accessing its .text attribute
from requests import get
url = 'https://www.ncaa.com/brackets/basketball-men/d1/2019'
response = get(url)
print(response.text[:500])

#Import the BeautifulSoup class creator from the package bs4
#Parse response.text by creating a BeautifulSoup object, and assign this object to html_soup. The 'html.parser' argument indicates that we want to do the parsing using Python’s built-in HTML parser.
from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

#store all games in a list, by searching for a list of class values
team_containers = html_soup.find_all('div', class_= ["play-pod game-pod pod-1 final", "play-pod game-pod pod-2 final", 
"play-pod game-pod pod-3 final", "play-pod game-pod pod-4 final", "play-pod game-pod pod-5 final"
, "play-pod game-pod pod-6 final", "play-pod game-pod pod-7 final", "play-pod game-pod pod-0 final"
, "play-pod game-pod pod-601 final", "play-pod game-pod pod-602 final", "play-pod game-pod pod-101 final"
, "play-pod game-pod pod-102 final", "play-pod game-pod pod-103 final", "play-pod game-pod pod-104 final"])


print(type(team_containers))
print(len(team_containers))
first_team = team_containers[0]
first_team

first_name = first_team.find('span', class_ = 'name')
first_name = first_name.text
first_name

first_rank = first_team.find('span', class_ = 'seed')
first_rank = first_rank.text
first_rank

first_score = first_team.find('span', class_ = 'score')
first_score = first_score.text
first_score

eighth_team_score = team_containers[7].find('span', class_ = 'score').text
eighth_team_score

teams = []
ranks = []
scores = []

team_containers = html_soup.find_all('div', class_= ["play-pod game-pod pod-1 final", "play-pod game-pod pod-2 final", 
"play-pod game-pod pod-3 final", "play-pod game-pod pod-4 final", "play-pod game-pod pod-5 final"
, "play-pod game-pod pod-6 final", "play-pod game-pod pod-7 final", "play-pod game-pod pod-0 final"
, "play-pod game-pod pod-601 final", "play-pod game-pod pod-602 final", "play-pod game-pod pod-101 final"
, "play-pod game-pod pod-102 final", "play-pod game-pod pod-103 final", "play-pod game-pod pod-104 final"])

for container in team_containers:

    team = container.find('span', class_ = 'name').text
    teams.append(team)
        
    rank = container.find('span', class_ = 'seed').text
    ranks.append(int(rank))
        
    score = container.find('span', class_ = 'score').text
    scores.append(int(score))
    
scores

import pandas as pd
test_df = pd.DataFrame({'teams': teams,
'ranks': ranks,
'scores': scores})
print(test_df.info())
test_df
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    