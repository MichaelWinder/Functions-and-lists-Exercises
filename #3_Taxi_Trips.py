def trip_Calculator():
    time_Driving = []
    cost_Of_Trips = []
    driver_Name = input("What is your name? ")
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
            print(f"\nFor the driver {driver_Name}\nThe total time of all "
                  f"trips is {sum(time_Driving)} minutes\nThe average time "
                  f"of all trips is "
                  f"{(sum(time_Driving)/len(time_Driving)):.1f} "
                  f"minutes\nThe total income for the day is $"
                  f"{sum(cost_Of_Trips)}\nThe average cost of all trips is "
                  f"${(sum(cost_Of_Trips)/len(cost_Of_Trips)):.2f}")
            null = 0


trip_Calculator()
