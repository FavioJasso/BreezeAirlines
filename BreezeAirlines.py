#####################################################################################################
# Lab 3: Breeze Airlines Application                                                                #
# Authored by: Favio Valentino Jasso and Julian Gelin                                                                         #
# For: CMP131-20237 Fundamentals of Programming (Python)                                            #
# At: County College of Morris, Dept. of Information Technologies                                   #
# Professor Tirrito                                                                                 #
# Date Modified: Monday April 15th, 2024                                                            #
#####################################################################################################

def main():
    #SEAT INDEX: 
    #Seat A: 0 
    #Seat B: 1 
    #Seat C: 2 
    #Seat D: 3 
    #Seat E: 4 
    #Seat F: 5
    #Class level: 6 

    #COURSE MEMBER INDEX:
    #First name = 0 
    #MI = 1
    #Last Name = 2
    #Passenger num = 3
    #Premium charge = 4 

    seat_map = [["!", "$$$", "!", "!", "$$$", "!", "First Class"],
                ["$$$", "!", "!", "!", "$$$", "$$$", "First Class"],
                ["!", "$$","!", "!", "$$", "!", "Business Class"],
                ["!", "$$", "$$", "!", "$$", "!", "Business Class"],
                ["$$", "$$", "!", "!", "$$", "!", "Business Class"],
                ["!", "!", "!", "!", "!", "!", "Exit Row"],
                ["!", "!", "!", "!", "!", "!", "Exit Row"],
                ["!", "!", "!", "!", "!", "!", "Exit Row"],
                ["!", "@", "!", "!", "@", "@", "Economy Class"],
                ["!", "@", "@", "!", "!", "@", "Economy Class"],
                ["@", "!", "!", "!", "!", "@", "Economy Class"],
                ["@", "@", "@", "@", "@", "@", "Econmy Class"],
                ["!", "!", "!", "@", "!", "!", "Econmy Class"],
                ["$", "$", "$", "$", "$", "$", "Exit Row"],
                ["$", "!", "!", "!", "!", "!", "Exit Row"],
                ["!", "!", "!", "!", "!", "!", "Economy Class"],
                ["!", "!", "!", "!", "!", "!", "Economy Class"],
                ["!", "!", "!", "!", "!", "!", "Economy Class"],
                ["!", "@", "@", "!", "@", "!", "Economy Class"],
                ["!", "!", "@", "!", "!", "@", "Economy Class"],]
    
    symbol = "#"

    welcome_banner(symbol)
    print("Our class has been selected by the school to attend a Computer Science Symposium in Fort Lauderdale, Florida " +
          "to compete in a national programming challenge of community college students. The school will fund basic economy " +
          "flights for all n students in the class, and the professor as a chaperone to attend the competition. Any seat " +
          "upgrades are the sole responsibility of the individual. The flight has been booked, but seating is getting limited. " +
          "We need to develop a Python application that will help us selectthe least expensive options left to assign seats " +
          "to every student and the professor. Priority will be placed on students first for remaining free seats, and " +
          "then the professor. The school will lay out the funds to cover necessary seat upcharges to book the seats, but " +
          "students and faculty accounts will be billed these charges accordingly.\n")
    print("This program will assit in assigning the cheapest seats first before seat upgrades start getting assigned. After "+
          "entering the number of course members that are supposed to be booked on the flight, this program will assign "+
          "free seating first to students and then the professor for all available free seating on the flight. After all "+
          "all free seating has been taken, seat upgrades will be given out starting at the cheapest option up to the most "+
          "expensive option. Exit row will be a premium charge of $100, business class will be a premium charge of $500, "+
          "and first class will be a premium charge of $1000. After all seating has been assigned you will be notified about "+
          "the grand total of the premium charges for seat upgrades. You will be notified about what course member was charged "+
          "a premium amount for a seat upgrade including the charge amount. You will also be shown the seating map of where each "+
          "course member was seated, referenced by their passenger number.\n")
    
    course_members = create_course_members_list()
    premium_charges = assign_seats(seat_map, course_members) ## Premium_charges is a list of the total amount of charges in each upgrade class ##
    grand_total = calculate_premium_charges(premium_charges)
    print("\nPremium Charges Grand Total: $" + str(grand_total))
    print("\nMembers Charged for Premium Seating:")
    show_upgraded_members(course_members)
    print("\nSeating Map:")
    print("Map Legend: ! = Unavailable, @ = Available free seating, $ = Available exit row seat, $$ = Available business class seat. "+
          "$$$ = Available first class seat")
    show_seat_map(seat_map)
    print()
    closing_banner(symbol)



## Show records of members who were upgraded ##
def show_upgraded_members(course_members):
    ## enumerate is keeping track of the current list within the nested list ##
    for member_index, row in enumerate(course_members):
        if row[4] == 100:
            print(row)
        elif row[4] == 500:
            print(row)
        elif row[4] == 1000:
            print(row)

## Calculate grand total of premium charges ##
def calculate_premium_charges(premium_charges):
    grand_total = 0

    for i in range(len(premium_charges)):
        grand_total += premium_charges[i]

    return grand_total

