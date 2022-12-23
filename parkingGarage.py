class parkingGarage:
    pg = {
        1 : {
            'paid': False,
            'full' : False
        }
        , 
    }
    def __init__(self):
        self.tickets = []
        self.vehicle = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.parkingSpaces = 9
        self.currentTicket = {'paid': False}
    def available(self):
        return self.parkingSpaces
    def takeTicket(self):
        # ticket = input(f'Welcome to our parking garage. We have {self.parkingSpaces} available')
        if self.parkingSpaces > 0:
            self.tickets.append()
            self.parkingSpaces -= 1
            self.tickets -= 1
        # pass

    def payforParking(self):
        time = int(input('How long are you planning on parking with us today?'))
        if time != "":
            print ('Your ticket has been paid, you have 15mins to exit the lot! Thank you and have a great day!')
            self.currentTicket  = True

    def leaveGarage(self):
        #pay for parking is done, so now display message:
        print ('Thank you and have a great day!')
        if unpaid > 0:
            unpaid = int(input('How long would you like to park for?'))

        self.parkingSpaces += 1
        self.tickets += 1
