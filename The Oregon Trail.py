import os
import random

os.system("title The Oregon Trail")

# A class that has info about the character you play so you can get started.
class main_character:
    def __init__(self, profession1, skill_sets, start_money, difficulty):
        self.profession = profession1
        self.skill_sets = skill_sets
        self.start_money = start_money
        self.difficulty = difficulty

# A class that has the state of health of each person in the wagon with you.
class wagon_passengers_health_state:
    def __init__(self, healthy_wife, healthy_mary, healthy_billy, injured_wife, injured_mary, injured_billy, diseases_wife, diseases_mary, diseases_billy, dead_wife, dead_mary, dead_billy):
        # Healthy
        self.healthy_wife = healthy_wife # Wife
        self.healthy_mary = healthy_mary# Little Mary
        self.healthy_billy = healthy_billy # Little Billy

        # Injured
        self.injured_wife = injured_wife # Wife
        self.injured_mary = injured_mary # Little Mary
        self.injured_billy = injured_billy # Little Billy

        # Has diseases
        self.diseases_wife = diseases_wife # Wife
        self.diseases_mary = diseases_mary # Little Mary
        self.diseases_billy = diseases_billy # Little Billy

        # Dead
        self.dead_wife = dead_wife # Wife
        self.dead_mary = dead_mary # Little Mary
        self.dead_billy = dead_billy # Little Billy

# A class that helps with stats to help you with traveling to know if you should make desperate changes.
class travel_stats:
    def __init__(self, pace, rations, distance_left, in_problem):
        self.pace = pace
        self.rations = rations
        self.distance_left = distance_left
        self.in_problem = in_problem
# A class that shows information on what items you have and how much. 
class supplies:
    def __init__(self, oxen, sets_of_clothing, ammunition, wagon_wheels, wagon_axles, wagon_tongues, pounds_of_food, money_left):
        self.oxen = oxen
        self.sets_of_clothing = sets_of_clothing
        self.ammunition = ammunition
        self.wagon_wheels = wagon_wheels
        self.wagon_axles = wagon_axles
        self.wagon_tongues = wagon_tongues
        self.pounds_of_food = pounds_of_food
        self.money_left = money_left

# A class to help know if the main character is near a traveler to trade with or a shop to buy items with. If so it will give a shop option.
# Otherwise it will just say there is none nearby. 
class travel_occurances:
    def __init__(self, traveler_nearby, forest_nearby, shop_nearby, broken_wagon_wheels, broken_wagon_axles, broken_wagon_tongues, injured_ox):
        self.traveler_nearby = traveler_nearby
        self.shop_nearby = shop_nearby
        self.broken_wagon_wheels = broken_wagon_wheels
        self.broken_wagon_axles = broken_wagon_axles
        self.broken_wagon_tongues = broken_wagon_tongues
        self.injured_ox = injured_ox
        self.forest_nearby = forest_nearby


wagon_passengers_health_state = wagon_passengers_health_state(healthy_wife=True, healthy_mary=True, healthy_billy=True, injured_wife=False, injured_mary=False, injured_billy=False, diseases_wife="none", diseases_mary="none", diseases_billy="none", dead_wife=False, dead_mary=False, dead_billy=False)
main_character = main_character(profession1="none", skill_sets="none", start_money=0, difficulty="none")
travel_stats = travel_stats(pace="steady", rations="filling", distance_left=2000, in_problem=False)
supplies = supplies(oxen=1, sets_of_clothing=0, ammunition=0, wagon_wheels=0, wagon_axles=0, wagon_tongues=0, pounds_of_food=500, money_left="unkown")
travel_occurances = travel_occurances(traveler_nearby=False, forest_nearby=False, shop_nearby=False, broken_wagon_wheels=False, broken_wagon_axles=False, broken_wagon_tongues=False, injured_ox=False)

