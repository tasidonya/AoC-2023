import re

# filepath = 'inputs.txt'
filepath = 'puzzle-input.txt'

def to_intlist_max(inlist):
    return max([int(x) for x in inlist])

def main():
    games = []
    for line in open(filepath,'r').read().split('\n'):
        # Get rid of game number, this will be the (list index + 1)
        game_turns = re.findall('\w+\s[0-9]+:\s(.*)',line)
        reds = to_intlist_max(re.findall('([0-9]+)\sred', game_turns[0]))
        greens = to_intlist_max(re.findall('([0-9]+)\sgreen', game_turns[0]))
        blues = to_intlist_max(re.findall('([0-9]+)\sblue', game_turns[0]))
        game_maxes = {'red': reds, 'green': greens, 'blue': blues}
        games.append(game_maxes)

    sum_of_products = 0
    for game in games:
        product = game["red"] * game["blue"] * game["green"]
        sum_of_products += product

    print(sum_of_products)

if __name__ == "__main__":
    main()
