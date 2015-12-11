# Christmas Gift Exchange


import random

raw_names = raw_input('Enter first names separated by commas: ')
givers_list = raw_names.replace(', ', ',').split(',')
receivers_list = list(givers_list)

results = {}

for i, giver in enumerate(givers_list):
    random_index = random.randint(0, len(receivers_list)-1)
    random_receiver = receivers_list.pop(random_index)
    while giver == random_receiver:
        if not receivers_list:
            print "rerun"
            break
        receivers_list.append(random_receiver)
        random_index = random.randint(0, len(receivers_list)-1)
        random_receiver = receivers_list.pop(random_index)
    print "{}. {} - {}".format(i+1, giver.title(), random_receiver.title())
