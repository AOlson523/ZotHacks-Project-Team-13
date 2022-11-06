import requests

def getHTMLData(url):
    page = requests.get(url) 
    html_file = open("zothacksf22.html", "w", encoding="utf-8")
    html_file.write(page.text) # write html_text from website to file 
    html_file.close()


URL = 'https://campusgroups.uci.edu/club_signup?view=all&group_type=9999'
getHTMLData(URL) # creates a text file of all the HTML text from campusgroups (for club names and info)