import json
import os

# This program is designed to be a team management device to be used while playing a Pokemon Soullink challenge
# It will allow the user to add new pairs and remove pairs
# Lastly, it will let the user build the best possible roster of pairs that follows typing rules

# defining pair list
pairs = []
team_comp = []


def read_file():
    global pairs, team_comp
    try:
        with open('pairs.json', 'r') as fp:
            pairs = json.load(fp)
        with open('teams.json', 'r') as pf:
            team_comp = json.load(pf)
    except (IOError, FileNotFoundError):
        pass


def write_file():
    global pairs, team_comp
    with open('pairs.json', 'w') as fp:
        json.dump(pairs, fp)
    with open('teams.json', 'w') as pf:
        json.dump(team_comp, pf)


def display_main_menu():
    os.system('cls')
    print(f'1. Add New Pair\n2. Delete Pair\n3. \"Kill\" Pair\n4. Revive Pair\n5. Build Team\n'
          f'6. Display Routes\n7. Display All Pairs\n8. Exit')
    selection = int(input('Select Menu Option (1-8): '))

    if selection == 1:
        add_pair()
    elif selection == 2:
        delete_pair()
    elif selection == 3:
        kill_pair()
    elif selection == 4:
        revive_pair()
    elif selection == 5:
        build_team()
    elif selection == 6:
        print_routes()
    elif selection == 7:
        os.system('cls')
        print_all_pairs()
        input('Press Enter to return to the main menu.')
        display_main_menu()
    elif selection == 8:
        write_file()
        exit(0)
    else:
        input('Invalid Selection. Press any key to return to the main menu.')


def print_type_list():
    """Prints the list of pokemon types and their respective numbers"""
    print('1. Normal\n2. Fire\n3. Water\n4. Electric\n5. Grass\n6. Ice\n7. Fighting\n8. Poison\n9. Ground\n10. Flying'
          '\n11. Psychic\n12. Bug\n13. Rock\n14. Ghost\n15. Dragon\n16. Dark\n17. Steel\n18. Fairy')


def get_type(type_num):
    """Changes the selected number into its respective string"""
    if type_num == 1:
        poke_type = 'Normal'
    elif type_num == 2:
        poke_type = 'Fire'
    elif type_num == 3:
        poke_type = 'Water'
    elif type_num == 4:
        poke_type = 'Electric'
    elif type_num == 5:
        poke_type = 'Grass'
    elif type_num == 6:
        poke_type = 'Ice'
    elif type_num == 7:
        poke_type = 'Fighting'
    elif type_num == 8:
        poke_type = 'Poison'
    elif type_num == 9:
        poke_type = 'Ground'
    elif type_num == 10:
        poke_type = 'Flying'
    elif type_num == 11:
        poke_type = 'Psychic'
    elif type_num == 12:
        poke_type = 'Bug'
    elif type_num == 13:
        poke_type = 'Rock'
    elif type_num == 14:
        poke_type = 'Ghost'
    elif type_num == 15:
        poke_type = 'Dragon'
    elif type_num == 16:
        poke_type = 'Dark'
    elif type_num == 17:
        poke_type = 'Steel'
    else:
        poke_type = 'Fairy'

    return poke_type


def add_pair():
    global pairs
    os.system('cls')

    # pokemon 1
    print('Input Pair Information:')
    pokemon1 = input('Pokemon 1: ')
    os.system('cls')

    # pokemon type 1
    print('Input Pair Information:')
    print_type_list()
    type1 = int(input('Pokemon 1 Type Number: '))
    if 1 <= type1 <= 17:
        type1_value = get_type(type1)
    else:
        display_main_menu()
        return
    os.system('cls')

    # pokemon 2
    print('Input Pair Information:')
    pokemon2 = input('Pokemon 2: ')
    os.system('cls')

    # pokemon type 2
    print('Input Pair Information:')
    print_type_list()
    type2 = int(input('Pokemon 2 Type Number: '))
    if 1 <= type2 <= 17:
        type2_value = get_type(type2)
    else:
        display_main_menu()
        return
    os.system('cls')

    # catch location
    print('Input Pair Information:')
    location = input('Capture Route: ')
    for p in pairs:
        if location == p['Location']:
            input('You have already encountered on this route. Press enter to return to the main menu.')
            display_main_menu()
            return
    os.system('cls')

    # adds pairs to the master list
    pair_info = {'Location': location, 'Pokemon 1': pokemon1, 'Type 1': type1_value, 'Pokemon 2': pokemon2,
                 'Type 2': type2_value, 'Status': 'Alive', 'Index': 0}
    pairs.append(pair_info)

    write_file()
    display_main_menu()
    return


