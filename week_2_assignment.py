# Question 1
my_list = []

# Question 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Question 3
my_list.insert(1,15)
print(my_list)

# Question 4
my_list.extend([50,60,70])
print(my_list)

# Question 5
my_list.pop()
print(my_list)

# Question 6
my_list.sort()
print(my_list)

# Question 7
index = 0
while True:
    if (my_list[index] == 30):
        print(index)
        break
    else:
        index += 1
