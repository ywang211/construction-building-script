#!/usr/bin/python3


class buildingFloorEntry:
  def __init__(self, name='N/A', floor=0, material='N/A', budget=0, current_stock=0, total_needed=0, team='N/A'):
    self.name = name
    self.floor = floor
    self.material = material
    self.budget = budget
    self.current_stock = current_stock
    self.total_needed = total_needed
    self.team = team
  def getNeedAmount(self):
  	return self.total_needed - self.current_stock
  def setName(self, name):
  	self.name = name
  def setFloor(self, floor):
  	self.floor = floor
  def setMaterial(self, material):
  	self.material = material
  def setBudget(self, budget):
  	self.budget = budget
  def setCurrentStock(self, current_stock):
  	self.current_stock = current_stock
  def setTotalNeeded(self, total_needed):
  	self.total_needed = total_needed
  def setTeam(self, team):
    self.team = team
