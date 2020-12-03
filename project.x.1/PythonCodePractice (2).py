ff = 9
name = "Rolf"
print(name)
a = 25
b = a
print(a)
print(b)

b= 17
print(a)
print(b)

a = "Bolbol"
b = "Bolbol"
print(a)
print(b)

a = 4
b = 6
print(a)
print(b)
print(a*b)

greating = "Hellooooooo "
print(greating +" " + name)

greating2 = f"Hellooo0000002, {name}"
print(greating2)

name3 = "Cotomoto"
greating3 = "Hellllooooooo3, {}"
with_whatever = greating3.format(name3)
print(greating3)

longer_phrase = "helloo, {} ... How are {}"
combined = longer_phrase.format(name3, name)
print(combined)

# in_square_feet = input("Enter: ")
# square_feet = int(in_square_feet)
# squar_meter = square_feet/10.5
# print(f"{square_feet} Sqaure feet is aproximate to -> {squar_meter:.3f} Square meter")

# age_years = int(input("Enter: "))
# age_months = age_years*12
# print(f"{age_years} years old is -> {age_months:.3f} months")

l = ["Kee", "Tee", "Mee"]
t = ("Keet", "Teet", "Meet")
s = {"Kees", "Tees", "Mees"}

print(l)
print(t)
print(s)


friends = {"William", "Ralf", "Robin", "Kriss"}
Locals = {"William Loc", "Ralf Loc", "Robin", "Kriss"} 

unionFriends = friends.union(Locals)
print(unionFriends)

differenceFriends = friends.difference(Locals)
print(differenceFriends)

differenceFriendsvise = Locals.difference(friends)
print(differenceFriendsvise)

intersectionFriends = friends.intersection(Locals)

intersectionFriendsvise = Locals.intersection(friends)

print(intersectionFriends )
print( intersectionFriendsvise)

my_list = [1 ,80, 19]
my_tuble = (15)
set1 = {8, 12, 66, 56, 77, 5, 24}
set2 = {5, 88, 45, 11, 62, 9, 77, 12}

total=0
for e in range(0, len(my_list)): 
    total = total + my_list[e]

print(total)

total2 = sum(my_list)
print(total2)

def sumOfList(my_list, size): 
   if (size == 0): 
     return 0
   else: 
     return my_list[size - 1] + sumOfList(my_list, size - 1) 
   
# Driver code      
total3 = sumOfList(my_list, len(my_list)) 
  
print("Sum of all elements in given list: ", total3) 

print(set1.intersection(set2))

goodFriends = ["Ahmed", "Walid", "Ramy"]
myFriends = ["Ahmed", "Ramy", "Walid"]
print(myFriends.sort == goodFriends.sort)
print(myFriends.sort is goodFriends.sort)

goodFriends1 = ["Ahmed", "Walid", "Ramy"]
myFriends1 = ["Ahmed", "Walid", "Ramy"]
print(myFriends1 == goodFriends1)
print(myFriends1 is goodFriends1)

x = 5
y = 5
print(x is y)

# day_one = input("Enter day: ")
# if day_one == "Monday":
#     print("Moday is a good start " + day_one)
# elif day_one == "Tusday":
#     print("Happy weekend " + day_one)
# else:
#     print("Have a gooood day " + day_one)

print(   f"{'Ahmed' in goodFriends} How are you") 