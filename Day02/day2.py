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

    desired_reds = 12
    desired_greens = 13
    desired_blues = 14
    sum_of_ids = 0
    for i, element in enumerate(games):
        if (int(element['red']) <= desired_reds and int(element['green']) <= desired_greens and int(element['blue']) <= desired_blues):
            sum_of_ids += (i+1)
    print(sum_of_ids)

if __name__ == "__main__":
    main()
