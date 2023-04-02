import requests
import json

API_URL = 'https://api.opendota.com/api/heroStats'


def get_hero_winrate(hero_info):
    pro_picks = hero_info['pro_pick']
    pro_wins = hero_info['pro_win']
    if pro_picks > 0:
        winrate = pro_wins / pro_picks
        return round(winrate, 5)
    else:
        return 0


response = requests.get(API_URL)
heroes = json.loads(response.text)

hero_winrates = {}
for hero in heroes:
    winrate = get_hero_winrate(hero)
    hero_name = hero['localized_name']
    hero_winrates[hero_name] = winrate

with open('hero_winrates.json', 'w') as f:
    json.dump(hero_winrates, f, indent=4, ensure_ascii=False)
