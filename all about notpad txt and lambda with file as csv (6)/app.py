"""
    names = []
for _ in range(3): 
    name = input('Enter your name: ')
    names.append(name)
for name in names:
    print(f'hello, {name}')
    L6 00:04:30
"""




"""
name = input('Whats your name? ')

file = open('name.txt', 'a')
file.write(f'{name}\n')
file.close()
L6 00:14:00
"""




"""
name = input('Whats your name? ')
with open('name.txt', "a") as file:
    file.write(f"{name}\n")
    L6 00:15:44
"""



"""
with open('name.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    print(f'hello, {line}', line.rstrip)
    L6 00:20:00
"""



"""with open('name.txt', 'r') as file:
    for line in file:
        print('hello,', line.rstrip())
        L6 00:20:00
        """
        
        
        
        
"""names = []

with open('name.txt') as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f'hello, {name}')
    L6 00:23:00"""
    
  
  
    
"""with open('name.txt') as file:
    for line in sorted(file):
        print('hello,', line.rstrip())"""
        
        
        
"""with open('name.csv') as file:
    for line in file:
        row = line.rstrip().split(',')
        print(f'{row[0]} lives in {row[1]}')
        L6 00:36:00"""
        
        
        
        
"""with open('name.csv') as file:
    for line in file:
        name, place = line.rstrip().split(',')
        print(f'{name} lives in {place}')
        L6 00:39:43
        """
        
        
        
        
"""names = []

with open('name.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        names.append(f'{name} lives in {house}')
        
for name in sorted(names):
    print(name)
    L6 00:41:30
    """
    
    
    
    
"""students = []

with open('name.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        
        student = {'name': name, 'house': house}
        students.append(student)
        
def get_name(student):
    return student['name']
        
for student in sorted(students, key=get_name):
    print(f"{student['name']} lives in {student['house']}")
    L6 00:45:57
    """
    
    
    

"""
students = []

with open('name.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        
        student = {'name': name, 'house': house}
        students.append(student)
        
for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} lives in {student['house']}")
    L6 00:56:52
    """
    
    
"""import csv
    
students = []

with open('name2.csv') as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['home']}")
    L6 01:02:50
    """
    
    
    
"""students = []

with open('name2.csv') as file:
    for line in file:
        name, home = line.split(',', 1)
        students.append({"name": name, "home": home.strip()})
    for student in sorted(students, key=lambda student: student['name']):
        print(f"{student['name']} is from {student['home']}")
        خودم نوشتم
        """
        
        
        


"""import csv
    
students = []

with open('name2.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['home']}")
    L6 1:08:30
    """
    
    



"""import csv 

name = input("Enter your name: ")
home = input("Enter your home: ")

with open('name2.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name,home])
    L6 01:14:45"""
   
   
   
   
   
   
"""import csv 

name = input("Enter your name: ")
home = input("Enter your home: ")

with open('name2.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({'name': name, 'home': home})
    # L6 01:14:45"""