people = {}
def create(name,age):
    
    people[name] = age

def average():
    if people:
        total = sum(people.values())
        avg = total/len(people)
        return total,avg
    return False
def print_it():
    if people:
        for key,value in people.items():
            print(f"{key} is {value} years old")



create('ali',38)
create('kali',34)
create('hari',38)

print(average())

print_it() 

