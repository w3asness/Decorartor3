from abc import ABC, abstractmetod

class Beverage(ABC) :
   _description: str

def _init_(self) -> None :
      self._description = 'Unknown Beverage'

def getDescription(self) -> str:
       return self._description

@abstractmetod
def cost(self) -> float:
           pass