def Start_Game():
    
    os.system("cls clear")

    game_running = True

    # While loop to keep the game running
    # Create random events that injure people, starvation, hunting, broke down wagon, and professions
    # That give different advantages.

    def Choose_Profession():
            os.system("cls clear")
            print("What do you want your profession to be?")
            profession_choice = input("Banker, Carpenter, or Farmer: ")

            if profession_choice.lower().strip() == "banker":
                main_character.profession = "Banker"
                main_character.skill_sets = "Lower trade costs and higher starting money"
                main_character.start_money = 1600
                main_character.difficulty = "Easy"
                travel_occurances.shop_nearby = True
                stats_question()
            elif profession_choice.lower().strip() == "carpenter":
                main_character.profession = "Carpenter"
                main_character.skill_sets = "Higher chance of successfully fixing something"
                main_character.start_money = 800
                main_character.difficulty = "Medium"
                travel_occurances.shop_nearby = True
                stats_question()
            elif profession_choice.lower().strip() == "farmer":
                main_character.profession = "Farmer"
                main_character.skill_sets = "Higher chance of killing a bigger animal while hunting"
                main_character.start_money = 400
                main_character.difficulty = "Hard"
                travel_occurances.shop_nearby = True
                stats_question()
            else:
                print("That isn't a profession! Please type something to try again!", end="\n\n")
                input()
                Choose_Profession()
    
    def stats_question():
        os.system("cls clear")
        
        print(f"Profession: {main_character.profession}\nSkill Sets: {main_character.skill_sets} \nStart Money: {main_character.start_money}\nDifficulty: {main_character.difficulty}")
       
        print("\nAre you happy with the given stats?")
       
        happy_stats_question = input("(Y / N): ")
        
        if happy_stats_question.lower().strip() == "y" or happy_stats_question.lower().strip() == "yes":
            run_game()
        elif happy_stats_question.lower().strip() == "n" or happy_stats_question.lower().strip() == "no":
            Choose_Profession()
        else:
            print("That answer wasn't understood.")
            print("Type something again to answer the question again.")
            input()
            stats_question()
    def run_game():
        os.system("cls clear")
        supplies.money_left = main_character.start_money
        
        while game_running:
            os.system("cls clear")
            # Quick Find #6
            print(f"Heatlh: Still a work in progress!\nPace: {travel_stats.pace}\nRations: {travel_stats.rations}\n\nYou may:\n\n\t1: Continue on trail\n\t2: Check Supplies\n\t3: Change Pace\n\t4: Change food rations\n\t5: Stop to rest\n\t6: Attempt to trade\n\t7: Buy Supplies\n")
            option_choice = input("What is your choice: ")

            if option_choice.strip() == "1":
                def start_traveling():
                    
                    # Showing stats to player
                    os.system("cls clear")
                    print(f"You have {travel_stats.distance_left} miles left")
                    print(f"Your pace: {travel_stats.pace}")
                    # Quick Find #6
                    print(f"Your Health: Needs work! ")
                    print(f"Your rations: {travel_stats.rations}", end="\n\n")
                    input("Type something to continue: ")

                    # Bad and Good event rolls
                    random_distance_roll = random.randint(10, 50)
                    good_roll = random.randint(1, 5)
                    nearby_events_roll = random.randint(1, 5)
                    bad_roll1 = random.randint(1, 10)


                    if good_roll == 1:
                        print("You found a traveler who is willing to sell some items to you!")
                        travel_occurances.traveler_nearby = True
                    
                    if nearby_events_roll == 1:
                        # This will be for coming to a nearby travler, or finding a forest to hunt in
                        
                        # Check if there's a chance that something is nearby | 1 in 5 chance
                        nearby = random.randint(1, 5)
                        
                        if nearby == 1:
                            # Choose wether it's a traveler or forest to hunt in
                            travelerForestRoll = random.randint(1, 2)
                            if travelerForestRoll == 1:
                                # Town
                                travel_occurances.traveler_nearby = True
                            else:
                                # Forest
                                travel_occurances.forest_nearby = True

                    if bad_roll1 == 1:
                        bad_roll2 = random.randint(1, 5)
                        
                        if bad_roll2 == 1:
                            # Injured Ox
                            # Quick Find #2
                            pass
                        
                        elif bad_roll2 == 2:
                            # Lose some food
                            lose_food_roll = random.randint(10, 30)
                            
                            print("You notice that some of the food went bad.")
                            print(f"You lose {lose_food_roll} pounds of food")

                            supplies.pounds_of_food -= lose_food_roll

                            input("Type something to continue: ")
                        
                        elif bad_roll2 == 3:
                            # Someone gets injured | If already injured, then catch disease
                            # Quick Find #7
                            injured_roll = random.randint(1, 3)

                        elif bad_roll2 == 4:
                            # Someone catches a disease | If already diseased, then die
                            # Quick Find #8
                            disease_roll = random.randint(1, 4)

                        elif bad_roll2 == 5:
                            # Wade across a river | Have a chance to sucessfully do it, or lose an item
                            # Quick Find #9
                            pass
                if travel_occurances.broken_wagon_wheels == False and travel_occurances.broken_wagon_axles == False and travel_occurances.broken_wagon_tongues == False and travel_occurances.injured_ox == False:
                    start_traveling()
                else:
                    # If a part of their wagon broke
                    # Quick Find #1
                    if travel_occurances.broken_wagon_wheels == True:
                        if supplies.wagon_wheels >= 1:
                            supplies.wagon_wheels -= 1
                            travel_occurances.broken_wagon_wheels = False
                            print("You replaced the broken wagon wheel and continue on your journey", end="\n\n")
                            input("Type something to continue: ")
                            start_traveling()
                        else:
                            new_traveler = random.randint(1, 2)
                            print("You don't have enough wagon wheels to continue.")
                            print("Keep trying until a traveler comes nearby!", end="\n\n")

                            if new_traveler == 1:
                                print("A travler comes nearby and greets you", end="\n\n")
                                travel_occurances.traveler_nearby = True
                            
                            else:
                                print("Keep trying until a new traveler comes!", end="\n\n")
                            
                            input("Type something to continue: ")
                    
                    elif travel_occurances.broken_wagon_axles == True:
                        if supplies.wagon_axles >= 1:
                            supplies.wagon_axles -= 1
                            travel_occurances.broken_wagon_axles = False
                            print("You replaced the broken wagon axle and continue on your journey", end="\n\n")
                            input("Type something to continue: ")
                            start_traveling()
                        else:
                            new_traveler = random.randint(1, 2)
                            print("You don't have enough wagon axles to continue.")
                            print("Keep trying until a traveler comes nearby!", end="\n\n")

                            if new_traveler == 1:
                                print("A travler comes nearby and greets you", end="\n\n")
                                travel_occurances.traveler_nearby = True
                            
                            else:
                                print("Keep trying until a new traveler comes!", end="\n\n")
                            
                            input("Type something to continue: ")
                    elif travel_occurances.broken_wagon_tongues == True:
                        if supplies.wagon_tongues >= 1:
                            supplies.wagon_tongues -= 1
                            travel_occurances.broken_wagon_tongues = False
                            print("You replaced the broken wagon tongue and continue on your journey", end="\n\n")
                            input("Type something to continue: ")
                            start_traveling()
                        else:
                            new_traveler = random.randint(1, 2)
                            print("You don't have enough wagon tongues to continue.")
                            print("Keep trying until a traveler comes nearby!", end="\n\n")

                            if new_traveler == 1:
                                print("A travler comes nearby and greets you", end="\n\n")
                                travel_occurances.traveler_nearby = True
                            
                            else:
                                print("Keep trying until a new traveler comes!", end="\n\n")
                            
                            input("Type something to continue: ")


            elif option_choice.strip() == "2":
                # Check Supplies: Check "Supplies.png" for more details
                os.system("cls clear")
                print(f"Oxen: {supplies.oxen}\nSets of clothing: {supplies.sets_of_clothing}\nBullets: {supplies.ammunition}\nWagon wheels: {supplies.wagon_wheels}\nWagon axles: {supplies.wagon_axles}\nWagon tongues: {supplies.wagon_tongues}\nPounds of food: {supplies.pounds_of_food}\nMoney left: {supplies.money_left}")
                input("Type something to continue: ")
            elif option_choice.strip() == "3":
                # Change Pace: Check "Change Pace Options.png" for more details"
                def change_pace_def():   
                    os.system("cls clear")
                    print("1: A steady pace\n2: A strenuous pace\n3: A grueling pace\n4: Find out what these different paces mean\n\n5: Exit")
                    change_pace = input("\nWhat is your choice: ")

                    if change_pace.strip() == "1":
                        travel_stats.pace = "steady"

                    elif change_pace.strip() == "2":
                        travel_stats.pace = "strenuous"

                    elif change_pace.strip() == "3":
                        travel_stats.pace = "grueling"

                    elif change_pace.strip() == "4":
                        os.system("cls clear")
                        print("Steady -- You travel about 8 hours a day, taking frequent rests. You take care not to get too tired.\n\nStrenuous -- You travel about 12 hours a day, starting just after sunrise and stopping shortly before sunset. you stop to rest only when necessary. You finish each day feeling very tired.\n\nGrueling -- You travel about 16 hours a day, starting before sunrise and continuing until dark. You almost never stop to rest. You do not get enough sleep at night. You finish each day feeling absolutely exhausted, and your health suffers.")
                        input("\nType something to continue: ")
                    
                    elif change_pace.strip() == "5":
                        # For exiting
                        pass
                    
                    else:
                        print("\nThat isn't a valid answer.")
                        input("Type something to continue: ")
                        change_pace_def()
                change_pace_def()

            elif option_choice.strip() == "4":
                # Change food rations: Check "Change Food Rations.png" for more details
                def change_food_rations_def():
                    os.system("cls clear")
                    print("The amount of food the people in your party eat each day can change. These amounts are:\n\n\t1. filling - meals are large and generous.\n\n\t2. meager - meals are small, but adequate.\n\n\t3. bare bones - meals are very small; everyone stays hungry.")
                    food_rations_option = input("\nWhat is your choice: ")

                    if food_rations_option.lower().strip() == "filling" or food_rations_option.lower().strip() == "1":
                        travel_stats.rations = "filling"
                    elif food_rations_option.lower().strip() == "meager" or food_rations_option.lower().strip() == "2":
                        travel_stats.rations = "meager"
                    elif food_rations_option.lower().strip() == "bare bones" or food_rations_option.lower().strip() == "3":
                        travel_stats.rations = "bare bones"
                    else:
                        print("\nThat isn't a valid answer.")
                        input("Type something to continue: ")
                        change_food_rations_def()

                change_food_rations_def()
                        
                
            
            elif option_choice.strip() == "5":
                # Stop to rest: Check "Rest Options.png" for more details
                os.system("cls clear")
                print("Option 5")
            elif option_choice.strip() == "6":
                # Attempt to trade: Check "Attempt to Trade Options.png" for more details
                os.system("cls clear")
                if travel_occurances.traveler_nearby:
                    which_trade = random.randint(1, 7)
                    if main_character.profession != "Banker":
                        discount_roll = random.randint(1, 5)
                        if discount_roll == 1:
                            discount = True
                    
                    # If player is banker, then they get lower trade costs
                    elif main_character.profession == "Banker":
                        discount = True

                    if which_trade == 1:
                        # Money for ox
                        
                        os.system("cls clear")
                        if discount != True:
                            def buy_ox_traveler():
                                print("I will sell you an ox for 20.00 each", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 20 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_ox_traveler()
                                    elif int(how_many) * 20 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 20
                                        supplies.oxen += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False

                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_ox_traveler()

                            buy_ox_traveler()

                        elif discount:
                            def buy_ox_traveler_discount():
                                print("I will sell each ox with a discount!")
                                print("I will sell you an ox for 16.00", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 16 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_ox_traveler()
                                    elif int(how_many) * 16 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 16
                                        supplies.oxen += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False
                                        
                                        input("Type something to continue: ")

                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_ox_traveler_discount()
                            
                            buy_ox_traveler_discount()


                    elif which_trade == 2:
                        # Money for sets of clothing
                        
                        os.system("cls clear")
                        if discount != True:
                            def buy_clothes_traveler():
                                print("I will sell you sets of clothes for 10.00 each", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 10 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_clothes_traveler()
                                    elif int(how_many) * 10 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 10
                                        supplies.sets_of_clothing += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False

                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_clothes_traveler

                            buy_clothes_traveler()
                        elif discount:
                            def buy_clothes_traveler_discount():
                                print("I will sell you set of clothes with a discount!")
                                print("I will sell you a set of clothes for 8.00", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 8 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_clothes_traveler_discount()
                                    elif int(how_many) * 8 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 8
                                        supplies.sets_of_clothing += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False
                                        
                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_clothes_traveler_discount()
                            
                            buy_clothes_traveler_discount()
                    elif which_trade == 3:
                        #Money for bullets
                        
                        os.system("cls clear")
                        if discount != True:
                            def buy_bullets_traveler():
                                print("I will sell you boxes of ammunition for 2.00 each", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 2 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_bullets_traveler()
                                    elif int(how_many) * 2 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 2
                                        supplies.ammunition += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False

                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_bullets_traveler()

                            buy_bullets_traveler()
                        elif discount:
                            def buy_bullets_traveler_discount():
                                print("I will sell you boxes of ammunition with a discount!")
                                print("I will sell you a set of clothes for 1.00", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 1 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_bullets_traveler_discount()
                                    elif int(how_many) * 1 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 1
                                        supplies.ammunition += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False
                                        
                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_bullets_traveler_discount()
                            
                            buy_bullets_traveler_discount()

                    elif which_trade == 4:
                        #Money for wagon Wheels
                        
                        os.system("cls clear")
                        if discount != True:
                            def buy_wagon_wheels_traveler():
                                print("I will sell you wagon wheels for 10.00 each", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 10 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_wagon_wheels_traveler()
                                    elif int(how_many) * 10 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 10
                                        supplies.wagon_wheels += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False

                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_wagon_wheels_traveler()

                            buy_wagon_wheels_traveler()
                        elif discount:
                            def buy_wagon_wheels_traveler_discount():
                                print("I will sell you wagon wheels with a discount!")
                                print("I will sell you wagon wheels for 8.00", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 8 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_wagon_wheels_traveler_discount()
                                    elif int(how_many) * 8 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 8
                                        supplies.wagon_wheels += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False
                                        
                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_wagon_wheels_traveler_discount()
                            
                            buy_wagon_wheels_traveler_discount()
                    elif which_trade == 5:
                        #Money for wagon axles
                        
                        os.system("cls clear")
                        if discount != True:
                            def buy_wagon_axles_traveler():
                                print("I will sell you wagon axles for 10.00 each", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 10 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_wagon_axles_traveler()
                                    elif int(how_many) * 10 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 10
                                        supplies.wagon_axles += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False

                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_wagon_axles_traveler()

                            buy_wagon_axles_traveler()
                        elif discount:
                            def buy_wagon_axles_traveler_discount():
                                print("I will sell you wagon axles with a discount!")
                                print("I will sell you wagon axles for 8.00", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 8 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_wagon_axles_traveler_discount()
                                    elif int(how_many) * 8 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 8
                                        supplies.wagon_axles += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False
                                        
                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_wagon_axles_traveler_discount()
                            
                            buy_wagon_axles_traveler_discount()
                    elif which_trade == 6:
                        #Money for wagon tongues
                        
                        os.system("cls clear")
                        if discount != True:
                            def buy_wagon_tongues_traveler():
                                print("I will sell you wagon tounges for 10.00 each", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 10 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_wagon_tongues_traveler()
                                    elif int(how_many) * 10 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 10
                                        supplies.wagon_tongues += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False

                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_wagon_tongues_traveler()

                            buy_wagon_tongues_traveler()
                        elif discount:
                            def buy_wagon_tongues_traveler_discount():
                                print("I will sell you wagon axles with a discount!")
                                print("I will sell you wagon axles for 8.00", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 8 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_wagon_tongues_traveler_discount()
                                    elif int(how_many) * 8 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 8
                                        supplies.wagon_tongues += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False
                                        
                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_wagon_tongues_traveler_discount()
                            
                            buy_wagon_tongues_traveler_discount()
                    elif which_trade == 7:
                        #Money for pounds of food
                        
                        os.system("cls clear")
                        if discount != True:
                            def buy_food_traveler():
                                print("I will sell you pounds of food for 0.20 each", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 0.20 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_food_traveler()
                                    elif int(how_many) * 0.20 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 0.20
                                        supplies.pounds_of_food += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False

                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_food_traveler()

                            buy_food_traveler()
                        elif discount:
                            def buy_food_traveler_discount():
                                print("I will sell you pounds of food with a discount!")
                                print("I will sell you pounds of food for 0.10", end="\n\n")
                                how_many = input("How many do you want to buy?: ")

                                try:
                                    if int(how_many) * 0.10 > supplies.money_left:
                                        print("You don't have enough money to buy that many!")
                                        input("Type something to continue: ")
                                        buy_food_traveler_discount()
                                    elif int(how_many) * 0.10 <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * 0.10
                                        supplies.pounds_of_food += int(how_many)
                                        print("Thank you for trading, and best of luck!")
                                        print("The traveler continues on their journey.", end="\n\n")
                                        travel_occurances.traveler_nearby = False
                                        
                                        input("Type something to continue: ")
                                except:
                                    input("That isn't a valid answer, please try again: ")
                                    buy_food_traveler_discount()
                            
                            buy_food_traveler_discount()


                else:
                    print("\nThere aren't any people who are nearby.")
                    input("Please type something to contine: ")

            elif option_choice.strip() == "7":
                def buy_supplies_option():    
                    # Buy Supplies: Check "Buy Supplies Options.png" for more details
                    os.system("cls clear")
                    if travel_occurances.shop_nearby == True:    
                        ox_cost = 20.00
                        clothing_cost = 10.00
                        ammunition_cost = 2.00
                        wagon_wheels_cost = 10.00
                        wagon_axels_cost = 10.00
                        wagon_tongues_cost = 10.00
                        food_cost = 0.20
                        
                        print(f"You may buy:\n\n\t1. Oxen\t\t\t20.00 per ox\t\tYou have: {supplies.oxen}\n\t2. Clothing\t\t10.00 per set\t\tYou have: {supplies.sets_of_clothing}\n\t3. Ammunition\t\t2.00 per box\t\tYou have: {supplies.ammunition}\n\t4. Wagon wheels\t\t10.00 per wheel\t\tYou have: {supplies.wagon_wheels}\n\t5. Wagon axles\t\t10.00 per axle\t\tYou have: {supplies.wagon_axles}\n\t6. Wagon Tongues\t10.00 per tongue\tYou have: {supplies.wagon_tongues}\n\t7. Food\t\t\t0.20 per pound\t\tYou have: {supplies.pounds_of_food}\n\t8. Leave Store\n\n")
                        print(f"You have ${supplies.money_left} to spend.")
                        buy_supplies_number = input("Which number: ")

                        if buy_supplies_number.lower().strip() == "1":
                            # Oxen
                            if supplies.money_left >= ox_cost:
                                how_many = input("\nHow many: ")
                                if how_many.isdigit():
                                    if int(how_many) * ox_cost <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * ox_cost
                                        supplies.oxen += int(how_many)
                                        buy_supplies_option()
                                    else:
                                        print("Not Enough Money")
                                        input("Type something to continue: ")
                                        buy_supplies_option()
                                else:
                                    print("That isn't a number.")
                                    input("Type something to continue: ")
                            else:
                                print("\nYou don't have anymore money left to spend.")
                                input("Please type something to continue: ")
                                buy_supplies_option()
                        elif buy_supplies_number.lower().strip() == "2":
                            # Clothing
                            if supplies.money_left >= clothing_cost:
                                how_many = input("\nHow many: ")
                                if how_many.isdigit():
                                    if int(how_many) * clothing_cost <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * clothing_cost
                                        supplies.sets_of_clothing += int(how_many)
                                        buy_supplies_option()
                                    else:
                                        print("Not Enough Money")
                                        input("Type something to continue: ")
                                        buy_supplies_option()
                                else:
                                    print("That isn't a number.")
                                    input("Type something to continue: ")
                            else:
                                print("\nYou don't have anymore money left to spend.")
                                input("Please type something to continue: ")
                                buy_supplies_option()
                        elif buy_supplies_number.lower().strip() == "3":
                            # Ammunition
                            if supplies.money_left >= ammunition_cost:
                                how_many = input("\nHow many: ")
                                if how_many.isdigit():
                                    if int(how_many) * ammunition_cost <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * ammunition_cost
                                        supplies.ammunition += int(how_many)
                                        buy_supplies_option()
                                    else:
                                        print("Not Enough Money")
                                        input("Type something to continue: ")
                                        buy_supplies_option()
                                else:
                                    print("That isn't a number.")
                                    input("Type something to continue: ")
                            else:
                                print("\nYou don't have anymore money left to spend.")
                                input("Please type something to continue: ")
                                buy_supplies_option()
                            buy_supplies_option()
                        elif buy_supplies_number.lower().strip() == "4":
                            # Wagon wheels
                            if supplies.money_left >= wagon_wheels_cost:
                                how_many = input("\nHow many: ")
                                if how_many.isdigit():
                                    if int(how_many) * wagon_wheels_cost <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * wagon_wheels_cost
                                        supplies.wagon_wheels += int(how_many)
                                        buy_supplies_option()
                                    else:
                                        print("Not Enough Money")
                                        input("Type something to continue: ")
                                        buy_supplies_option()
                                else:
                                    print("That isn't a number.")
                                    input("Type something to continue: ")
                            else:
                                print("\nYou don't have anymore money left to spend.")
                                input("Please type something to continue: ")
                                buy_supplies_option()
                            buy_supplies_option()
                        elif buy_supplies_number.lower().strip() == "5":
                            # Wagon axles
                            if supplies.money_left >= wagon_axels_cost:
                                how_many = input("\nHow many: ")
                                if how_many.isdigit():
                                    if int(how_many) * wagon_axels_cost <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * wagon_axels_cost
                                        supplies.wagon_axles += int(how_many)
                                        buy_supplies_option()
                                    else:
                                        print("Not Enough Money")
                                        input("Type something to continue: ")
                                        buy_supplies_option()
                                else:
                                    print("That isn't a number.")
                                    input("Type something to continue: ")
                            else:
                                print("\nYou don't have anymore money left to spend.")
                                input("Please type something to continue: ")
                                buy_supplies_option()
                            buy_supplies_option()
                        elif buy_supplies_number.lower().strip() == "6":
                            # Wagon tongues
                            if supplies.money_left >= wagon_tongues_cost:
                                how_many = input("\nHow many: ")
                                if how_many.isdigit():
                                    if int(how_many) * wagon_tongues_cost <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * wagon_tongues_cost
                                        supplies.wagon_tongues += int(how_many)
                                        buy_supplies_option()
                                    else:
                                        print("Not Enough Money")
                                        input("Type something to continue: ")
                                        buy_supplies_option()
                                else:
                                    print("That isn't a number.")
                                    input("Type something to continue: ")
                            else:
                                print("\nYou don't have anymore money left to spend.")
                                input("Please type something to continue: ")
                                buy_supplies_option()
                            buy_supplies_option()
                        elif buy_supplies_number.lower().strip() == "7":
                            # Food
                            if supplies.money_left >= food_cost:
                                how_many = input("\nHow many: ")
                                if how_many.isdigit():
                                    if int(how_many) * food_cost <= supplies.money_left:
                                        supplies.money_left -= int(how_many) * food_cost
                                        supplies.pounds_of_food += int(how_many)
                                        buy_supplies_option()
                                    else:
                                        print("Not Enough Money")
                                        input("Type something to continue: ")
                                        buy_supplies_option()
                                else:
                                    print("That isn't a number.")
                                    input("Type something to continue: ")
                            else:
                                print("\nYou don't have anymore money left to spend.")
                                input("Please type something to continue: ")
                                buy_supplies_option()
                            buy_supplies_option()
                        elif buy_supplies_number.lower().strip() == "8":
                            # Leave store
                            pass
                        else:
                            buy_supplies_option()
                    elif travel_occurances.shop_nearby == False:
                        print("There is no shop nearby at the moment.\n")
                        input("Please type something to continue: ")

                buy_supplies_option()
            elif option_choice.strip() == "8":
                # Check health states of members
                os.system("cls clear")

                # Person 1 (Wife)
                if wagon_passengers_health_state.healthy_wife:
                    print("Wife: Healthy")
                elif wagon_passengers_health_state.injured_wife:
                    print("Wife: Injured")
                elif wagon_passengers_health_state.diseases_wife:
                    print("Wife: Has a disease")
                elif wagon_passengers_health_state.dead_wife:
                    print("Wife: Dead")
                
                # Person 2 (Little Mary)
                if wagon_passengers_health_state.healthy_mary:
                    print("Little Mary: Healthy")
                elif wagon_passengers_health_state.injured_mary:
                    print("Little Mary: Injured")
                elif wagon_passengers_health_state.diseases_mary:
                    print("Little Mary: Has a disease")
                elif wagon_passengers_health_state.dead_mary:
                    print("Little Mary: Dead")
                
                # Person 3 (Little Billy)
                if wagon_passengers_health_state.healthy_billy:
                    print("Little Billy: Healthy", end="\n\n")
                elif wagon_passengers_health_state.injured_billy:
                    print("Little Billy: Injured", end="\n\n")
                elif wagon_passengers_health_state.diseases_billy:
                    print("Little Billy: Has a disease", end="\n\n")
                elif wagon_passengers_health_state.dead_billy:
                    print("Little Billy: Dead", end="\n\n")
                
                input("Type something to exit: ")
    
    Choose_Profession()

if __name__ == "__main__":
    Start_Game()