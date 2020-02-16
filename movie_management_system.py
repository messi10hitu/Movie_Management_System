def ticket():
    name = input("plz enter your name: ")
    contact = int(input("plz enter your contact no: "))
    no_of_seats = int(input("plz enter no of seats you want to book: "))
    return [{'success': 1, 'ticketData': [name, contact, no_of_seats]}]



def book():
    ticketData = []
    ticketData.extend(ticket())
    return ticketData


def update():
    newname = ""
    flag = True
    while flag:
        userchoice = input("what do you want to update: ")
        if userchoice == 'name':
            def namechange():
                name = input("plz enter new name: ")
                return name

            newname = newname.replace((), namechange())


# main program
print("------Bus Ticket Management System--------")
print("for booking a ticket press 'b' or 'B'")
print("for updating a ticket press 'u' or 'U'")
print("for canceling a ticket press 'c' or 'C'")
print("for reciept of a ticket press 'r' or 'R'")

ticketBook = []
ticketUpdate = []
cancel = ""
flag = True
userinput = input("enter your choice: ")
while flag:
    if userinput == 'b' or userinput == 'B':
        ticketBook.extend([book()])
    elif userinput == 'u' or userinput == 'U':
        ticketUpdate.extend([update()])
    elif userinput == 'c' or userinput == 'C':
        pass
        # for the reciept of the ticket
    elif userinput == 'r' or userinput == 'R':
        for item in ticketBook[0]:
            print("Name of the Movie: " + item['ticketData'][0], " \nyear of release: " + item['ticketData'][1],
                  "\nrating: " + item['ticketData'][2])
    else:
        print(">>>Invalid Option!!! Please Try Again!!!")
