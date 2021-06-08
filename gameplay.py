import random
import requests


## choose the pokemon name from API 
def typed_pokemon():
    pokemon_name = input("What pokemon would you like to use?")
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }

## opponents random pokemon choice
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }

## Obtaining your pokemons stats
def run():
    pokemon_choice = typed_pokemon()

    print('Your pokemons stats are id {}, height {} and weight {}'.format(pokemon_choice['id'], 
                                                                          pokemon_choice['height'],
                                                                          pokemon_choice['weight']))
    print('\n')

## Opponents choice of stat
    if round % 2 == 0:
        stats = ['id', 'height', 'weight']
        stat_choice = stats[random.randint(0, 3)]
        my_stat = pokemon_choice[stat_choice]
        print(f'Your opponent has chosen {stat_choice}')
        print('\n')
    else:
        stat_choice = input('Which stat do you want choose? (id, height, weight)')
        my_stat = pokemon_choice[stat_choice]
        print('Your choice of {} has a score of {}'.format(stat_choice, my_stat))
        print('\n')

## outcome of opponents pokemon selection
    opponent_pokemon = random_pokemon()
    print('The opponent choses {}'.format(opponent_pokemon['name']))
    opponent_stat = opponent_pokemon[stat_choice]
    print('Your opponents {} scores {} compared to your {}'.format(stat_choice, opponent_stat, my_stat))
    print('\n')

## results
    if my_stat > opponent_stat:
        print('\33[1m', '\33[94m', 'Victory is Yours!\U0001f600', '\33[0m')
        print('\n')

    elif my_stat < opponent_stat:
        print('\33[1m', '\33[91m', 'You have been Defeated!\U0001F4A9', '\33[0m')
        print('\n')

    else:
        print('\33[1m', 'You and your Opponent have Tied!\U0001F91D', '\33[0m')
        print('\n')

## choosing the number of rounds
print('\n')
number_of_rounds = int(input("How many rounds would you like to play?"))
print('\n')

## ensuring the number of rounds is possible
if (number_of_rounds > 5) or (number_of_rounds < 1):
    number_of_rounds = int(input("This is an impossible number of rounds! Try again:"))
if (number_of_rounds > 5) or (number_of_rounds < 1):
    number_of_rounds = int(input("That number is ridiculous! Try again:"))
if (number_of_rounds > 5) or (number_of_rounds < 1):
    print("That's it, I'm done! Now you need to start over!")
    quit()

round = 1

## playing the number of rounds
while round <= number_of_rounds:
    print("Starting new battle!")
    print("Here are your Pokemon choices! Choose wisely...")
    pokemon_name = random_pokemon()
    list_name = [pokemon_name['name']]

## fetching pokemon names then storing then in a list 
    for name in range(0, 10):
        pokemon_name = random_pokemon()
        list_name.append(pokemon_name['name'])
    print('\33[93m', list_name, '\33[0m')
    print('\n')

    run()
    round = round + 1
