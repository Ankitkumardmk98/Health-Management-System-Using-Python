# health management system
try:
    def gtd():
        import datetime
        return datetime.datetime.now()

    User_name = input("Enter User Name:\n") #Takes user name
    def user(usr):
        Inspect_or_Append = int(input("Enter 1 for inspect, and 2 for append\n"))
    
        if Inspect_or_Append == 1: #This mean inspection
            Food_or_Exercise = int(input("Enter 1 for food, and 2 for exercise\n"))
        
            if Food_or_Exercise == 1:
                with open(f"{usr}_food.txt") as usar_food:
                    print(usar_food.read())
                    usar_food.close()
        
            elif Food_or_Exercise == 2:
                with open(f"{usr}_exercise.txt") as usar_exercise:
                    print(usar_exercise.read())
                    usar_exercise.close()
            else:
                print("Please give the right value to inspect {for food-1 and for exercise-2")
            
        elif Inspect_or_Append == 2:  #this mean appending
            Food_or_Exercise = int(input("Enter 1 for food, and 2 for exercise\n"))
        
            if Food_or_Exercise == 1:
                food = input("Enter food name:\n")
                with open(f"{usr}_food.txt", "a") as usar_food:
                    usar_food.write(f"{gtd()} = {food} \n")
                    usar_food.close()
        
            elif Food_or_Exercise == 2:
                exercise = input("Enter exercise name:\n")
                with open(f"{usr}_exercise.txt", "a") as usar_exercise:
                    usar_exercise.write(f"{gtd()} = {exercise} \n")
                    usar_exercise.close()
            else:
                print("Please give the right value to append {for food-1 and for exercise-2")
            
        else:
            print("Please give the right value {for inspection-1 and for appending-2")
       
    user(User_name)

except Exception:
    print("An Error occured, no file found")






# # health management system
# def gtd():
#     import datetime
#     return datetime.datetime.now()

# User_name = input("Enter User Name:\n") #Takes user name
# def user(usr):
#     Inspect_or_Append = int(input("Enter 1 for inspect, and 2 for append\n"))
    
#     if Inspect_or_Append == 1: #This mean inspection
#         Food_or_Exercise = int(input("Enter 1 for food, and 2 for exercise\n"))
        
#         if Food_or_Exercise == 1:
#             with open(f"{usr}_food.txt") as usar_food:
#                 print(usar_food.read())
#                 usar_food.close()
        
#         elif Food_or_Exercise == 2:
#             with open(f"{usr}_exercise.txt") as usar_exercise:
#                 print(usar_exercise.read())
#                 usar_exercise.close()
#         else:
#             print("error")
            
#     elif Inspect_or_Append == 2:  #this mean appending
#         Food_or_Exercise = int(input("Enter 1 for food, and 2 for exercise\n"))
        
#         if Food_or_Exercise == 1:
#             food = input("Enter food name:\n")
#             with open(f"{usr}_food.txt", "a") as usar_food:
#                 usar_food.write(f"{gtd()} = {food} \n")
#                 usar_food.close()
        
#         elif Food_or_Exercise == 2:
#             exercise = input("Enter exercise name:\n")
#             with open(f"{usr}_exercise.txt", "a") as usar_exercise:
#                 usar_exercise.write(f"{gtd()} = {exercise} \n")
#                 usar_exercise.close()
#         else:
#             print("error")
            
#     else:
#         print("sry")
       
# user(User_name)