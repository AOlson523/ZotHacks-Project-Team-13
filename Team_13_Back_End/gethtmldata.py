import requests

def getHTMLData(url):
    print('done reading')
    page = requests.get(url)
    html_file = open("zothacksf22.html", "w", encoding="utf-8")
    html_file.write(page.text)
    html_file.close()


URL = 'https://campusgroups.uci.edu/club_signup?view=all&group_type=9999'
getHTMLData(URL)