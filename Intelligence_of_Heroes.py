import requests


def get_intelligens(name):
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
    for hero in response:
        if hero['name'] == name:
            return hero['powerstats']['intelligence']


def SH_Choice():
    heroes = ['Hulk', 'Captain America', 'Thanos']
    rating_list = []
    for i in heroes:
        rating_list.append([get_intelligens(i), i])
    rating_list.sort(reverse=True)
    return f'{rating_list[0][1]} - это самый умный супергерой среди: {", ".join(heroes)}.\n' \
           f'Интеллект {rating_list[0][1]} - {rating_list[0][0]} единиц.'


print(SH_Choice())