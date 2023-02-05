import requests

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print("Failed to download image")

images = [
    'https://cdnb.artstation.com/p/assets/images/images/058/250/877/original/ryan-haight-volunteer-park-small.gif?1673728567',
    'https://cdna.artstation.com/p/assets/images/images/037/888/560/original/ryan-haight-cincinatti-small.gif?1621576299',
    'https://cdnb.artstation.com/p/assets/images/images/058/250/569/original/ryan-haight-ws-bus-large.gif?1673727850',
    'https://cdnb.artstation.com/p/assets/images/images/058/250/967/original/ryan-haight-leschi-park-large.gif?1673728804',
    'https://cdna.artstation.com/p/assets/images/images/058/250/772/original/ryan-haight-ws-concrete-large.gif?1673728398',
    'https://cdnb.artstation.com/p/assets/images/images/058/250/661/original/ryan-haight-carkeek-park-large.gif?1673728045',
    'https://cdnb.artstation.com/p/assets/images/images/058/250/433/original/ryan-haight-cherry-hill-large.gif?1673727592',
    'https://cdna.artstation.com/p/assets/images/images/058/250/400/original/ryan-haight-west-queenanne-large.gif?1673727429',
    'https://cdna.artstation.com/p/assets/images/images/056/215/680/original/ryan-haight-eastlake-hway-large.gif?1668708925',
    'https://cdnb.artstation.com/p/assets/images/images/041/146/243/original/ryan-haight-pikesplace-600.gif?1630901497',
    'https://cdnb.artstation.com/p/assets/images/images/043/102/245/original/ryan-haight-sam.gif?1636324205',
    'https://cdnb.artstation.com/p/assets/images/images/044/113/857/original/ryan-haight-monorail-spneed-large.gif?1639122189',
    'https://cdnb.artstation.com/p/assets/images/images/043/102/271/original/ryan-haight-northgate-station.gif?1636324301',
    'https://cdna.artstation.com/p/assets/images/images/055/536/614/original/ryan-haight-apartment-large.gif?1667202801'
]

for i, image in enumerate(images):
    download_image(image, f'{i}.gif')