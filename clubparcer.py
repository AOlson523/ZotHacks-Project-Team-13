import json
from bs4 import BeautifulSoup

with open("zothacksf22.html", encoding="utf8") as htmltext:
    datasoup = BeautifulSoup(htmltext, 'html.parser')

    clubs_json_list = []
    club_groups = datasoup.find_all('h2', class_ = "media-heading header-cg--h4")
    for club in club_groups:
        club_info = club.find_all('a', limit = 1)
        clubs_json_list.append({'name': club_info[0].get_text(strip = True)})
    
    clubs_json = json.dumps(clubs_json_list, indent = 4)

    with open('campus_groups.json', 'w') as output:
        output.write(clubs_json)
        


