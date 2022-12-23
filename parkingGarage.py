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
        self.currentTicket = {}

    def available(self):
        return self.parkingSpaces

    def takeTicket(self):
        # ticket = input(f'Welcome to our parking garage. We have {self.parkingSpaces} available')
        if self.parkingSpaces > 0:
            self.tickets.append()
            self.parkingSpaces -= 1
            self.tickets -= 1
        # pass

    

    