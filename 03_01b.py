from collections import namedtuple

def can_take_order (driver, nb_pack):
    return driver.car_capacity >= nb_pack

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    driver = namedtuple('driver',['name', 'car_type', 'car_capacity'])
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    d1 = driver("Iris", "Prius", 7)
    d2 = driver("Marc", "C4", 15)
    d3 = driver("Paul", "Transporter", 26)
    #check if they can take a certain order, given their car's capacity.
    print(can_take_order(d3,20))
    return

if __name__ == "__main__":
    main()