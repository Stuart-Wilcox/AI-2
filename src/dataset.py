import csv
from passenger import Passenger

class Dataset:
    def __init__(self, useTest=False):
        self.useTest = useTest

        self.testPath = '../data/test.csv'
        self.trainPath = '../data/train.csv'

    def getPassengers(self):
        filename = self.testPath if self.useTest else self.trainPath

        passengers = []
        with open(filename, 'r', newline='\n') as file:
            reader = csv.reader(file)

            for row in reader:
                cells = row
                if len(cells) != 12:
                    raise Exception('Fields missing in dataset!')

                passengerId, survived, pClass, name, sex, age, sibSp, parch, ticket, fare, cabin, embarked = cells

                passenger = Passenger(passengerId, survived, pClass, name, sex, age, sibSp, parch, ticket, fare, cabin, embarked)
                passengers.append(passenger)

        return passengers
