import requests
from bs4 import BeautifulSoup
import json


def scrape_instructables(link):
    url = link

    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser",
                         from_encoding="iso-8859-1")

    header_title = soup.find("h1", {"class": "header-title"}).text

    yt_links = soup.find("iframe")
    if yt_links:
        youtube_url = yt_links['src']
    else:
        youtube_url = yt_links

    view_count = soup.find("p", {"class": "view-count"}).text
    favorite_count = soup.find("p", {"class": "favorite-count"}).text

    try:
        comment_count = soup.find("p", {"class": "comment-count"}).text
    except:
        comment_count = soup.find("p", {"class": "comment-count"})

    steps = soup.findAll("h2", {"class": "step-title"})
    step_titles = []
    for step in steps:
        step_titles.append(step.text)

    supplies_body = soup.find("div", {"class": "step-body"})
    supp = supplies_body.find('ul')
    supply_list = []
    if supp:
        sups = supp.findAll('li')
        for sup in sups:
            sup = sup.text
            supply_list.append(sup)

    scraped = {
        "header_title": str(header_title),
        "youtube_url": str(youtube_url),
        "view_count": str(view_count),
        "favorite_count": str(favorite_count),
        "comment_count": str(comment_count),
        "steps": step_titles,
        "supplies": supply_list
    }
    return scraped


url_list = ["https://www.instructables.com/Building-a-Self-Driving-Boat-ArduPilot-Rover/",
            "https://www.instructables.com/Hydraulic-Craft-Stick-Box/",
            "https://www.instructables.com/How-to-Make-a-Self-Watering-Plant-Stand/"]

for i, url in enumerate(url_list):
    with open("url"+str(i+1)+".json", 'w') as f:
        f.write(json.dumps(scrape_instructables(url)))
