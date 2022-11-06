import json
from bs4 import BeautifulSoup
# Extracts information from each club in Campus Groups 
# and stores it into a JSON file.


with open("zothacksf22.html", encoding="utf8") as htmltext:
    datasoup = BeautifulSoup(htmltext, 'html.parser') # turn html text to datasoup project to use index functions

    clubs_json_list = []
    club_groups = datasoup.find_all('h2', class_ = "media-heading header-cg--h4") # finds the start of each club information in Campus Groups (each located in h2)
    for club in club_groups:
        club_info = club.find_all('a', limit = 2) # finds block of info that contains club name and website
        club_name = club_info[0].get_text(strip = True)
        club_website = club_info[1].get("href")

        club_mission = club.find_all('p', class_ = 'noOutlineOnFocus', limit = 1) # finds club bio

        club_type = club.find_all('p', class_ = 'h5 media-heading grey-element') # finds club types (both main and sub)
        club_type = club_type[0].get_text(strip = True)

        if club_mission[0].get_text(strip = True)[7:] == '': # Starts from index 7 because each bio started with the word "Mission"
            bio = None                                      # makes bio null if not found
        else:
            bio = club_mission[0].get_text(strip = True)[7:]
            bio = bio.replace('\u200b', '')                 # removes ZeroWidthSpace

        if '-' in club_type:            # splits the main type from the sub types
            club_type = club_type.split('-')
            club_main_type = club_type[0].strip()
            club_sub_type = club_type[1].strip().split(', ') # organizes sub types in a list
        else:
            club_main_type = club_type  # if no dashes exits, then sub types don't exist
            club_sub_type = None
        clubs_json_list.append({'name': club_name, 
                                'main_type': club_main_type, 
                                'sub_type': club_sub_type, 
                                'bio': bio,
                                'website': club_website})
    
    clubs_json = json.dumps(clubs_json_list, indent = 4)

    with open('campus_groups.json', 'w') as output:
        output.write(clubs_json)