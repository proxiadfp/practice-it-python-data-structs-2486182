from csv import reader
from collections import namedtuple
def main():
    #add code here
    #read data/Customer.csv
    with open('data/Customer.csv', mode='r') as file:
        csv_reader = reader(file)
        Person = namedtuple("Person", next(csv_reader))
        for line in csv_reader :
            person =Person(*line)
            print (person)
    #Create workable objects with each line
    return

if __name__ == "__main__":
    main()