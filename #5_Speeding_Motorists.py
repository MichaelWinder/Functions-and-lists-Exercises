def speeding_Motorists():
    null = 1
    while null == 1:
        trip = input("Do you want to record a trip? ").lower()
        while trip not in ("yes", "no"):
            trip = input("Do you want to record a trip? ").lower()
        if trip == "yes":
            time_Of_Trip = int(input("How many minutes was your trip? "))
            time_Driving.append(time_Of_Trip)
            print(f"The trip costs ${time_Of_Trip * 2 + 10}\n")
            cost_Of_Trips.append(time_Of_Trip * 2 + 10)
        else:

            null = 0
