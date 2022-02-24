#!/usr/bin/python3

def createBuildingFloorEntryObject(index, value, building):
    if index == 0:
        building.setName(value)
    elif index == 1:
        building.setFloor(value)
    elif index == 2:
        building.setMaterial(value)
    elif index == 3:
        building.setBudget(value)
    elif index == 4:
        building.setCurrentStock(value)
    elif index == 5:
        building.setTotalNeeded(value)
    elif index == 6:
        building.setTeam(value)
    return building
