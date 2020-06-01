from Lift import liftDetails
from Building import FloorDetails

lift_Details = liftDetails()
elevators = lift_Details.lifts
floor_Details = FloorDetails()
floors = floor_Details.floors

def setCurrentFloor(lift,floorNumber):
    elevators[lift-1].setCurrentFloor(floorNumber)



def pressButton(lift,floorNumber):
    elevators[lift-1].lbuttons[floorNumber-1].flipStatus()
    target = goingTo(lift)

def pressFloorButton(floorNumber):
    floors[floorNumber-1].flipStatus()
    target = goingTo(1)    
 

def goingTo(lift):
    target = 0 # o means going nowhere, 1 means up, and 2 means going down.
    if(elevators[lift-1].getDirection() == 0):
        #print("Scenario 1")
        for floor in range(1,11):
            if(elevators[lift-1].lbuttons[floor-1].getStatus() == True or floors[floor-1].getStatus() == True):
                target = floor   
        if(elevators[lift-1].getCurrentFloor() < target):
            elevators[lift-1].setDirection(2)
        elif elevators[lift-1].getCurrentFloor() > target:
            elevators[lift-1].setDirection(1)
        elif elevators[lift-1].getCurrentFloor() == target:        
            elevators[lift-1].setDirection(0)
            if  elevators[lift-1].lbuttons[target - 1].getStatus() == True:
                elevators[lift-1].lbuttons[floor-1].flipStatus()
            elif floors[target-1].getStatus() == True:
                floors[target - 1].flipStatus()
    elif(elevators[lift-1].getDirection() == 1):
        #print("Scenario 2")
        for floor in range(elevators[lift-1].getCurrentFloor(),0,-1):
            if(elevators[lift-1].lbuttons[floor-1].getStatus() == True or floors[floor-1].getStatus() == True):
                target = floor
    elif(elevators[lift-1].getDirection() == 2):
        #print("Scenario 3")
        for floor in range(elevators[lift-1].getCurrentFloor(),11):
            if(elevators[lift-1].lbuttons[floor-1].getStatus() == True or floors[floor-1].getStatus() == True):
                target = floor
    if target == 0:
        #print("Scenario 4")
        target = elevators[lift-1].getCurrentFloor()
    return target

setCurrentFloor(1,5)
source =  elevators[0].getCurrentFloor() 
print("source = ",source)
pressButton(1,4)
pressFloorButton(2)
destination = goingTo(1)
print("destination = ",destination)


