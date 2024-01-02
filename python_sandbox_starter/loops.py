# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["jun","karl","andrew", "will"]

for person in people:
    print(f'Current Person {person}')

# While loops execute a set of statements as long as a condition is true.
count =0
while count <= 10:
    print(f'count {count}')
    count += 1

#range
for i in range(len(people)):
    print(people[i])