from faker import Faker
import names
import random
import time
from datetime import datetime, date


##Global Variables
fake = Faker()
customer_id = 100000
address_id = 200000

## State + Capital
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

def main():
    iteration = 10

    ##Open all Files
    file_customer = open("DataFiles/Customer.txt", "a")
    file_address = open("DataFiles/Address.txt", "a")

    ##create DataSets
    iterationCustomer = iteration
    while iterationCustomer > 0:
        customer = create_customer()
        file_customer.write(customer)
        iterationCustomer = iterationCustomer - 1

    iterationAddress = iteration
    while iterationAddress > 0:
        address = create_address()
        file_address.write(address)
        iterationAddress = iterationAddress - 1



    ##close files
    file_customer.close()
    file_address.close()

def create_customer():
    global customer_id
    customer = ""
    ## create ID
    customer = customer + str(customer_id)

    ## create gender and first name
    genderSwitch = random.choice([True, False])
    if genderSwitch == True:
        customer = customer  + ";" + "male"
        firstName = names.get_first_name("male")
        customer = customer + ";" + firstName
    else:
        customer = customer + ";" + "female"
        firstName = names.get_first_name("female")
        customer = customer + ";" + firstName

    ##create last name
    lastName = names.get_last_name()
    customer = customer + ";" + lastName

    ##create dob
    birthday = randomDate("1/1/1950", "1/1/2000", random.random())
    customer = customer + ";" + str(birthday)

    dob = datetime.strptime(birthday, "%d/%m/%Y")
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    customer = customer + ";" + str(age)

    customer_id = customer_id + 1
    customer = customer + "\n"
    return customer

def create_address():
    global address_id
    address = ""
    address = address + str(address_id)

    state = random.choice(capitals.keys())#
    city = capitals[state]

    file_streets = open("DataFiles/washington-dc.osm.streets.txt", "r")

    address = address + ";" + state + ";" + city

    address_id = address_id + 1
    address = address + "\n"
    return address


##time builder for dob
def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))
def randomDate(start, end, prop):
    return strTimeProp(start, end, "%d/%m/%Y", prop)





##call main
main()