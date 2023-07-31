import os
import random

"""Recreation of "The Oregon Trail Game"
    TODO: 
        1. Write a save function to save all stats
        2. Write a delete save function to remove the save data
        3. Write a load function to load all stats and "continue" the game
        4. Write a function to check if save file is there, otherwise 
        create file with no save data
        5. Playtest game to check for anymore bugs or events that occur to often or less
"""


os.system("title The Oregon Trail")
# A class that has info about the character you play so you can get started.
class main_character:
    def __init__(self, profession1, skill_sets, start_money, difficulty, health, days_to_heal, discount_perk):
        self.profession = profession1
        self.skill_sets = skill_sets
        self.start_money = start_money
        self.difficulty = difficulty
        # Three stages of health:
        # healthy, sick, dead
        self.health = health
        self.days_to_heal = days_to_heal
        self.discount_perk = discount_perk

# A class that helps with stats to help you with traveling to know if you should make desperate changes.
class travel_stats:
    def __init__(self, pace, rations, distance_left, fatigued, days_traveled):
        self.pace = pace
        self.rations = rations
        self.distance_left = distance_left
        # Fatigued = 0 : Not tired
        # Fatigued = 7 : Needs sleep or sick
        # Fatigued = 8 : Sick, desperately needs sleep
        # Fatigued = 11 : Dies
        self.fatigued = fatigued
        self.days = days_traveled
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


main_character = main_character(profession1="none", skill_sets="none", start_money=0, difficulty="none", health="healthy", days_to_heal=0, discount_perk=False)
travel_stats = travel_stats(pace="steady", rations="filling", distance_left=2000, fatigued=0, days_traveled=0)
supplies = supplies(oxen=0, sets_of_clothing=0, ammunition=0, wagon_wheels=0, wagon_axles=0, wagon_tongues=0, pounds_of_food=0, money_left="unkown")
travel_occurances = travel_occurances(traveler_nearby=False, forest_nearby=False, shop_nearby=False, broken_wagon_wheels=False, broken_wagon_axles=False, broken_wagon_tongues=False, injured_ox=False)

