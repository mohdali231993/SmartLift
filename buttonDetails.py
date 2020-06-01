from Button import Button
from LiftButton import LiftButton
from FloorButton import FloorButton
class buttonDetails:
    def __init__(self):
        self._buttonPolicy = {
            
                1: LiftButton('1',False,1),
                2: LiftButton('2',False,2),
                3: LiftButton('3',False,3),
                4: LiftButton('4',False,4),
                5: LiftButton('5',False,5),
                6: LiftButton('6',False,6),
                7: LiftButton('7',False,7),
                8: LiftButton('8',False,8),
                9: LiftButton('9',False,9),
                10: LiftButton('10',False,10)
        }
        self._floorButtonPolicy = {
            
                1: FloorButton('1',False,1),
                2: FloorButton('2',False,2),
                3: FloorButton('3',False,3),
                4: FloorButton('4',False,4),
                5: FloorButton('5',False,5),
                6: FloorButton('6',False,6),
                7: FloorButton('7',False,7),
                8: FloorButton('8',False,8),
                9: FloorButton('9',False,9),
                10: FloorButton('10',False,10)
        }

    def getButton(self, button_id):
        buttonP = self._buttonPolicy.get(button_id)
        if not buttonP:
            return ValueError(button_id)
        return buttonP    


        