## assign seats ##
def assign_seats(seat_map, course_members):
    ## Variables to keep track of premium seating charges ## 
    exit_row = 0
    business_class = 0
    first_class = 0
    
    ## keeps track of the member we are assigning. Assumes first member is at index 0 ##
    member_index = 0
    ## Fills all available free seating before anything else ##
    for row_index, row in enumerate(seat_map):
        for seat_index, seat in enumerate(row):
            if seat == "@" and member_index < len(course_members):
                member_number = course_members[member_index][3]
                seat_map[row_index][seat_index] = member_number
                member_index += 1
    print("All available free seating have been filled.")
    print("NOW FILLING EXIT ROW AT A PREMIUM CHARGE OF $100")

    ## Fill in exit row before assigning to business class ##
    for row_index, row in enumerate(seat_map):
        for seat_index, seat in enumerate(row):
            if seat != "!" and seat != "@" and member_index < len(course_members):
                if seat == "$":
                    exit_row += 100
                    member_number = course_members[member_index][3]
                    seat_map[row_index][seat_index] = member_number
                    course_members[member_index][4] = 100
                    member_index += 1
    print("All available exit row seating have been filled.")
    print("NOW FILLING BUSINESS CLASS AT A PREMIUM CHARGE OF $500")
                  
    ## Fill in business class before assigning first class ##
    for row_index, row in enumerate(seat_map):
        for seat_index, seat in enumerate(row):
            if seat != "!" and seat != "@" and member_index < len(course_members):
                if seat == "$$":
                    business_class += 500
                    member_number = course_members[member_index][3]
                    seat_map[row_index][seat_index] = member_number
                    course_members[member_index][4] = 500
                    member_index += 1
    print("All available business class seats have been filled.")
    print("NOW FILLING FIRST CLASS AT A PREMIUM CHARGE OF $1000.")
                    
    ## Fill in first class only if no other available seating ##
    for row_index, row in enumerate(seat_map):
        for seat_index, seat in enumerate(row):
            if seat != "!" and seat != "@" and member_index < len(course_members):
                if seat == "$$$":
                    first_class += 1000
                    member_number = course_members[member_index][3]
                    seat_map[row_index][seat_index] = member_number
                    course_members[member_index][4] = 1000
                    member_index += 1
    print("All first class seats have been filled.")
               
    
    premium_charges = [exit_row, business_class, first_class]
    return premium_charges
                

## Display the seating map of the flight ## 
def show_seat_map(seat_map):
    print("Seat A, Seat B, Seat C, Seat D, Seat E, Seat F, Class level")
    row_num = 1
    for row in seat_map:
        print("row",row_num, row)
        row_num += 1 
    ##Cant figure out how to format seat map to match constraint 

## create a list for course members. Size depends on user input ## 
def create_course_members_list():
    ## Boolean variable for try/except block 
    valid_input = False
    ## while not executes as long as condition is false
    while not valid_input:
        try:
            course_members = int(input("Enter the number of course members, including the professor: "))
            if 0 < course_members <= 40:
                valid_input = True
            elif course_members <= 0:
                print("Cannot not assign seats for an empty group. Please enter a number above zero.")
            else:
                print(str(course_members) + " is too many people for the amount of seats available this flight. " +
                      "Please enter a number that can accommodate for 40 seats.")
        except ValueError:
            print("Invalid input. Please enter a valid number, (1,2,3,etc...).")

    nested_list = []

    # Assumes that first course members gets assigned passenger number 1 ## 
    passenger_num = 1

    for i in range(course_members):
        row_contents = [''] * 5  ## This means that each list within the nested list will have a length of 5 
        row_contents[0] = "First Name"
        row_contents[1] = "MI"
        row_contents[2] = "Last Name"
        row_contents[3] = passenger_num
        row_contents[4] = "Premium Charge"
        passenger_num += 1
        nested_list.append(row_contents) ##Puts created list into the main list ##

    return nested_list

## Welcome Banner ##
def welcome_banner(symbol):
     
 # VARIABLE INITIALIZATIONS
    topBorder = ''
    bottomBorder = ''

 # CONSTRUCTING THE TOP BORDER LINE USING A COUNT-CONTROLLED LOOP
    for i in range(80):
        topBorder += symbol
 
 # CONSTRUCTING THE BOTTOM BORDER LINE AS A COPY OF THE TOP BORDER
    bottomBorder = topBorder

 # PRINTING THE WELCOME BANNER
    print(topBorder)
    print(symbol + f"{'Welcome to the Breeze Airlines Application':^78}" + symbol)
    print(symbol + f"{'Written by: Favio Valentino Jasso & Julian Gelin':^78}" + symbol)
    print(symbol + f"{'Date Written: Monday April 15th, 2024':^78}" + symbol)
    print(bottomBorder)
    print()

    return symbol

## Closing Banner ##
def closing_banner(symbol):
    
    # VARIABLE INITIALIZATIONS
    topBorder = ''
    bottomBorder = ''
    
    # CONSTRUCTING THE TOP BORDER LINE USING A COUNT-CONTROLLED LOOP
    for i in range(80):
        topBorder += symbol
        
    # CONSTRUCTING THE BOTTOM BORDER LINE AS A COPY OF THE TOP BORDER
    bottomBorder = topBorder
    
    # PRINTING THE CLOSING BANNER
    print(topBorder)
    print(symbol + f"{'Thank You for using the Breeze Airlines Application':^78}" + symbol)
    print(symbol + f"{'Written by: Favio Valentino Jasso & Julain Gelin':^78}" + symbol)
    print(symbol + f"{'Date Written: Monday April 15th, 2024':^78}" + symbol)
    print(symbol + f"{'THIS PROGRAM WILL NOW TERMINATE':^78}" + symbol)
    print(bottomBorder)
    print()
    # END OF CLOSING BANNER
    
 
main()