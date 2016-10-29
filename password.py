user_input = input("Please enter password: ")
password = "changeme"
count = 1
while user_input != password:
    user_input = input("Please try again. Please enter password: ")
    count+=1
    if count >5:
        print("Access denied, please press enter to \
exit and contact security to reset your password")
        print("You have tried more than five times.")
        quit()
    elif user_input == password:
        print("Accepted")
        print("You have tried", count, "times.")
