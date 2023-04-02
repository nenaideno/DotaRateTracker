import json

with open('hero_winrates.json', 'r') as f:
    hero_winrates = json.load(f)

def sort_heroes_by_winrate(hero_winrates):
    sorted_heroes = sorted(hero_winrates.items(), key=lambda x: x[1], reverse=True)
    for i, (hero_name, winrate) in enumerate(sorted_heroes):
        sorted_heroes[i] = (hero_name, f'{winrate*100:.2f}')
    return dict(sorted_heroes)

sorted_hero_winrates = sort_heroes_by_winrate(hero_winrates)

with open('sorted_hero_winrates.json', 'w') as f:
    json.dump(sorted_hero_winrates, f, indent=4, ensure_ascii=False)
