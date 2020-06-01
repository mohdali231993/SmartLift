from buttonDetails import buttonDetails
class Lift:
    #constructor
    def __init__(self,id,liftNumber,functioning,lbuttons,currentFloor,direction):
        self.id = id
        self.liftNumber = liftNumber    
        self.functioning = functioning
        self.lbuttons = lbuttons
        self.currentFloor = currentFloor
        self.direction = direction
        

    
    def getButtonsPressed(self):
        pass
    def getCurrentFloor(self):
        return self.currentFloor
    def setCurrentFloor(self,currentFloor):
        self.currentFloor = currentFloor 
    def getDirection(self):
        return self.direction
    def setDirection(self,direction):
        self.direction = direction
    def getHealth(self):
        return self.functioning   
    def setHealth(self,functioning):
        self.functioning = functioning        

          

class liftDetails:
    def __init__(self):
        self._liftData = [
            {
                'id' : 1,
                'liftNumber' : 1,
                'functioning' : "True",
                'currentFloor' : 1,
                'direction' : 0
            },
        ]
        self._buttonData = [
            {
                'id' : 1
            },
            {
                'id' : 2
            },
            {
                'id' : 3
            },
            {
                'id' : 4
            },
            {
                'id' : 5
            },
            {
                'id' : 6
            },
            {
                'id' : 7
            },
            {
                'id' : 8
            },
            {
                'id' : 9
            },
            {
                'id' : 10
            },
        ]
        self.buttonDets = buttonDetails()
        

    @property
    def lifts(self):
        return [self._create_lift(**data) for data in self._liftData]

    @property
    def buttons(self):
        return [self._create_buttons(**data) for data in self._buttonData]    



    def _create_lift(self, id, liftNumber, functioning, currentFloor, direction):
        lbuttons = self.buttons
        return Lift(id, liftNumber, functioning, lbuttons, currentFloor, direction)

    
    def _create_buttons(self, id):
        buttonPolicy = self.buttonDets.getButton(id)
        return buttonPolicy
    