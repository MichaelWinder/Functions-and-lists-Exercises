import time

child_List = ["Billy", "Bob", "Ethan"]
number_List = [1, 2, 3]


def welcome_Screen():
    null = 1
    while null == 1:
        try:
            option = int(input("\nWelcome to MGS Childcare!\nHow do you want "
                               "to "
                               "proceed?\n1. Drop "
                               "off Child\n2. Pickup Child\n3. Calculate the "
                               "cost of "
                               "Childcare\n4. See role of Children currently in "
                               "care\n5."
                               " Execute\n"))
            null = 0
        except ValueError:
            null = 1
    if option == 1:
        drop_Off()
    elif option == 2:
        pickup()
    elif option == 3:
        calculate_Cost()
    elif option == 4:
        print_Roll()
    else:
        quit("GET OUT!")


def drop_Off():
    child_List.append(input("What is your Child's name? :) ").capitalize())
    number_List.append(len(number_List) + 1)
    print(child_List)
    time.sleep(0.5)
    welcome_Screen()


def pickup():
    try:
        child_List.remove(input("What is your Child's name? :) ").capitalize())
    except ValueError:
        print("That child is not on the role")
        welcome_Screen()
    print(f"{child_List}\n")
    calculate_Cost()


def calculate_Cost():
    hours = int(input("How many Hours has your Child been at MGS Childcare? "))
    print(f"That will charge you ${hours * 12}")
    time.sleep(2)
    welcome_Screen()


def print_Roll():
    print(f"{child_List}\nThere are {len(child_List)} Children at the MGS "
          f"care Center")
    time.sleep(2)
    welcome_Screen()


welcome_Screen()
