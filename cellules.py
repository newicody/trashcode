import argparse
from myplanet import MyPlanet

class Cellules(MyPlanet):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Selection de l\'activite")
        self.parser.add_argument('--clone', action=self.select, nargs='0', help='clone le ')
        self.parser.add_argument('--put1', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
        self.parser.add_argument('--geto', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
        self.parser.add_argument('--status', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

    def select(self, act):
        if act. == ""

start = Cellules()
start.parser.parse_args()
print(start.args.accumulate(start.args.integers))
