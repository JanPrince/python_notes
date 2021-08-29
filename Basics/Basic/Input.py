# An interactive program takes input from the user

User_Name = input("Enter your name : ")    # when the user inputs the name, it is stored in the variable User_Name
# NB: Whatever input is given is taken as a string by python
# therefore to work with numbers,
User_age = int(input("Enter your age: "))    # any input is casted into integer ; therefore gives an error for strings
user_balance = float(input("Enter amount: "))   # input is casted into floats ;

print("my name is" , User_Name , ". I am" ,User_age, "years old\n I have", user_balance , "in my bank account")

user_fun = input("Type anything: ")
print(5* user_fun)