def print_all_pairs():
    global pairs
    count = 1
    print(f'{"Num":<5}|{"Pokemon 1":^15}|{"Type 1":^10}|{"Pokemon 2":^15}|{"Type 2":^10}|'
          f'{"Status":^10}|{"Location":^20}|')
    for p in pairs:
        print(f'{count:<5}|{p["Pokemon 1"]:^15}|{p["Type 1"]:^10}|{p["Pokemon 2"]:^15}|'
              f'{p["Type 2"]:^10}|{p["Status"]:^10}|{p["Location"]:^20}|')
        count += 1


def delete_pair():
    """Allows the user to delete a pair that was added by mistake or that contains an error"""
    os.system('cls')
    print_all_pairs()
    # allows selection of pair to be deleted
    selection = int(input('Select Pair Number to Delete: '))

    # validates that selection was valid
    if 1 <= selection <= len(pairs):
        pairs.pop(selection-1)

    write_file()
    display_main_menu()


def kill_pair():
    """To be used if a pair has been killed in combat"""
    os.system('cls')
    print_all_pairs()
    selection = int(input('Select Pair Number that has tragically died: '))

    # validates that selection was valid
    if 1 <= selection <= len(pairs):
        pairs[selection-1]['Status'] = 'Dead'
        team_comp.remove(pairs[selection-1])
    write_file()
    display_main_menu()


def revive_pair():
    """To be used if a pair has been marked as killed in combat by mistake"""
    os.system('cls')
    print_all_pairs()
    selection = int(input('Select Pair Number that has been marked as dead by accident: '))

    # validates that selection was valid
    if 1 <= selection <= len(pairs):
        pairs[selection-1]['Status'] = 'Alive'
    write_file()
    display_main_menu()


def print_eligible_pairs(used_types, count=1):
    """Prints all pairs that are able to be added to the created party according to typing rules"""
    global pairs
    print('\n\tEligible Pairs:')
    print(f'{"Num":<5}|{"Pokemon 1":^15}|{"Type 1":^10}|{"Pokemon 2":^15}|{"Type 2":^10}|')
    if len(team_comp) < 6:
        for p in pairs:
            if p["Type 1"] not in used_types and p["Type 2"] not in used_types and p["Status"] == 'Alive':
                print(f'{count:<5}|{p["Pokemon 1"]:^15}|{p["Type 1"]:^10}|{p["Pokemon 2"]:^15}|{p["Type 2"]:^10}|')
                p['Index'] = count
                count += 1
            else:
                p['Index'] = 0

    else:
        print('Team has 6 pairs. Remove a pair to add more.')


def print_team_comp():
    """Prints the pairs that have already been selected for a team"""
    global team_comp
    os.system('cls')
    count = 1
    print('\tCurrent Roster:')
    print(f'{"Num":<5}|{"Pokemon 1":^15}|{"Type 1":^10}|{"Pokemon 2":^15}|{"Type 2":^10}|')
    for p in team_comp:
        print(f'{count:<5}|{p["Pokemon 1"]:^15}|{p["Type 1"]:^10}|{p["Pokemon 2"]:^15}|{p["Type 2"]:^10}|')
        p['Index'] = count
        count += 1
    return count


def build_team():
    global pairs, team_comp

    selection = -1
    used_types = []
    for p in team_comp:
        used_types.append(p['Type 1'])
        used_types.append(p['Type 2'])

    # loop to add pokemon to team
    while selection != 0:
        os.system('cls')
        count = 1
        if len(team_comp) > 0:
            count = print_team_comp()
        print_eligible_pairs(used_types, count)
        selection = int(input('\nSelect Pair Number to add to team, or select a team member to remove them '
                              'from the roster, or press 0 to go back to the main menu: '))

        if selection > len(team_comp):
            for p in pairs:
                if selection == p['Index']:
                    team_comp.append(p)
                    used_types.append(p['Type 1'])
                    used_types.append(p['Type 2'])
        elif selection <= len(team_comp) and selection != 0:
            removed_pair = team_comp.pop(selection-1)
            used_types.remove(removed_pair['Type 1'])
            used_types.remove(removed_pair['Type 2'])
        else:
            display_main_menu()

        write_file()


def print_routes():
    os.system('cls')
    for p in pairs:
        print(p['Location'])
    input('Press Enter to return to the main menu.')
    display_main_menu()


read_file()
display_main_menu()
