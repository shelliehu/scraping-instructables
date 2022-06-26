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
    supp2 = supplies_body.find(id = 'stepsupplies')
    supply_list = []
    if supp:
        sups = supp.find_all('li')
        for sup in sups:
            supplies = sup.text
            supply_list.append(supplies)
    if supp2: #find class p in id stepsupplies
        sups = supp.find('p')
        for sup in sups:
            supplies = sup.text
            supply_list.append(supplies)     

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


url_list = ["https://www.instructables.com/Interceptor-Jet-Card-Stock-Airplane/", #supplies: <p>
           "https://www.instructables.com/Mechanical-Cardboard-Hand/",#supplies: <ul>
            "https://www.instructables.com/Old-Toothbrush-Becomes-Rechargeable-Flashlight/",
            "https://www.instructables.com/Giant-Binder-Clip-Bag/", #supplies: <p>
            "https://www.instructables.com/Giant-Golden-Girls-Purse/", #supplies: <p> within class "step-body"
            "https://www.instructables.com/3D-Printable-Timelapse3D-Scanning-Turntable/", #supplies: <p> + <ul>
            "https://www.instructables.com/Making-Notebook-by-Using-Discarded-Cardboard/" #supplies: <p> supposed to work
           ]

for i, url in enumerate(url_list):
    with open("url"+str(i+1)+".json", 'w') as f:
        f.write(json.dumps(scrape_instructables(url)))
