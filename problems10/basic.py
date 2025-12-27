#Question 1 : Age group categorization 

# age=input("Give a age: ")
# ageInInt=int(age)


# if ageInInt<13 :
#     print("Child")
# elif ageInInt<20:
#     print("Teenager")
# elif ageInInt<60:
#     print("Adults")
# else:
#     print("Senior ☠️")

#Question 2 if age is above 18 ticket is 12 $ and 8 $ below 18 and 2$ discount on every wednesday
# day='Wednesday'
# age=int(input("Enter age "))
# if age>=18 :
#     if day == "Wednesday":
#         print("Ticket = 10")
#     else:
#         print("Ticket = 12")
# else:
#     if day=="Wednesday":
#         print("Ticket = 6")
#     else:
#         print("Ticket = 8")
# SOLUTION 2
# age=21
# day="Wednesday"
# price=12 if age>=18 else 8
# if day == "Wednesday":
#     price-=2
# print("Ticket Price is $",price)

# Question 3 assign grades A(90-100),B(80-89),C(70-79),D(60-69),F(below 60)

# score=int(input("Enter the marks "))
# if score>=101:
#     print("Verify your grade again")
# elif score>89:
#     print("Grade A")
# elif score>79:
#     print("Grade B")
# elif score>69:
#     print("Grade C")
# elif score>59:
#     print("Grade D")
# else:
#     print("Grade F")


#Question 4 determine if a fruit is ripe , overripe , or unripe based on its color eg(Banana:Green - Unripe,Yellow -Ripe , Brown -Overripe)

# fruit="Banana"
# color="Yellow"

# if fruit =="Banana":
#     if color=='Yellow':
#         print('Ripe')
#     if color=='Green':
#         print("Unripe")
#     if color=='Brown':
#         print("OVerripe")
# else:
#     print("Data not available")

#Question 5 Suggest activity on the basis of weather Sunny: Go for walk, Rainy: Read a book , Snowy : Build a snowman
# weather="Sunny"
# if weather =="Sunny":
#     print("Go for a Walk")
# elif weather =="Rainy":
#     print("Read a Book")
# elif weather =="Snowy":
#     print("Build a snowman")
# else:
#     print("Study")

#Question 6 Choose mode of transport based on distance <3 walk,3-15 bike,15+ car
# distance=int(input("Enter Distance "))
# if distance<=3:
#     mode="Walk"
# elif distance<=15 :
#     mode="Bike"
# else:
#     mode="Car"
# print(mode)

#Question 7 Coffee customization Small , Medium, Large with option of extra shot of espresso
# order_size="Medium"
# extra_shot=False

# if extra_shot:
#     coffee=order_size+' coffee with extra shot'
# else:
#     coffee=order_size+' coffee'
# print("Order: ",coffee)

#Question 8 if password is "Weak", "Medium","Strong" Criteria <6 weak , 6-10 medium , >10 strong
# password="1234567037434"
#passlen=len(password)
# if len(passlen)<6:
#     strength="Weak"
# elif len(passlen)<=10:
#     strength = "Medium"
# else:
#     strength="Strong"
    
# print("Password is ",strength)

#Question 9 Determine if leap year (dividble by 4 but not by 100 unless dividlbe by 400)
# year=2024
# if (year%400 == 0)or(year%4==0 and year % 100 !=0):
#     print("Year is Leap",year)
# else:
#     print("Not Leap Year", year)

#Question 10 Pet Food Recomendation based on pets species eg Dog <2 _ Puppy Food,Cat  >5 Senior cat food
# pet="Cat"
# age=6
# if pet=="Dog":
#     if age<3:
#         print("Adult Dog Food")
#     else:
#         print("Puppy Food")
# elif pet=="Cat":
#     if age>=5:
#         print("Senior Cat Food")
#     else:
#         print("Junior Cat Food")
# else:
#     print("Food Data not available for pet ",pet ,"of age ",age)


