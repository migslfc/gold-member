

first_name = "David"
last_name = "Joliceur"

print(first_name+" "+last_name)

#%%%%

first_name = "Harvey"
surname = "Elliott"

print("My first name is {}. My family name is {}".format(first_name, surname))


#%%%%%


firstname = "Luis"
surname = "Diaz"

print(f"My first name is {firstname}. My family name is {surname}")


#%%

my_int = 718
sentence = " keeps me marvelous."

print(str(my_int) + sentence)

#%%%%

user = {"first_name": "Kelvin"}
print(user["first_name"])
user["family_name"] = "Mercer"
print(user)
user["family_name"] = "Mason"
print(user)
del user["family_name"]
print(user)


#%%%%%


fruit = ["guanabana","mamey","guayaba"]
print(fruit[1])

len(fruit)

print(fruit[-2])

print(fruit[-1])

fruit.append("lulo")
print(fruit)

fruit.insert(2, "maracuya")
print(fruit)

print(sorted(fruit))
print(fruit)

fruit.sort()
print(fruit)

fruit.reverse()
print(fruit)

del fruit[1]
print(fruit)

favorite_fruit = fruit.pop()
print(favorite_fruit)

fresh_fruit = fruit.pop(1)
print(fresh_fruit)

fruit.remove('maracuya')
print(fruit)


