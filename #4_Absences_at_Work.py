nameDict = {
    "Michael": 80,
    "Ethan": 23,
    "Hunter": 12,
    "Bob": 0,
    "Jimmy": 0,
}
zeroAbsent = []
name_above_ave = []
above_ave = []


def absences():
    null = 1
    while null == 1:
        absence = input("Do you want to record a Absence? (yes or $ "
                        "for no) ").lower()
        while absence not in ("yes", "$"):
            absence = input("Do you want to record a Absence? (yes or $ "
                            "for no) ").lower()
        if absence == "yes":
            name = input("What is the name of the employee? ").capitalize()
            days_off = int(input(f"How many days has {name} been absent? "))
            nameDict[name] = days_off
        else:
            abs_days_ave = sum(nameDict.values()) / len(nameDict.values())
            most_days_abs = max(nameDict.values())
            for i in nameDict:
                if nameDict[i] == most_days_abs:
                    name_most_days_abs = i
            for i in nameDict:
                if nameDict[i] == 0:
                    zeroAbsent.append(i)
            for i in nameDict:
                if nameDict[i] >= abs_days_ave:
                    name_above_ave.append(i)
                    above_ave.append(nameDict[i])
            print(f"The average number of days of absences is "
                  f"{abs_days_ave:.2f} days")
            # Gets the key for the person with the most days absent from the value and prints
            print(f"The person with the most days absent is: "
                  f"{name_most_days_abs} "
                  f"with {most_days_abs} days off")
            print(", ".join(zeroAbsent))
            print("Have not had a day absent")
            while len(above_ave) > 0:
                print(name_above_ave.pop(), above_ave.pop())
            print("These are the people with above average days absent.")


            null = 0


absences()
