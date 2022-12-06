class CabService:

    # Class Variables --->
    vehicleType = ""
    vehicleOption = 0
    selectedOption: ""
    systemOption = ""

    add = ""
    vehicle = ""
    number = ""
    maxi = ""
    type_ac = ""

    # Customer Method
    @staticmethod
    def customer():
        print("\n==================== WELCOME CUSTOMER =====================")
        while True:
            main.chooseVehicle()
            main.vehicleType = input("Enter Vehicle : ")
            if main.vehicleType.lower() == "car" or main.vehicleType == "1":
                main.chooseOption("car")
                main.vehicleOption = int(input("Enter Option : "))
                main.availableQueue(main.vehicleOption, "car")
                main.exit()

            elif main.vehicleType.lower() == "van" or main.vehicleType == "2":
                main.chooseOption("van")
                main.vehicleOption = int(input("Enter Option : "))
                main.availableQueue(main.vehicleOption, "van")
                main.exit()

            elif main.vehicleType.lower() == "3 wheeler" or main.vehicleType == "3":
                main.chooseOption("3Wheeler")
                main.availableQueue(0, "3Wheeler")
                main.exit()

            elif main.vehicleType.lower() == "trucks" or main.vehicleType == "4":
                main.chooseOption("truck")
                main.vehicleOption = int(input("Enter Option : "))
                main.availableQueue(main.vehicleOption, "truck")
                main.exit()

            elif main.vehicleType.lower() == "lorry" or main.vehicleType == "5":
                main.chooseOption("lorry")
                main.vehicleOption = int(input("Enter Option : "))
                main.availableQueue(main.vehicleOption, "lorry")
                main.exit()

            elif main.vehicleType.lower() == "exit" or main.vehicleType == "99":
                print("\n============= Thank You for Join With Us...! ==============")
                break
            else:
                print("Invalid Input Please Enter Valid Input... !")

    # Admin Method
    @staticmethod
    def admin():
        print("\n====================== WELCOME ADMIN ======================")
        while True:
            print('''
                (1) Add a new vehicle to the system
                (2) Remove a vehicle from the system
                (3) Assign a job (hire)
                (4) Release form assigned job (hire) after completing
                (5) See available vehicles in each category
                (99) Exit\n''')
            main.systemOption = int(input("Enter the Task : "))

            if main.systemOption == 1:      # Add vehicle
                main.vehicle = input("Enter Vehicle ( Car / Van / 3 Wheeler / Truck / Lorry ) : ")
                main.number = int(input("Enter Vehicle Number ( xxxx ) : "))
                main.maxi = int(input("Enter Maximum Passenger Count ( x ) : "))
                main.type_ac = input("Enter Type ( AC / Non-AC ) : ")
                add = {"Vehicle": main.vehicle, "Number": main.number,
                       "Max.Passengers": main.maxi, "Type": main.type_ac}
                main.system.append(add)
                print("================ Successfully Added.... !!! ================")
                main.seeSystem(main.vehicle)

            elif main.systemOption == 2:        # Remove vehicle
                main.vehicle = input("Enter Vehicle ( Car / Van / 3 Wheeler / Truck / Lorry ) : ")
                main.number = int(input("Enter Vehicle Number ( xxxx ) : "))
                for i in main.system:
                    if main.number in i.values():
                        main.system.remove(i)
                print("================ Successfully Removed.... !!! ================")
                main.seeSystem(main.vehicle)

            elif main.systemOption == 3:        # Assign vehicle
                c = 0
                for j in main.job:
                    c += 1
                    print("(", c, ")", j)
                if c == 0:                  # When list is empty if condition is True
                    print("List Empty !")
                    while True:
                        break
                else:
                    main.assign_vehicle = int(input("\nWhich vehicle you want assign ? : "))
                    s = 1
                    for i in main.job:
                        if main.assign_vehicle == s:
                            print("You assigned vehicle ", s)
                            main.assign.append(i)
                            main.job.remove(i)
                        s += 1
                    print("================ Successfully Assigned.... !!! ================")
                    main.seeAssigned()

            elif main.systemOption == 4:        # Release vehicle
                c = 0
                for j in main.assign:
                    c += 1
                    print("(", c, ")", j)
                if not main.assign:             # When list is empty if condition is True
                    print("List Empty !")
                else:
                    main.release_vehicle = int(input("\nWhich vehicle you want release ? : "))
                    s = 1
                    for i in main.assign:
                        if main.release_vehicle == s:
                            print("You released vehicle ", s)
                            main.available.append(i)
                            main.assign.remove(i)
                        s += 1
                    print("================ Successfully Released.... !!! ================")
                    main.seeAssigned()

            elif main.systemOption == 5:        # See Available vehicle
                while True:
                    main.chooseVehicle()
                    main.vehicleType = input("Enter Vehicle Type : ")
                    if main.vehicleType.lower() == "car" or main.vehicleType == "1":
                        j = 0
                        for i in main.available:
                            if "Car" in i.values():
                                j += 1
                                print(i)
                        if j == 0:                  # When list is empty if condition is True
                            print("List Empty !")
                        main.exit()

                    elif main.vehicleType.lower() == "van" or main.vehicleType == "2":
                        j = 0
                        for i in main.available:
                            if "Van" in i.values():
                                j += 1
                                print(i)
                        if j == 0:                  # When list is empty if condition is True
                            print("List Empty !")
                        main.exit()

                    elif main.vehicleType.lower() == "3 wheeler" or main.vehicleType == "3":
                        j = 0
                        for i in main.available:
                            if "3 Wheeler" in i.values():
                                j += 1
                                print(i)
                        if j == 0:                  # When list is empty if condition is True
                            print("List Empty !")
                        main.exit()

                    elif main.vehicleType.lower() == "trucks" or main.vehicleType == "4":
                        j = 0
                        for i in main.available:
                            if "Truck" in i.values():
                                j += 1
                                print(i)
                        if j == 0:                  # When list is empty if condition is True
                            print("List Empty !")
                        main.exit()

                    elif main.vehicleType.lower() == "lorry" or main.vehicleType == "5":
                        j = 0
                        for i in main.available:
                            if "Lorry" in i.values():
                                j += 1
                                print(i)
                        if j == 0:                  # When list is empty if condition is True
                            print("List Empty !")
                        main.exit()

                    elif main.vehicleType.lower() == "exit" or main.vehicleType == "99":
                        break
                    else:
                        print("Invalid Input Please Enter Valid Input... !")

            elif main.systemOption == 99:
                print("\n============= Thank You for Join With Us...! ==============")
                break
            else:
                print("Invalid Input Please Enter Valid Input... !")

    # Print the Vehicle Types
    @staticmethod
    def chooseVehicle():
        print('''\nChoose a vehicle Type --->
                (1) Car
                (2) Van
                (3) 3 Wheeler
                (4) Trucks
                (5) Lorry
                (99) Exit\n''')

    # Print the vehicle options
    @staticmethod
    def chooseOption(option):
        while True:
            if option == "car":
                print('''Which option you want --->
                (1) Car - 3 Maximum Passengers - AC
                (2) Car - 3 Maximum Passengers - Non-AC
                (3) Car - 4 Maximum Passengers - AC
                (4) Car - 4 Maximum Passengers - Non-AC                                      
                (99) Exit\n''')
            elif option == "van":
                print('''Which option you want --->
                (1) Van - 6 Maximum Passengers - AC
                (2) Van - 6 Maximum Passengers - Non-AC
                (3) Van - 8 Maximum Passengers - AC
                (4) Van - 8 Maximum Passengers - Non-AC                                       
                (99) Exit\n''')
            elif option == "3Wheeler":
                print('''Maximum Number of Passengers - 3''')
            elif option == "truck":
                print('''Which option you want --->
                (1) Truck - 7 feet
                (2) Truck - 12 feet                                       
                (99) Exit\n''')
            elif option == "lorry":
                print('''Which option you want --->
                (1) Lorry - Maximum Load & Size 2500Kg
                (2) Lorry - Maximum Load & Size 3500Kg                                       
                (99) Exit\n''')
            else:
                print("Invalid Input Please Enter Valid Input... !")
            break

    # This is called in Customer Method
    @staticmethod
    def availableQueue(option, vehicle):
        if vehicle == "car" and option == 1:
            main.checkAvailability(3, "AC")
        elif vehicle == "car" and option == 2:
            main.checkAvailability(3, "Non-AC")
        elif vehicle == "car" and option == 3:
            main.checkAvailability(4, "AC")
        elif vehicle == "car" and option == 4:
            main.checkAvailability(4, "Non-AC")
        elif vehicle == "van" and option == 1:
            main.checkAvailability(6, "AC")
        elif vehicle == "van" and option == 2:
            main.checkAvailability(6, "Non-AC")
        elif vehicle == "van" and option == 3:
            main.checkAvailability(8, "AC")
        elif vehicle == "van" and option == 4:
            main.checkAvailability(8, "Non-AC")
        elif vehicle == "3Wheeler" and option == 0:
            main.checkAvailability(3, "-")
        elif vehicle == "truck" and option == 1:
            main.checkAvailability(7, "-")
        elif vehicle == "truck" and option == 2:
            main.checkAvailability(12, "-")
        elif vehicle == "lorry" and option == 1:
            main.checkAvailability(2500, "-")
        elif vehicle == "lorry" and option == 2:
            main.checkAvailability(3500, "-")
        elif option == 99:
            while True:
                break
        else:
            print("Invalid Input Please Enter Valid Input... !")

    # This is called in availableQueue
    @staticmethod
    def checkAvailability(maximum, ac_type):
        print("Available Vehicles --->")
        j = 0
        for i in main.available:
            if maximum in i.values() and ac_type in i.values():
                j += 1
                print("(", j, ")", i)
        if j == 0:                          # When list is empty if condition is True
            print("List Empty !")
            while True:
                break
        else:
            main.selectFromQueue(maximum, ac_type)

    # Select a vehicle from available options
    @staticmethod
    def selectFromQueue(maximum, ac_type):
        main.selectedOption = int(input("\nEnter your vehicle : "))
        s = 1
        for i in main.available:
            if maximum in i.values() and ac_type in i.values():
                if main.selectedOption == s:
                    print("You selected option", s)
                    main.job.append(i)
                    main.available.remove(i)
                    print("================ Booking Successfully.... !!! ================")
                s += 1

    # This run from Admin part to see system vehicles
    @staticmethod
    def seeSystem(vehicle):
        print("\nDo You want to see system", vehicle, "...!")
        see = input("yes/ no ? : ")
        j = 0
        if see == "yes":
            for i in main.system:
                if vehicle in i.values():
                    j += 1
                    print(i)
            if j == 0:                      # When list is empty if condition is True
                print("List Empty !")
            main.exit()
        else:
            while True:
                break

    # This run from Admin part to see assigned vehicles
    @staticmethod
    def seeAssigned():
        print("\nDo You want to see assigned list ? ")
        see = input("yes/ no ? : ")
        j = 0
        if see == "yes":
            for i in main.assign:
                j += 1
                print("(", j, ")", i)
            if j == 0:                      # When list is empty if condition is True
                print("List Empty !")
            main.exit()
        else:
            while True:
                break

    # This is main method which run first
    def main(self):
        while True:
            print("\n======================= CAB SERVICE =======================")
            print('''
                (1) Customer
                (2) Admin\n''')

            login = input("Enter User Type : ")
            if login.lower() == "customer" or login.lower() == "1":
                self.customer()
            elif login.lower() == "admin" or login.lower() == "2":
                self.admin()
            else:
                print("Invalid Input Please Enter Valid Input... !")

    # when calling exit method after the tasks this will run
    @staticmethod
    def exit():
        p = input("\nPress Enter to Exit")
        if not p:
            print("Exiting............")
            while True:
                break

    # Lists --->

    system = [
        # "CARS":
        {"Vehicle": "Car", "Number": 1001, "Max.Passengers": 3, "Type": "AC"},
        {"Vehicle": "Car", "Number": 1002, "Max.Passengers": 3, "Type": "AC"},
        {"Vehicle": "Car", "Number": 1003, "Max.Passengers": 3, "Type": "Non-AC"},
        {"Vehicle": "Car", "Number": 1004, "Max.Passengers": 3, "Type": "Non-AC"},
        {"Vehicle": "Car", "Number": 1005, "Max.Passengers": 4, "Type": "AC"},
        {"Vehicle": "Car", "Number": 1006, "Max.Passengers": 4, "Type": "AC"},
        {"Vehicle": "Car", "Number": 1007, "Max.Passengers": 4, "Type": "AC"},
        {"Vehicle": "Car", "Number": 1008, "Max.Passengers": 4, "Type": "Non-AC"},
        {"Vehicle": "Car", "Number": 1009, "Max.Passengers": 4, "Type": "Non-AC"},
        {"Vehicle": "Car", "Number": 1010, "Max.Passengers": 4, "Type": "Non-AC"},

        # "VANS":
        {"Vehicle": "Van", "Number": 2001, "Max.Passengers": 6, "Type": "AC"},
        {"Vehicle": "Van", "Number": 2002, "Max.Passengers": 6, "Type": "AC"},
        {"Vehicle": "Van", "Number": 2003, "Max.Passengers": 6, "Type": "Non-AC"},
        {"Vehicle": "Van", "Number": 2004, "Max.Passengers": 6, "Type": "Non-AC"},
        {"Vehicle": "Van", "Number": 2005, "Max.Passengers": 8, "Type": "AC"},
        {"Vehicle": "Van", "Number": 2006, "Max.Passengers": 8, "Type": "AC"},
        {"Vehicle": "Van", "Number": 2007, "Max.Passengers": 8, "Type": "AC"},
        {"Vehicle": "Van", "Number": 2008, "Max.Passengers": 8, "Type": "Non-AC"},
        {"Vehicle": "Van", "Number": 2009, "Max.Passengers": 8, "Type": "Non-AC"},
        {"Vehicle": "Van", "Number": 2010, "Max.Passengers": 8, "Type": "Non-AC"},

        # "3WHEELERS":
        {"Vehicle": "3 Wheeler", "Number": 3001, "Max.Passengers": 3, "Type": "-"},
        {"Vehicle": "3 Wheeler", "Number": 3002, "Max.Passengers": 3, "Type": "-"},
        {"Vehicle": "3 Wheeler", "Number": 3003, "Max.Passengers": 3, "Type": "-"},
        {"Vehicle": "3 Wheeler", "Number": 3004, "Max.Passengers": 3, "Type": "-"},

        # "TRUCKS":
        {"Vehicle": "Truck", "Number": 4001, "Max.Long": 7, "Type": "-"},
        {"Vehicle": "Truck", "Number": 4002, "Max.Long": 7, "Type": "-"},
        {"Vehicle": "Truck", "Number": 4003, "Max.Long": 12, "Type": "-"},

        # "LORRIES":
        {"Vehicle": "Lorry", "Number": 5001, "Max.Load and Size": 2500, "Type": "-"},
        {"Vehicle": "Lorry", "Number": 5002, "Max.Load and Size": 2500, "Type": "-"},
        {"Vehicle": "Lorry", "Number": 5003, "Max.Load and Size": 3500, "Type": "-"}
    ]
    available = system
    job = []
    assign = []


main = CabService()     # main object
main.main()
