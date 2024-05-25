#Abstraction in python
from abc import ABC,abstractmethod
class Game(ABC):
    @abstractmethod
    def play(self):
        pass
class Cricket(Game):
    def play(self):
        print('player is palying cricket game')
class FootBall(Game):
    def play(self):
        print('palyeer is playying football')