def Start_Game():
    
    os.system("cls clear")

    game_running = True

    # While loop to keep the game running
    # Create random events that injure people, starvation, hunting, broke down wagon, and professions
    # That give different advantages.

    def Choose_Profession():
            print("What do you want your profession to be?")
            profession_choice = input("Banker, Carpenter, or Farmer: ")

            if profession_choice.lower().strip() == "banker":
                main_character.profession = "Banker"
                main_character.skill_sets = "Lower trade costs and higher starting money"
                main_character.start_money = 1600
                main_character.difficulty = "Easy"
                travel_occurances.shop_nearby = True
                main_character.discount_perk = True
                stats_question()
            elif profession_choice.lower().strip() == "carpenter":
                main_character.profession = "Carpenter"
                main_character.skill_sets = "Lower chance of things on your wagon breaking"
                main_character.start_money = 800
                main_character.difficulty = "Medium"
                travel_occurances.shop_nearby = True
                main_character.discount_perk = False
                stats_question()
            elif profession_choice.lower().strip() == "farmer":
                main_character.profession = "Farmer"
                main_character.skill_sets = "Find more food while out hunting in nearby forests"
                main_character.start_money = 400
                main_character.difficulty = "Hard"
                travel_occurances.shop_nearby = True
                main_character.discount_perk = False
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
            print(f"Distance To Travel: {travel_stats.distance_left}\nHealth: {main_character.health}\nPace: {travel_stats.pace}\nRations: {travel_stats.rations}\nFatigue Level: {travel_stats.fatigued}\n\nYou may:\n\n\t1: Continue on trail\n\t2: Check Supplies\n\t3: Change Pace\n\t4: Change food rations\n\t5: Stop to rest\n\t6: Attempt to trade\n\t7: Buy Supplies\n\t8: Hunt in nearby forest\n")
            option_choice = input("What is your choice: ")

            if option_choice.strip() == "1":
                def start_traveling():
                    
                    # They started traveling so make sure they can't trade or go to stores
                    # that they left while continuing on the trail
                    travel_occurances.shop_nearby = False
                    travel_occurances.traveler_nearby = False
                    travel_occurances.forest_nearby = False
                    
                    # Travel faster or slower based on pace
                    if travel_stats.pace == "steady":
                        random_distance_roll = random.randint(10, 50)
                    if travel_stats.pace == "strenuous":
                        random_distance_roll = random.randint(50, 75)
                        # Have a chance of getting sick while in this pace
                        sick_roll = random.randint(1, 6)
                        if sick_roll == 1:
                            main_character.health = "sick"
                            main_character.days_to_heal += 2
                            print("You got sick from sleep deprivation!")
                            print("Hint: To lower the chances of getting sick this way, consider changing your pace")
                            input("Type something to continue: ")
                        
                    if travel_stats.pace == "grueling":
                        random_distance_roll = random.randint(100, 150)
                        # Have a chance of getting sick while in this pace
                        sick_roll = random.randint(1, 4)
                        if sick_roll == 1:
                            main_character.health = "sick"
                            main_character.days_to_heal += 2
                            print("You got sick from sleep deprivation!")
                            print("Hint: To lower the chance of getting sick this way, consider changing your pace")
                            input("Type something to continue: ")
                    
                    if travel_stats.distance_left > random_distance_roll:
                        travel_stats.distance_left -= random_distance_roll
                        travel_stats.fatigued += 1
                        travel_stats.days += 1
                        
                        if travel_stats.fatigued == 7:
                            print("You should rest. If you continue, you will get sick!")
                            input("Type something to continue: ")
                        elif travel_stats.fatigued == 8:
                            print("You got sick! Rest or you may die of sleep deprivation!")
                            main_character.health = "sick"
                            main_character.days_to_heal += 2
                            input("Type something to continue: ")
                        elif travel_stats.fatigued == 11:
                            print("You died of sleep deprivation!")
                            print("GAME OVER")
                            input("Type something to continue: ")
                            quit()
                        
                    elif travel_stats.distance_left <= random_distance_roll:
                        print(f"You beat the game! You traveled to your destination in {travel_stats.days}!")
                        input("Type something to continue: ")
                        quit()
                    
                    # Showing stats to player
                    os.system("cls clear")
                    print(f"You have {travel_stats.distance_left} miles left")
                    print(f"Your pace: {travel_stats.pace}")
                    print(f"Your Health: {main_character.health}")
                    print(f"Your rations: {travel_stats.rations}")
                    print(f"Fatigue Level: {travel_stats.fatigued}", end="\n\n")
                    print(f"Total days went by: {travel_stats.days}")
                    # Let the user know something is happening
                    print(f"You continue down the trail and travel {random_distance_roll} miles...")
                    input("Type something to continue: ")

                    # Bad and Good event rolls
                    good_roll = random.randint(1, 5)
                    nearby_events_roll = random.randint(1, 6)
                    bad_roll1 = random.randint(1, 5)

                    

                    # Lose food as you travel
                    if travel_stats.rations == "filling":
                        # Make sure they have enough food
                        if supplies.pounds_of_food >= 25:
                            supplies.pounds_of_food -= 25
                        else:
                            print("You died of starvation!")
                            print("GAME OVER")
                            input("Type something to continue: ")
                            quit()
                    if travel_stats.rations == "meager":
                        # Make sure they have enough food
                        if supplies.pounds_of_food >= 10:
                            supplies.pounds_of_food -= 10
                            # A small chance that you can get sick
                            sick_roll = random.randint(1, 5)
                            if sick_roll == 1:
                                print("You got sick!")
                                main_character.health = "sick"
                                main_character.days_to_heal += 2
                                print("To lower the chance of getting sick! Keep the rations at \"filling\"")
                                input("Type something to continue: ")
                        else:
                            print("You died of starvation!")
                            print("GAME OVER")
                            input("Type something to continue: ")
                            quit()
                    if travel_stats.rations == "bare bones":
                        # Make sure they have enough food
                        if supplies.pounds_of_food >= 5:
                            supplies.pounds_of_food -= 5
                            sick_roll = random.randint(1, 3)
                            if sick_roll == 1:
                                print("You got sick!")
                                main_character.health = "sick"
                                main_character.days_to_heal += 2
                                print("To lower the chances of getting sick, keep the rations at \"filling\" or \"meager\"")
                                input("Type something to continue: ")
                        else:
                            print("You died of starvation!")
                            print("GAME OVER")
                            input("Type something to continue: ")
                            quit()
                    
                    # Warns player if their food is getting low
                    if supplies.pounds_of_food <= 200:
                        print("Your food supply is getting low!")
                        print(f"You have {supplies.pounds_of_food} pounds of food left!")
                        input("Type something to continue: ")
                    
                    
                    if good_roll == 1:
                        print("You found a nearby traveler who is willing to sell some items to you!")
                        travel_occurances.traveler_nearby = True
                        input("Type something to continue: ")
                    
                    if nearby_events_roll == 1:
                        # This will be for coming to a nearby travler, or finding a forest to hunt in
                        
                        # Check if there's a chance that something is nearby | 1 in 5 chance
                        nearby = random.randint(1, 5)
                        
                        if nearby == 1:
                            # Choose wether it's a traveler or forest to hunt in, and if unlucky nothing will happen
                            travelerForestRoll = random.randint(1, 5)
                            if travelerForestRoll == 1:
                                # Town
                                travel_occurances.traveler_nearby = True
                                print("You found a nearby traveler who is willing to sell some items to you!")
                            elif travelerForestRoll in [2, 3]:
                                # Forest
                                travel_occurances.forest_nearby = True
                                print("There's a forest nearby!")
                                print("You can stop to hunt and use a day, or you can continue on the trail...")
                                input("Type something to continue: ")
                            
                            

                    if bad_roll1 == 1:
                        bad_roll2 = random.randint(1, 6)
                        
                        if bad_roll2 == 1:
                            # Worn out clothes
                            if supplies.sets_of_clothing >= 1:
                                supplies.sets_of_clothing -= 1
                                print("A set of your clothes got ripped while traveling!")
                                print(f"You lost 1 set of clothing and have {supplies.sets_of_clothing} set(s) of clothing left")
                                input("Type something to continue: ")
                        
                        elif bad_roll2 == 2:
                            # Lose some food
                            lose_food_roll = random.randint(10, 30)
                            
                            print("You notice that some of the food went bad.")
                            print(f"You lose {lose_food_roll} pounds of food")

                            supplies.pounds_of_food -= lose_food_roll

                            input("Type something to continue: ")
                        
                        elif bad_roll2 == 3:
                            # Someone gets sick
                            if main_character.health == "healthy":
                                main_character.health = "sick"
                                main_character.days_to_heal += 3
                                print("You got sick while traveling!")
                                input("Type something to continue: ")
                            else:
                                print("You died of sickness!")
                                print("GAME OVER!")
                                input("Type something to continue: ")
                                quit()
                        
                        elif bad_roll2 == 4:
                            # A part on the wagon breaks
                            # Random roll to decide which part breaks
                            
                            # If your profession is a carpenter, lower chance of a part breaking
                            if main_character.profession == "Carpenter":
                                carpenter_helpPerk_roll = random.randint(1, 2)
                                if carpenter_helpPerk_roll == 1:
                                    # Don't have a part break
                                    print("You notice that one of your parts on the wagon was broken.")
                                    print("However, you fix it up as if nothing happened.")
                                    input("Type something to continue: ")
                                    # Skips everything else and continues the game
                                    run_game()
                                
                            part_break = random.randint(1, 3)
                            
                            # Wagon wheels break
                            if part_break == 1:
                                print("One of your wagon wheels broke!")
                                if supplies.wagon_wheels >= 1:
                                    supplies.wagon_wheels -= 1
                                    print("You replaced one of your wheels with the broken one!")
                                    print("You continue along the trail.")
                                    input("Type something to continue: ")
                                elif supplies.wagon_wheels == 0:
                                    travel_occurances.broken_wagon_wheels = True
                                    print("You don't have enough wagon wheels to replace the broken one!")
                                    print("You can wait for a traveler nearby to pass!")
                                    input("Type something to continue: ")
                            
                            # Wagon tongues break
                            elif part_break == 2:
                                print("one of your wagon tongues broke!")
                                if supplies.wagon_tongues >= 1:
                                    supplies.wagon_tongues -= 1
                                    print("You replaced one of your wagon tongues with the broken one!")
                                    print("You continue along the trail.")
                                    input("Type something to continue: ")
                                elif supplies.wagon_tongues == 0:
                                    travel_occurances.broken_wagon_wheels = True
                                    print("You don't have enough wagon tongues to replace the broken one!")
                                    print("You can wait for a traveler nearby to pass!")
                                    input("Type something to continue: ")
                            
                            # Wagon axles break
                            elif part_break == 3:
                                print("one of your wagon axles broke!")
                                if supplies.wagon_axles >= 1:
                                    supplies.wagon_axles -= 1
                                    print("You replaced one of your wagon axles with the broken one!")
                                    print("You continue along the trail.")
                                    input("Type something to continue: ")
                                elif supplies.wagon_axles == 0:
                                    travel_occurances.broken_wagon_wheels = True
                                    print("You don't have enough wagon axles to replace the broken one!")
                                    print("You can wait for a traveler nearby to pass!")
                                    input("Type something to continue: ")
                                    

                        elif bad_roll2 == 5:
                            # Wade across a river | Have a chance to sucessfully do it, or lose an item
                            os.system("cls clear")
                            print("You run into a river! You must wade across it!")
                            input("Type something to continue: ")
                            # A roll whether they pass through it successfully or not
                            success_or_failure = random.randint(1, 2)
                            
                            if success_or_failure == 1:
                                # Successfully passes without anything bad happening
                                print("You successfully passed the river!")
                                input("Type something to continue: ")
                            elif success_or_failure == 2:
                                # Fails to pass without losing something
                                print("You passed the river, but you didn't do it without losing something!")
                                # A roll to see what they lost
                                random_loss = random.randint(1, 3)
                                if random_loss == 1:
                                    # Loss of Ammunition
                                    # A roll on how much they lost
                                    ammunition_lost = random.randint(1, 3)
                                    # Make sure they don't lose more than they have
                                    if ammunition_lost >= supplies.ammunition:
                                        supplies.ammunition = 0
                                        print("You lost all of your ammunition!")
                                        input("Type something to continue: ")
                                    else:
                                        supplies.ammunition -= ammunition_lost
                                        print(f"You lost {ammunition_lost} bullets!")
                                        print(f"You have {supplies.ammunition} bullets left!")
                                        input("Type something to continue: ")
                                    
                                elif random_loss == 2:
                                    # Loss of Food
                                    # A roll on how much they lost
                                    food_lost = random.randint(50, 100)
                                    # Make sure they don't lose more than they have
                                    if food_lost >= supplies.pounds_of_food:
                                        supplies.pounds_of_food = 0
                                        print("You lost all of your food!")
                                        input("Type something to continue: ")
                                    else:
                                        supplies.pounds_of_food -= food_lost
                                        print(f"You lost {food_lost} pounds of food!")
                                        print(f"You have {supplies.pounds_of_food} pounds of food left!")
                                        input("Type something to continue: ")
                                        
                                elif random_loss == 3:
                                    # Loss of Money
                                    # A roll on how much they lost
                                    money_lost = random.randint(50, 100)
                                    # Make sure they don't lose more than they have
                                    if money_lost >= supplies.money_left:
                                        supplies.money_left = 0
                                        print("You lost all of your money!")
                                        input("Type something to continue: ")
                                    else:
                                        supplies.money_left -= money_lost
                                        print(f"You dropped ${money_lost} while crossing the river!")
                                        print(f"You still have ${supplies.money_left} left!")
                                        input("Type something to continue: ")
                            elif bad_roll2 == 6:
                                # Injured oxen
                                print("One of your oxen got injured!")
                                if supplies.oxen >= 1:
                                    supplies.oxen -= 1
                                    print("You replaced one of your injured oxen with another!")
                                    print("You continue along the trail.")
                                    input("Type something to continue: ")
                                elif supplies.oxen == 0:
                                    travel_occurances.injured_ox = True
                                    print("You don't have enough wagon tongues to replace the broken one!")
                                    print("You can wait for a traveler nearby to pass!")
                                    input("Type something to continue: ")
                            
                # Checks if they have enough supplies to continue
                if travel_occurances.broken_wagon_wheels == False and travel_occurances.broken_wagon_axles == False and travel_occurances.broken_wagon_tongues == False and supplies.sets_of_clothing >= 1 and supplies.oxen >= 1:
                        start_traveling()
                else:
                    # If a part of their wagon broke, injured ox, or ripped clothing
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
                            print("\nKeep trying until a traveler comes nearby!", end="\n\n")

                            if new_traveler == 1:
                                print("A traveler comes nearby and greets you", end="\n\n")
                                travel_occurances.traveler_nearby = True
                            
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
                            print("\nKeep trying until a traveler comes nearby!", end="\n\n")

                            if new_traveler == 1:
                                print("A travler comes nearby and greets you", end="\n\n")
                                travel_occurances.traveler_nearby = True
                            
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
                            print("\nKeep trying until a traveler comes nearby!", end="\n\n")

                            if new_traveler == 1:
                                print("A travler comes nearby and greets you", end="\n\n")
                                travel_occurances.traveler_nearby = True
                            
                            input("Type something to continue: ")
                    elif supplies.sets_of_clothing == 0:
                        new_traveler = random.randint(1, 2)
                        print("You don't have enough sets of clothing to continue.")
                        print("\nKeep trying until a traveler comes nearby!", end="\n\n")

                        if new_traveler == 1:
                            print("A travler comes nearby and greets you", end="\n\n")
                            travel_occurances.traveler_nearby = True
                        
                        input("Type something to continue: ")
                    
                    elif supplies.oxen == 0:
                        new_traveler = random.randint(1, 2)
                        print("You don't have enough oxen to continue.")
                        print("\nKeep trying until a traveler comes nearby!", end="\n\n")

                        if new_traveler == 1:
                            print("A travler comes nearby and greets you", end="\n\n")
                            travel_occurances.traveler_nearby = True
                        
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
                        change_pace_def()
                    
                    elif change_pace.strip() == "5":
                        # For exiting the shop | IMPORTANT DON'T DELETE
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
                    print("The amount of food the people in your party eat each day can change. These amounts are:\n\n\t1. filling - meals are adequate.\n\n\t2. meager - meals are small, but have a chance of getting sick.\n\n\t3. bare bones - meals are very small; you stay hungry and have a higher chance of getting sick.")
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
                if main_character.days_to_heal >= 6:
                    os.system("cls clear")
                    print("You died because you never recovered from your past illnesses!")
                    print("GAME OVER")
                    input("Type something to continue: ")
                    quit()
                
                elif main_character.days_to_heal >= 1:
                    if main_character.days_to_heal > 1:
                        # Eat a random amount of food
                        food_eat_roll = random.randint(5, 15)
                        # Checking if the amount of food they lose is greater than how much they have
                        if food_eat_roll >= supplies.pounds_of_food:
                            food_eat_roll = supplies.pounds_of_food
                        
                        supplies.pounds_of_food -= food_eat_roll
                        main_character.days_to_heal -= 1
                        print("You healed yourself by resting!")
                        print(f"You have {main_character.days_to_heal} days left to heal until you're healthy")
                        print(f"You spend a day healing, you eat {food_eat_roll} pounds of food")
                        print(f"You have {supplies.pounds_of_food} pounds of food left")
                        input("Type something to continue: ")
                    elif main_character.days_to_heal == 1:
                        main_character.days_to_heal = 0
                        main_character.health = "healthy"
                        print(f"You healed yourself fully, you're now healthy!")
                        input("Type something to continue: ")
                if travel_occurances.injured_ox == True:
                    travel_occurances.injured_ox = False
                    print("Your ox have healed!")
                    input("Type something to continue: ")
                if travel_stats.fatigued >= 2:
                    travel_stats.fatigued -= 2
                    print(f"Your fatigue level is now {travel_stats.fatigued}")
                    input("Type something to continue: ")
                elif travel_stats.fatigued <=2:
                    travel_stats.fatigued = 0
                    print(f"Your fatigue level is now {travel_stats.fatigued}")
                    input("Type something to continue: ")
                travel_stats.days += 1

            elif option_choice.strip() == "6":
                # Attempt to trade: Check "Attempt to Trade Options.png" for more details
                os.system("cls clear")
                if travel_occurances.traveler_nearby:
                    
                    # Check to make sure a part isn't broken on wagon
                    if travel_occurances.broken_wagon_wheels == False and travel_occurances.broken_wagon_axles == False and travel_occurances.broken_wagon_tongues == False and supplies.sets_of_clothing >= 1 and supplies.oxen >= 1:
                        which_trade = random.randint(1, 7)
                    else:
                        # Check which part of the wagon is broken
                        if travel_occurances.broken_wagon_wheels:
                            # Makes traveler sell wagon wheels
                            which_trade = 4
                        elif travel_occurances.broken_wagon_tongues:
                            # Makes traveler sell wagon axles
                            which_trade = 5
                        elif travel_occurances.broken_wagon_axles:
                            # Makes traveler sell wagon tongues
                            which_trade = 6
                        elif supplies.sets_of_clothing == 0:
                            # Makes traveler sell sets of clothes
                            which_trade = 2
                        elif supplies.oxen == 0:
                            # Makes traveler sell oxen
                            which_trade = 1
                    
                    # If player is banker, then they get lower trade costs
                    if which_trade == 1:
                        # Money for ox
                        
                        os.system("cls clear")
                        if main_character.discount_perk != True:
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

                        elif main_character.discount_perk:
                            def buy_ox_traveler_discount():
                                print("I will sell each ox with a discount!")
                                print("I will sell you an ox for 16.00 each", end="\n\n")
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
                        if main_character.discount_perk != True:
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
                                    buy_clothes_traveler()

                            buy_clothes_traveler()
                        elif main_character.discount_perk:
                            def buy_clothes_traveler_discount():
                                print("I will sell you set of clothes with a discount!")
                                print("I will sell you a set of clothes for 8.00 each", end="\n\n")
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
                        if main_character.discount_perk != True:
                            def buy_bullets_traveler():
                                print("I will sell you ammunition for 2.00 each", end="\n\n")
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
                        elif main_character.discount_perk:
                            def buy_bullets_traveler_discount():
                                print("I will sell you boxes of ammunition with a discount!")
                                print("I will sell you a box of ammunition for 1.00 each", end="\n\n")
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
                        if main_character.discount_perk != True:
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
                        elif main_character.discount_perk:
                            def buy_wagon_wheels_traveler_discount():
                                print("I will sell you wagon wheels with a discount!")
                                print("I will sell you wagon wheels for 8.00 each", end="\n\n")
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
                        if main_character.discount_perk != True:
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
                        elif main_character.discount_perk:
                            def buy_wagon_axles_traveler_discount():
                                print("I will sell you wagon axles with a discount!")
                                print("I will sell you wagon axles for 8.00 each", end="\n\n")
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
                        if main_character.discount_perk != True:
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
                        elif main_character.discount_perk:
                            def buy_wagon_tongues_traveler_discount():
                                print("I will sell you wagon axles with a discount!")
                                print("I will sell you wagon axles for 8.00 each", end="\n\n")
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
                        if main_character.discount_perk != True:
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
                        elif main_character.discount_perk:
                            def buy_food_traveler_discount():
                                print("I will sell you pounds of food with a discount!")
                                print("I will sell you pounds of food for 0.10 each", end="\n\n")
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
                        
                        print(f"You may buy:\n\n\t1. Oxen\t\t\t20.00 per ox\t\tYou have: {supplies.oxen}\n\t2. Clothing\t\t10.00 per set\t\tYou have: {supplies.sets_of_clothing}\n\t3. Ammunition\t\t2.00 per bullet\t\tYou have: {supplies.ammunition}\n\t4. Wagon wheels\t\t10.00 per wheel\t\tYou have: {supplies.wagon_wheels}\n\t5. Wagon axles\t\t10.00 per axle\t\tYou have: {supplies.wagon_axles}\n\t6. Wagon Tongues\t10.00 per tongue\tYou have: {supplies.wagon_tongues}\n\t7. Food\t\t\t0.20 per pound\t\tYou have: {supplies.pounds_of_food}\n\t8. Leave Store\n\n")
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
                            run_game()
                        else:
                            buy_supplies_option()
                    elif travel_occurances.shop_nearby == False:
                        print("There is no shop nearby at the moment.\n")
                        input("Please type something to continue: ")

                buy_supplies_option()
            
            elif option_choice.strip() == "8":
                # Clean up the terminal (Clears it)
                os.system("cls clear")
                
                # Check if forest is nearby
                if travel_occurances.forest_nearby == True:
                    # Checks if they have any bullets to hunt
                    if supplies.ammunition > 0:
                        print("You go hunting for animals nearby...")
                        # Come back with random amount of food
                        if main_character.profession != "Farmer":
                            hunting_food = random.randint(50, 100)
                        # If they are a farmer, they come back with more food, (Profession Perk)
                        else:
                            hunting_food = random.randint(150, 250)
                            farmer_perk = random.randint(15, 50)
                            supplies.pounds_of_food += farmer_perk
                        
                        supplies.pounds_of_food += hunting_food
                        # Lose a random amount of ammunition
                        ammunition_lost = random.randint(5, 25)
                        # If you lose more ammo than you have, set the amount of ammunition to 0
                        if ammunition_lost >= supplies.ammunition:
                            supplies.ammunition = 0
                            print("You lost all of your ammunition while hunting!")
                        else:
                            supplies.ammunition -=  ammunition_lost
                            print(f"You lost {ammunition_lost} bullets while hunting, {supplies.ammunition} ammunition left!")
                        print(f"You won {hunting_food} pounds of food while hunting!")
                        print(f"You now have {supplies.pounds_of_food} pounds of food!")
                        print(f"You lost {ammunition_lost} bullets while hunting, {supplies.ammunition} ammunition left!")
                        input("Type something to continue: ")
                    # If they don't have any bullets to hunt
                    else:
                        print("You don't have any ammunition to hunt with...")
                        input("Type something to continue: ")
                else:
                    print("There is not a forest nearby to hunt in...")
                    input("Type something to continue: ")
                    
    
    Choose_Profession()

if __name__ == "__main__":
    Start_Game()