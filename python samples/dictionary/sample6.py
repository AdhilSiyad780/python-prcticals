def changer(alpla):
    result  = {}
    for name,age,place in alpla:
        result[name] = {'age':age,'place':place} 
    return result

people = [
    ('John', 25, 'New York'),
    ('Alice', 30, 'Los Angeles'),
    ('Bob', 22, 'Chicago')
]

print(changer(people))