import os
import json

print("*******************")
print("Welcome to Flexisaf")
print("*******************\n")

#This is the function that validates user input.
def profile(first_name, last_name, age, nationality, education):
    if not (first_name.isalpha() and last_name.isalpha()):
        print("\nEnter a valid name.")
        return False
    
    elif not ( 18<= age <= 45):
        print("\nAge out of range, you must be between 18 and 45 years old to register.")
        return False

    elif nationality not in ["nigerian", "south african", "european", "american"]:
        print("\nEnter a valid nationality.")
        return False

    elif education not in ["b.sc", "m.sc", "intern", "graduate intern"]:
        print("\nEnter a valid education level\n.")
        return False
    return True

is_running = True
print("Please Create Your Profile")


# This is the loop that runs as long as is running is true. Its prompts the user to enter their information.
while is_running:
    print("Note: Our services are available in Nigeria, South Africa, London and USA\n")

    print("***********************************************************")
    print("                     Profile                               ")
    print("***********************************************************")

    # This gets user input and validates it using the profile function.
    try:
        
        first_name = input("First name: \n")
        last_name = input("Last name: \n")
        age = int(input ("Age 18-45: \n"))
        nationality =  input("Nationality: \n").lower()
        education =  input ("Education (B.sc, M.sc, Intern or Graduate Intern): \n").lower()

    except ValueError:
        print("\ninvalid input.\nPlease enter the correct information\n")
        continue

    result =  profile(first_name, last_name, age, nationality, education )

    # This confirms with the user if they are okay with the information and if yes their information is saved.
    # if no they are prompted to enter their information again and if the validation of input data fails they are promted to enter their details.  
    if result == True:
        if input("Do you want to save your profile (Yes/No)?").lower() == "yes":
            print("\n**************************")
            print("Profile saved successfully")   
            print("**************************\n")
            is_running = False

            # This converts the profile_data into a dictionary which is a json file format.
            profile_data = {
                            "First_name": first_name, 
                            "Last_name": last_name, 
                            "Age": age, 
                            "Nationality": nationality, 
                            "Education": education
                    }
            #This makes sure the summary file is saved in the same directory as the main.py file, for easy sharing and access.
            folder = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(folder, "profile.json")

            # This writes the json file
            with open(path, "w") as f:
                json.dump(profile_data, f, indent=4)

            # this reads the json file and prints the profile summary to the user.
            with open(path, "r") as f:
                users_file = json.load(f)

            print("Here is your profile summary")
            print("-------------------------\n")
            for key, value in users_file.items():
                print(f"{key}: {value}")
        else:
            print("********************************")
            print("Please re-enter your information\n")
    else:
        print("ValidationError: Please enter the correct information.\n")




