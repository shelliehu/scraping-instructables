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
    print(soup.find("p", {"class": "favorite-count"})) #test
    if "text" in soup.find("p", {"class": "favorite-count"}):
      favorite_count = soup.find("p", {"class": "favorite-count"}).text
    else: 
      favorite_count = ""
    #favorite_count = soup.find("p", {"class": "favorite-count"}).text
     

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


url_list = ["https://www.instructables.com/DIY-Cardboard-Tensegrity-Pen-Holder/",
           "https://www.instructables.com/Cardboard-Jedi-Starfighter/",
           "https://www.instructables.com/HIVE1-an-Experimental-Low-cost-High-efficiency-Gre/",
           "https://www.instructables.com/How-to-Make-a-Modern-Dog-Bed/",
           "https://www.instructables.com/Marblevator-Pick-and-Place/",
           "https://www.instructables.com/Retropie-Arcade/",
           "https://www.instructables.com/Dovetailed-Blanket-Chest-With-Hand-Forged-Hinges/",
           "https://www.instructables.com/Pokemon-Gastly/",
           "https://www.instructables.com/Mini-Indoor-Fire-Pit-for-Smores/",
           "https://www.instructables.com/Mandolin-From-One-2X4-stand-Too/",
           "https://www.instructables.com/PVC-Pipe-Lamp-2/",
           "https://www.instructables.com/Valentine-Heart-Pinwalker/",
           "https://www.instructables.com/Building-a-Self-Driving-Boat-ArduPilot-Rover/",
           "https://www.instructables.com/Hydraulic-Craft-Stick-Box/",
           "https://www.instructables.com/How-to-Make-a-Self-Watering-Plant-Stand/",
           "https://www.instructables.com/Mechanical-Cardboard-Hand/",
           "https://www.instructables.com/Animation-Light-Box-1/",
           "https://www.instructables.com/PVC-Pipe-Peg/",
           "https://www.instructables.com/Skull-and-Mushroom-Terrarium/",
           "https://www.instructables.com/Simple-LED-Earrings-1/",
           "https://www.instructables.com/Cardboard-Storage-Shelf-From-Single-Box/",
           #"https://www.instructables.com/A-Cardboard-Polaroid-Camera-Webcam-Holder/", this url produces error: it prints None for favorite count
           "https://www.instructables.com/Recycled-Denim-Book-Protector/",
           "https://www.instructables.com/Color-Changing-Bling-Ring/",
           "https://www.instructables.com/Mushroom-Forest-Book-Nook/",
           "https://www.instructables.com/Backflow-Incense-Burner/",
           "https://www.instructables.com/The-74-PVC-Mega-Awesome-Super-PVC-Table/",
           "https://www.instructables.com/Old-Bicycle-Seat-Felted-Taxidermy/",
           "https://www.instructables.com/O3-enabled-BLE-Weather-Station-Predicting-Air-Qual/",
           "https://www.instructables.com/Repair-a-Gramophone-SoundboxReproducer-With-3D-Pri/",
           "https://www.instructables.com/Plywood-Legoman-60cm-Cardboard-Lego-Brick-Light/",
           "https://www.instructables.com/Modular-Tree-Lamp-3D-Printed-or-Lasercut-/",
           "https://www.instructables.com/Orrery-Earth-Moon-and-Sun/",
           "https://www.instructables.com/Lazy-Susan-20-Sushi-Train/",
           "https://www.instructables.com/Table-From-a-2-X-4-Board/",
           "https://www.instructables.com/Giantamax-Snorlax-Flower-Pot-%E8%B6%85%E6%9E%81%E5%B7%A8%E5%8C%96%E5%8D%A1%E6%AF%94%E5%85%BD%E8%8A%B1%E7%9B%86/",
           "https://www.instructables.com/Make-a-Custom-Tilt-Top-Tool-Caddy/",
           "https://www.instructables.com/Simple-Holographic-Audio-Visualizer/",
           "https://www.instructables.com/Making-a-Pencil-Box-From-Scrap-Wood-Gift-Idea/",
           "https://www.instructables.com/Turning-an-Old-Teak-Coffee-Table-Into-a-Ceiling-La/",
           "https://www.instructables.com/Tensegrity-Levitation/",
           "https://www.instructables.com/Cardboard-Lamp-2/",
           "https://www.instructables.com/Premium-Black-Walnut-21-Speakers/",
           "https://www.instructables.com/D4E1-Coffee-Cup-Carrier/",
           "https://www.instructables.com/Emotionally-Unavailable-Plant/"
            
           ]

for i, url in enumerate(url_list):
    with open("url"+str(i+1)+".json", 'w') as f:
        f.write(json.dumps(scrape_instructables(url)))
