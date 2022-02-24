# THE TWO NUMBERS SUM OF A GIVEN LIST
# this code helps in printing nout two numbers in a given array that adds up to a desired target
try:
    import itertools  # importing the looping module
    while True:
        num_list = []
        print('THIS CODE  HELPS IN PRINTING OUT TWO NUMBERS IN A GIVEN ARRAY THAT ADDS UP TO A PARTICULAR TARGET'
              '\nNote the number 0 cannot belong to the list')
        print('After entering all numbers in your list, press zero to end\n')  # teaching the user how to break out
        # of the loop
        for i in range(1, 1000001):
            user_numbers = int(input(f'Enter the {i} number: '))
            num_list.append(user_numbers)
            if user_numbers == 0:
                break
            else:
                continue
        num_list.remove(0)  # Removing the item used to break out of the loop
        target = int(input('Enter your desired target: '))
        com_num_list = itertools.combinations(num_list, 2)  # looping through the list and printing out two items
        print(f'In all the numbers {num_list} the number below adds up to the target {target}\n')
        for result in com_num_list:
            if sum(result) == target:  # Using the inbuilt sum function to help add the two items gotten from the loop
                print(result)
        repeat_code = input('Enter 1 to re-run code, enter 2 to end: ')
        if repeat_code == '1':
            continue
        else:
            break
except Exception:
    print('INVALID INFORMATION ENTERED')
