class parkingGarage:
    
    tickets = {} #where we will save ticket number and linked to the time that car is in lot
    garage = {'spaces': 9, 'ticketsTaken': 1}
    
        

    #def __init__(self):
    #this is used for specific information, not for something as general as a parking garage
    #we're not making instances of 'cars' or 'animals'

#how many parking spaces are left:
   
    def available(self):
        if self.garage['spaces'] == 0:
            print(f"Unfortunately, we have {self.garage['spaces']} parking spaces left.")
            return self.garage['spaces'] ##why are we returning self.garage['spaces'] here?
        else:
            print(f"Welcome, we have {self.garage['spaces']} spaces available in the lot at the moment!")##should we also return self.garage['spaces'] here?
            #so how much time do you want to stay? lock it in to the key of the dictionary
            #parking spot 1 : 2 Hrs

#pay for a spot in the garage when they arrive and links to ticket number and time so that time in lot is billed correctly.
    def takeTicket(self):
        time = input("How many hours do you plan to stay with us today? ")
        if time.isdigit():
            #is.digit() checks to see if the value inputted is actually an integer or not
            currentTicket = self.garage['ticketsTaken'] 
            self.tickets[currentTicket] = time 
            print (f'Your ticket number is: {currentTicket}')
            self.garage['ticketsTaken'] += 1
            #next ticket number is gonna be higher starting from 1!
            self.garage['spaces'] -= 1
            #incrementing down as people enter lot
            reset = input('Do you need another ticket? ')
            if reset.lower() == 'yes':
                self.takeTicket()
            else:
                self.available()
            #reset for next customer after ticket is taken
        else:
            print('Invalid entry, please try again!')
            #call function again
            self.takeTicket()
#current ticket is key and the value will be time. whenever you store ticket, it will be storing ticket and time in tickets dictionary.
  

#Notes to self: Ticket number, locate ticket in tickets dictionary, then multiply time associated with ticket by rate then you owe blah blah cash or card.
#increment spaces up to account for new availability

    def leaveGarage(self):
        #is this ticket id in the dict? if it is, we pass that id in and get the value which is time associated with that key!
            exitTicket = int(input('What is your ticket number? '))
            print (self.tickets)
            #if self.tickets != exitTicket:
            if not self.tickets[exitTicket]:
                #"if not" acts as a true false statement (boolean) 
                print ('Invalid ticket, please try again.')
                #self.leaveGarage()
            else:
                payment = int(self.tickets[exitTicket]) * 2
                print (f'You owe: ${payment}. You have 15 minutes to leave the garage.') 
                payoption = input('Would you like to pay with cash or card? ')
            if payoption.lower() == 'cash' or 'card': 
                self.garage['spaces'] += 1
                #incrementing spaces when lot empties
                print ('Thank you for visting the garage, please come again soon!')
            else: 
                print(f'You must pay ${payment} before leaving the lot. Please try again.')
                self.leaveGarage()
           


theparkinggarage = parkingGarage()
theparkinggarage.available()
theparkinggarage.takeTicket()
theparkinggarage.leaveGarage()