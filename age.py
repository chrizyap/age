# Get the current year from the user
current_year = int(input("What year is it?:"))
# Get the date of birth of the user
year_of_birth = int(input("What year were you born?:"))
# Calulate the age of the user
age = current_year - year_of_birth
# convert this number (int) to a word (string)
agestr = str(age)
# print the age of the user
print("You are " + agestr + "years old")
