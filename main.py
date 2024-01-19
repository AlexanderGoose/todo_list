import os
import time


def clear_screen():
    os.system('clear')


class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


# list of all items for each day of the week to be added to
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []
unsure = []


# adds after the last to do item but before the first
# done item. The later defined print function adds the index,
# that is NOT done here.
def add_to_list(thing_to_add, day):
    current_pos = 0
    for i in day:
        if day:
            if 'DONE' in i:
                break
        current_pos += 1

    adding = f' {Colors.RED}TODO:{Colors.RESET} ' + thing_to_add

    day.insert(current_pos, adding)


# marking complete grabs the to do item
# removes the to do item, strips of the "TO DO"
# appends to the end of the list and adds 'DONE'
# appending to the end makes to possible to remove based on it's index
def mark_complete(num, day):
    if len(day) < num - 1:
        print('That item is out of range. Try again.')
        time.sleep(2)
    else:
        curr_day = day[num - 1]
        new = curr_day.split(':')
        day.remove(curr_day)
        day.append(f' {Colors.GREEN}DONE:{Colors.RESET}{new[1]}')


# remove uses the to do item's index
# and removes it from the list for the assigned day
# delays for a moment so user can catch any mistakes
def remove_item(num, day):

    if len(day) < num - 1:
        print('That item is out of range. Try again.')
        time.sleep(2)
    else:
        curr_day = day[num - 1]
        new = curr_day.split(':')
        day.remove(curr_day)
        print(f'{new[1]} removed or edited from todo list.')
        time.sleep(2)


# moves an item to a new day
# currently not in use due to bugs
def move_item(old_day, curr_pos, day_to_add_item_to):
    curr_item = old_day[curr_pos - 1]
    just_item = curr_item.split(':')
    just_last = just_item[-1]
    #just_stripped = just_last.replace(' ', '')
    #joined = ' '.join(just_stripped)
    add_to_list(just_last, day_to_add_item_to)


# prints in order of to do items first and done
# items second. Adds the position + 1 before the item
# so user can mark complete and remove based on number
def print_current_day(day):
    current_position = 1

    # start by printing to do items only
    for i in day:
        if 'TODO' in i:
            print(f'    ({current_position}):{i}')
            current_position += 1
        else:
            break
    print('\n')

    # print done items next
    for i in day:
        if 'DONE' in i:
            print(f'    ({current_position}):{i}')
            current_position += 1
    print('\n')


# prints all items for each day of the week list
# calls above function on each day to print items in order
# of their current status
def print_todo_items(m, t, w, th, f, s, su, u):
    print('MONDAY')
    print_current_day(m)

    print('TUESDAY')
    print_current_day(t)

    print('WEDNESDAY')
    print_current_day(w)

    print('THURSDAY')
    print_current_day(th)

    print('FRIDAY')
    print_current_day(f)

    print('SATURDAY')
    print_current_day(s)

    print('SUNDAY')
    print_current_day(su)

    print('UNSURE')
    print_current_day(u)


# asks users what they would like to do and prevents
# invalid inputs.
def add_or_remove():
    valid_inputs = ['a', 'c', 'r']
    while True:
        selection = input("Press 'a' to add a new todo item.\n"
                          "Press 'c' to mark complete.\n"
                          "Press 'r' to remove an item.\n >>> ")

        if selection not in valid_inputs:
            print('Selected option is invalid...')
            time.sleep(2)
            continue

        else:
            break

    return selection


# asks user which day they would like to modify
def print_selection_options():
    valid_days = ['m', 't', 'w', 'th', 'f', 's', 'su', 'u']
    while True:
        new_day = input("What day?\n'm' for Monday\n't' for Tuesday\n'w' for Wednesday"
                        "\n'th' for Thursday\n'f' for Friday\n's' for Saturday"
                        "\n'su' for Sunday\n'u' for Unsure\n>>> ")

        # If input is invalid, tell the user, sleep so they can read it
        # and then restart the loop
        if new_day not in valid_days:
            print('Selected day is invalid...')
            time.sleep(2)
            continue

        if new_day == 'm':
            day_to_add = monday
        elif new_day == 't':
            day_to_add = tuesday
        elif new_day == 'w':
            day_to_add = wednesday
        elif new_day == 'th':
            day_to_add = thursday
        elif new_day == 'f':
            day_to_add = friday
        elif new_day == 's':
            day_to_add = saturday
        elif new_day == 'su':
            day_to_add = sunday
        elif new_day == 'u':
            day_to_add = unsure
        else:
            day_to_add = unsure

        # if input valid, break out of loop
        break

    return day_to_add


# If the user selects a day in which to modify (c or r) then
# they must select a number. This will only be prompted if the day
# selected has items in it. Checks for numbers within range and
# prevents crashing from string inputs.
def which_number(day):

    while True:
        num_selection = input('Which number?\n>>> ')

        try:
            num_selection = int(num_selection)
        # gets rid of invalid string inputs
            if num_selection <= len(day):
                break
            else:
                print('Selected number is out of range...')
                time.sleep(2)

        except ValueError:
            print('Selected number is invalid...')
            time.sleep(2)

    return num_selection


# Selector lets the user input what they are doing and what day
# they are doing it on. If the user selects 'c' or 'r' it requires
# a number. If the user mistakenly selects a day to modify that
# is empty, they will be told this and be brought back to the start.
def selector():
    what_to_do = add_or_remove()
    what_day = print_selection_options()

    if what_to_do == 'a':
        to_add = input('Add new todo: ')
        add_to_list(to_add, what_day)

    elif what_to_do == 'c':
        if len(what_day) == 0:
            print('Day is empty, nothing to modify.')
            time.sleep(2)
            return
        else:
            number = which_number(what_day)
            mark_complete(number, what_day)

    elif what_to_do == 'r':
        if len(what_day) == 0:
            print('Day is empty, nothing to modify.')
            time.sleep(2)
            return
        else:
            number = which_number(what_day)
            remove_item(number, what_day)


# create title for to do list!
title = input('What is the name of this todo list?\n>>> ')

todo = True

while todo:

    clear_screen()

    print(f'TODO LIST: {Colors.MAGENTA}{title}{Colors.RESET}\n')

    print_todo_items(monday, tuesday, wednesday, thursday, friday,
                     saturday, sunday, unsure)

    selector()



