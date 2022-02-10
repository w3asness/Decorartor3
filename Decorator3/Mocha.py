from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Mocha(CondimentDecorator):
    beverage: Beverage
    
    def _init_(self, b: Beverage) -> None:
         self.beverage = basestring
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Mocha' 

    def cost(self) -> float:
        return self.beverage.cost() + 20    