from buttonDetails import buttonDetails
class Building:
    #constructor
    def __init__(self,fbuttons):
        self.fbuttons = fbuttons

class FloorDetails:
    def __init__(self):
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
        self.floorButtonDets = buttonDetails()


    @property
    def floors(self):
        return [self._create_buttons(**data) for data in self._buttonData] 


    def _create_buttons(self, id):
        buttonPolicy = self.floorButtonDets.getButton(id)
        return buttonPolicy