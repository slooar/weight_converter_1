print("""\
____    __    ____  _______  __    _______  __    __  .___________.     _______  _______ .__   __.  _______ .______          ___   .___________.  ______   .______      
\   \  /  \  /   / |   ____||  |  /  _____||  |  |  | |           |    /  _____||   ____||  \ |  | |   ____||   _  \        /   \  |           | /  __  \  |   _  \     
 \   \/    \/   /  |  |__   |  | |  |  __  |  |__|  | `---|  |----`   |  |  __  |  |__   |   \|  | |  |__   |  |_)  |      /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
  \            /   |   __|  |  | |  | |_ | |   __   |     |  |        |  | |_ | |   __|  |  . `  | |   __|  |      /      /  /_\  \    |  |     |  |  |  | |      /     
   \    /\    /    |  |____ |  | |  |__| | |  |  |  |     |  |        |  |__| | |  |____ |  |\   | |  |____ |  |\  \----./  _____  \   |  |     |  `--'  | |  |\  \----.
    \__/  \__/     |_______||__|  \______| |__|  |__|     |__|         \______| |_______||__| \__| |_______|| _| `._____/__/     \__\  |__|      \______/  | _| `._____
""")

class WeightConverter:
    current_weight = None
    current_weight_type = None
    
    
    def __init__(self, conversion_factor=2.20462):
        self.conversion_factor = conversion_factor
    
    def weight_type_converter(self):
        print("Welcome to the weight generator!")
        while True:
             weight = input("Please enter your current weight in numbers: ")
             if weight.isdigit():
                 weight = int(weight)
                 break
             else:
                 while True:
                    weight = input("Invalid input please input a valid number: ")
                    if weight.isdigit():
                        weight = int(weight)
                        break
                 break
        while True:
            weight_type = input("Is this weight in kgs or lbs?: ").lower()
            if weight_type == "kgs" or weight_type == "lbs":
                break
            else:
                while True:
                    weight_type = input("Invalid input. Please enter either kgs or lbs: ")
                    if weight_type == "kgs" or weight_type == "lbs":
                        break
                break
                            
        while True:
            if weight_type == "kgs":
                conversion_choice = input("Would you like to convert to lbs? y or n: ").lower()
                if conversion_choice == "y":
                    weight *= self.conversion_factor
                    weight_type = "lbs"
                    print("Your weight is {0} in {1}".format(weight, weight_type))
                    break
                elif conversion_choice == "n":
                    print("Your weight is {0} in {1}".format(weight, weight_type))
                    break
                else:
                    while True:
                        conversion_choice = input("Invalid input Please press y or n: ")
                        if conversion_choice.lower() in ["y", "n"]:
                            break
                    if conversion_choice == "y":
                        weight *= self.conversion_factor
                        weight_type = "lbs"
                        print("Your weight is {0} in {1}".format(weight, weight_type))
                        break
                    elif conversion_choice == "n":
                        print("Your weight is {0} in {1}".format(weight, weight_type))
                        break
 
            elif weight_type == "lbs":
                conversion_choice = input("Would you like to convert to kgs? y or n: ").lower()
                if conversion_choice == "y":
                    weight /= self.conversion_factor
                    weight_type = "kgs"
                    print("Your weight is {0} in {1}".format(weight, weight_type))
                    break
                elif conversion_choice == "n":
                    print("Your weight is {0} in {1}".format(weight, weight_type))
                    break
                else:
                    print("Invalid input Please press y or n: ")
                    continue
        self.current_weight = weight
        self.current_weight_type = weight_type

 # CALLING WEIGHT_CONVERTER FUNCTION
    
weight_converter = WeightConverter()
weight_converter.weight_type_converter()
    

class Bmi_calculator:
    def __init__(self, height_conversion=2):
        self.height_conversion = height_conversion
        
    def open_bmi_calculator(self):
        while True:
            open_bmi = input("Would you like to open the BMI calculater? y or n: ").lower()
            if open_bmi == "y":
                print("""\
            
.______   .________.  __        _____     ___       __        ______  ___   __   __          ___   .___________.  ______   .______                      
|   _  \  |   \/   | |  |     /      |   /   \     |  |      /      ||  |  |  | |  |        /   \  |           | /  __  \  |   _  \       _     _   
|  |_)  | |  \  /  | |  |    |  ,----'  /  ^  \    |  |     |  ,----'|  |  |  | |  |       /  ^  \ `---|  |----`|  |  |  | |  |_)  |    _| |_ _| |_ 
|   _  <  |  |\/|  | |  |    |  |      /  /_\  \   |  |     |  |     |  |  |  | |  |      /  /_\  \    |  |     |  |  |  | |      /    |_   _|_   _|
|  |_)  | |  |  |  | |  |    |  `----./  _____  \  |  `----.|  `----.|  `--'  | |  `----./  _____  \   |  |     |  `--'  | |  |\  \----. |_|   |_|  
|______/  |__|  |__| |__|     \______/__/     \__\ |_______| \______| \______/  |_______/__/     \__\  |__|      \______/  | _| `._____|            
                                                                                                                                                       
""")
                self.calculate_bmi()
                break
            elif open_bmi == "n":
                print("Thankyou for using weight converter")
                break
            else:
                print("Invalid input please type y or n and press enter: ") 
    
    # BMI CALCULATOR
    
    def calculate_bmi(self):
        print("Okay lets calculate your bmi")
        #TAKES IN WEIGHT IN NUMBERS
        while True:
            weight = input("Please enter your weight in numbers: ")
            if weight.isdigit():
                weight = int(weight)
                break
            else:
                print("Invalid input!: ")
        # TAKES IN WEIGHT TYPE KGS OR LBS AND CONVERTS TO LBS IF NESSECARY 
        while True:        
            weight_type = input("Is this in lbs or kgs?: ")
            if weight_type == "lbs":
                weight = weight
                break
            elif weight_type == "kgs":
                weight *= 2.2
                break
            else: print("invalid input please enter either 'kgs' or 'lbs': ")
        #TAKES IN HEIGHT IN FEET AND INCHES
        print("ok now we need you to enter your height. Feet first and then inches:")
        while True:
            height_in_feet = input("please enter your height in feet(without inches): ")
            if height_in_feet.isdigit():
                height_in_feet = int(height_in_feet) * 12
                break
            else:
                print("Invalid input!: ")
        while True:
            height_in_inches = input("Now enter your inches: ")
            if height_in_inches.isdigit():
                height_in_inches = int(height_in_inches)
                height_inches_total = height_in_inches + height_in_feet
                break
            else:
                print("Invalid input!: ")
        #DOES MATH TO CALCULATE BMI
        bmi = (weight / (height_inches_total ** 2)) * 703
        print("Your bmi is {0}".format(bmi))
        if bmi >= 30:
            print("You are Obese")
        elif bmi < 29.9 and bmi >= 25:
            print("You are not Obese but are overweight")
        elif bmi < 24.9 and bmi >= 18.5:
            print("You are at a healthy weight")
        else:
            print("You are underweight")


        
    
                
        
        
        

                
        














bmi_calculator = Bmi_calculator()
bmi_calculator.open_bmi_calculator()











            

        
        

    
        
        


        
        



