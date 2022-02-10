from abc import ABC, abstractmetod
from Beverage import Beverage

class CondimentDecorator(Beverage, ABC) :
    @abstractmetod
    def getDescriprion(self) -> str:
        return self._description