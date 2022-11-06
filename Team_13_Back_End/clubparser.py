import json
from bs4 import BeautifulSoup

with open("zothacksf22.html", encoding="utf8") as htmltext:
    datasoup = BeautifulSoup(htmltext, 'html.parser') # turn html text to datasoup project to use index functions

    clubs_json_list = []
    club_groups = datasoup.find_all('h2', class_ = "media-heading header-cg--h4") # finds all club names in Campus Groups (each located in h2)
    for club in club_groups:
        club_info = club.find_all('a', limit = 2)
        club_name = club_info[0].get_text(strip = True)
        club_website = club_info[1].get("href")
        club_mission = club.find_all('p', class_ = 'noOutlineOnFocus', limit = 1)
        club_type = club.find_all('p', class_ = 'h5 media-heading grey-element')
        club_type = club_type[0].get_text(strip = True)
        if club_mission[0].get_text(strip = True)[7:] == '':
            bio = None
        else:
            bio = club_mission[0].get_text(strip = True)[7:]
            bio = bio.replace('\u200b', '')

        if '-' in club_type:
            club_type = club_type.split('-')
            club_main_type = club_type[0].strip()
            club_sub_type = club_type[1].strip().split(', ')
        else:
            club_main_type = club_type
            club_sub_type = None
        clubs_json_list.append({'name': club_name, 
                                'main_type': club_main_type, 
                                'sub_type': club_sub_type, 
                                'bio': bio,
                                'website': club_website})
    
    clubs_json = json.dumps(clubs_json_list, indent = 4)

    with open('campus_groups.json', 'w') as output:
        output.write(clubs_json)