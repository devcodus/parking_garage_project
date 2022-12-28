class parkingGarage:
    
    tickets = {} #where we will save ticket number and linked to the time that car is in lot
    garage = {'spaces': 9, 'ticketsTaken': 1}
    
        

    #def __init__(self):
    #this is used for specific information, not for something as general as a parking garage


#how many parking spaces are left:
   
    def available(self):
        if self.garage['spaces'] == 0:
            print(f"Unfortunately, we have {self.garage['spaces']} parking spaces left.")
            return self.garage['spaces']
        else:
            print(f"We have {self.garage['spaces']} left")

#pay for a spot in the garage when they arrive and links to ticket number and time so that time in lot is billed correctly.
    def takeTicket(self):
        time = input("How many hours do you plan to stay with us today?")
        if time.isdigit():
            #is.digit() checks to see if the value inputted is actually an integer or not
            currentTicket = self.garage['ticketsTaken']
            self.tickets[currentTicket] = time
            print (f'Your ticket number is: {currentTicket}')
            self.garage['ticketsTaken'] += 1
            self.garage['spaces'] -= 1
        else:
            print('Invalid entry, please try again!')
            #call function again
            self.takeTicket()   

#current ticket is key and the value will be time. whenever you store ticket, it will be storing ticket and time

    def leaveGarage(self):
            payment = int(time) * 2
            print (f'You owe: ${payment}.') 
            payoption = input('Would you like to pay with cash or card?')
    
            
            
#Ticket number, locate ticket in tickets dictionary, then multiply time associated with ticket by rate then you owe blah blah cash or card.
#increment spaces up to account for new availability
           


    # def payforParking(self):
    #     time = int(input('How long are you planning on parking with us today?'))
    #     if time != []:
    #         time = False
    #         print ('Your ticket has been paid, you have 15mins to exit the lot! Thank you and have a great day!')
            # self.currentTicket  = True
            
    

    #     #pay for parking is done, so now display message:
    #     print ('Thank you and have a great day!')
    #     if unpaid > 0:
    #         unpaid = int(input('How long would you like to park for?'))
    #     self.parkingSpaces += 1
    #     self.tickets += 1

theparkinggarage = parkingGarage()
print (theparkinggarage.parkingSpaces)