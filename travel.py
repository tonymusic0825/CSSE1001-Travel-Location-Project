"""

"""

__author__ = ""
__date__ = ""


from destinations import Destinations

def interest_input(interest):
    """Outputs interest questions, takes and validates user input

    Parameters:
        interest (str): Name of interest type

    Return:
        int: The value of user input
    """

    interest_value = 0

    while True:
        print("How much do you like " + interest + "? (-5 to 5)")
        interest_value = int(input("> "))

        if interest_value > -6 and interest_value < 6:
            break
        else:
            print()
            print("I'm sorry, but " + str(interest_value) + " is not a valid choice. Please try again.")
            print()
            continue

    return interest_value

def change_multivalue_input(input):
    """Changes user's multivalued string input into integers within a list

    Parameters:
        input (str): User's input with multiple values

    Return:
        list<int>: List including the values of the user's input which have been turned into integers
    """
    change_list = []

    input = input.replace(" ", "")
    input = input.split(",")

    for value in input:
        if int(value) not in change_list:
            change_list.append(int(value))
        else:
            continue

    return change_list

def compare_season_score(destination, list_season):
    """Finds highest score for the corresponding seasons of user's choice of a particular destination

    Parameters:
        destination (instance): Instance of a certain destination
        list_season (list<str>): User's input for seasons

    Return:
        int: The highest season score for user's choices
    """

    destination_season_score = destination.get_season_factor(list_season[0])

    for season_choice in list_season:
        if destination_season_score < destination.get_season_factor(season_choice):
            destination_season_score = destination.get_season_factor(season_choice)

    return destination_season_score

def calculate_score(destination, season_score, sports, wildlife, nature, historical, fine_dining, adventure, beach):
    """Calculates the score of a particular destination

    Parameters:
        destination (instance): Particular destination
        season_score (int): Season score for the same destination parameter
        sports (int): User's input value for sport
        wildlife (int): User's input value for wildlife
        nature (int): User's input value for nature
        historical (int): User's input value for historical
        fine_dining (int): User's input value for fine_dining
        adventure (int): User's input value for adventure
        beach(int): User's input value for beach

    Return:
        int: The calculated score for a certain destination
    """

    destination_interest_score = 0
    destination_score = 0

    destination_interest_score = sports * destination.get_interest_score('sports')       \
                              + wildlife * destination.get_interest_score('wildlife')    \
                              + nature * destination.get_interest_score('nature')        \
                              + historical * destination.get_interest_score('historical')\
                              + fine_dining * destination.get_interest_score('cuisine')  \
                              + adventure * destination.get_interest_score('adventure')  \
                              + beach * destination.get_interest_score('beach')

    destination_score = destination_interest_score * season_score

    return destination_score

def continent_choice():
    """Prints continent choices and validates user input

    Return:
        list<int>: User input in list form
    """

    ASIA = "Asia"
    AFRICA = "Africa"
    NORTH_AMERICA = "North America"
    SOUTH_AMERICA = "South America"
    EUROPE = "Europe"
    OCEANIA = "Oceania"
    ANTARCTICA = "Antarctica"

    while True:
        list_continent = []
        continent_status = True

        print("Which continents would you like to travel to?")
        print("  1) " + ASIA)
        print("  2) " + AFRICA)
        print("  3) " + NORTH_AMERICA)
        print("  4) " + SOUTH_AMERICA)
        print("  5) " + EUROPE)
        print("  6) " + OCEANIA)
        print("  7) " + ANTARCTICA)
        continent = input("> ")

        list_continent_int = change_multivalue_input(continent)

        for number in list_continent_int:
            if number > 0 and number < 8:
                if number == 1:
                    list_continent.append(ASIA.lower())
                elif number == 2:
                    list_continent.append(AFRICA.lower())
                elif number == 3:
                    list_continent.append(NORTH_AMERICA.lower())
                elif number == 4:
                    list_continent.append(SOUTH_AMERICA.lower())
                elif number == 5:
                    list_continent.append(EUROPE.lower())
                elif number == 6:
                    list_continent.append(OCEANIA.lower())
                elif number == 7:
                    list_continent.append(ANTARCTICA.lower())

            else:
                print()
                print("I'm sorry, but " + continent + " is not a valid choice. Please try again.")
                print()
                continent_status = False
                break
        if continent_status == False:
            continue
        else:
            break

    return list_continent

def cost_choice():
    """Prints cost choices and validates user input

    Return:
        str: User's cost choice input
    """
    while True:
        print("What is money to you?")
        print("  $$$) No object")
        print("  $$) Spendable, so long as I get value from doing so")
        print("  $) Extremely important; I want to spend as little as possible")
        cost = input("> ")

        if cost == "$$$" or cost == "$$" or cost == "$":
            break
        else:
            print()
            print("I'm sorry, but " + cost + " is not a valid choice. Please try again.")
            print()
            continue

    return cost

def crime_choice():
    """Prints crime choices and validates user input

    Return:
        str: User's crime choice input
    """

    LOW = "Low"
    AVERAGE = "Average"
    HIGH = "High"

    while True:
        print("How much crime is acceptable when you travel?")
        print("  1) " + LOW)
        print("  2) " + AVERAGE)
        print("  3) " + HIGH)
        crime = int(input("> "))

        if crime > 0 and crime < 4:
            if crime == 1:
                crime = LOW.lower()
                break
            elif crime == 2:
                crime = AVERAGE.lower()
                break
            elif crime == 3:
                crime = HIGH.lower()
                break
        else:
            print()
            print("I'm sorry, but " + str(crime) + " is not a valid choice. Please try again.")
            print()
            continue

    return crime

def kid_friendly_choice():
    """Prints children choices and validates user input

    Return:
        Bool: User's children choice
    """
    while True:
        print("Will you be travelling with children?")
        print("  1) Yes")
        print("  2) No")
        kid_friendly = int(input("> "))

        if kid_friendly > 0 and kid_friendly < 3:
            if kid_friendly == 1:
                kid_friendly = True
                break
            elif kid_friendly == 2:
                kid_friendly = False
                break
        else:
            print()
            print("I'm sorry, but " + str(kid_friendly) + " is not a valid choice. Please try again.")
            print()
            continue

    return kid_friendly

def season_choice():
    """Prints season choices and validates user input

    Return:
        list<int>: User input in list form
    """

    SPRING = "Spring"
    SUMMER = "Summer"
    AUTUMN = "Autumn"
    WINTER = "Winter"

    while True:
        list_season = []
        season_status = True

        print("Which seasons do you plan to travel in?")
        print("  1) " + SPRING)
        print("  2) " + SUMMER)
        print("  3) " + AUTUMN)
        print("  4) " + WINTER)
        season = input("> ")

        list_season_int = change_multivalue_input(season)

        for number in list_season_int:
            if number > 0 and number < 5:
                if number == 1:
                    list_season.append(SPRING.lower())
                elif number == 2:
                    list_season.append(SUMMER.lower())
                elif number == 3:
                    list_season.append(AUTUMN.lower())
                elif number == 4:
                    list_season.append(WINTER.lower())

            else:
                print()
                print("I'm sorry, but " + season + " is not a valid choice. Please try again.")
                print()
                season_status = False
                break
        if season_status == False:
            continue
        else:
            break

    return list_season

def climate_choice():
    """Prints climate choices and validates user input

    Return:
        str: User's climate choice
    """

    COLD = "Cold"
    COOL = "Cool"
    MODERATE = "Moderate"
    WARM = "Warm"
    HOT = "Hot"

    while True:
        print("What climate do you prefer?")
        print("  1) " + COLD)
        print("  2) " + COOL)
        print("  3) " + MODERATE)
        print("  4) " + WARM)
        print("  5) " + HOT)
        climate = int(input("> "))

        if climate > 0 and climate < 6:
            if climate == 1:
                climate = COLD.lower()
                break
            elif climate == 2:
                climate = COOL.lower()
                break
            elif climate == 3:
                climate = MODERATE.lower()
                break
            elif climate == 4:
                climate = WARM.lower()
                break
            elif climate == 5:
                climate = HOT.lower()
                break
        else:
            print()
            print("I'm sorry, but " + str(climate) + " is not a valid choice. Please try again.")
            print()
            continue

    return climate


def main():
    # Task 1: Ask questions here
    print("Welcome to Travel Inspiration!")
    print()

    user_name = input("What is your name? ")
    print()

    print("Hi, " + user_name + "!")
    print()

    list_continent = continent_choice()
    print()

    cost = cost_choice()
    print()

    crime = crime_choice()
    print()

    kid_friendly = kid_friendly_choice()
    print()

    list_season = season_choice()
    print()

    climate = climate_choice()
    print()

    print("Now we would like to ask you some questions about your interests, on a scale of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong interest, and 0 indicates indifference.")
    print()

    sports_str = 'sports'
    sports = interest_input(sports_str)
    print()

    wildlife_str = 'wildlife'
    wildlife = interest_input(wildlife_str)
    print()

    nature_str = 'nature'
    nature = interest_input(nature_str)
    print()

    historical_str = 'historical sites'
    historical = interest_input(historical_str)
    print()

    fine_dining_str = 'fine dining'
    fine_dining = interest_input(fine_dining_str)
    print()

    adventure_str = 'adventure activities'
    adventure = interest_input(adventure_str)
    print()

    beach_str = 'the beach'
    beach = interest_input(beach_str)
    print()

    print("Thank you for answering all our questions. Your next travel destination is:")

    destination_list = []

    for destination in Destinations().get_all():
        for continent in list_continent:
            if destination.get_continent() == continent:
                if len(destination.get_cost()) <= len(cost):
                    if destination.get_climate() == climate:
                        if kid_friendly == True:
                            if destination.is_kid_friendly() == kid_friendly:
                                if crime == "high":
                                    if destination.get_crime() == "low" or "average" or crime:
                                        destination_list.append(destination)
                                elif crime == "average":
                                    if destination.get_crime() == "low" or crime:
                                        destination_list.append(destination)
                                elif crime == "low":
                                    if destination.get_crime() == crime:
                                        destination_list.append(destination)
                        elif kid_friendly == False:
                            if destination.is_kid_friendly() == True or destination.is_kid_friendly() == False:
                                if crime == "high":
                                    if destination.get_crime() == "low" or "average" or crime:
                                        destination_list.append(destination)
                                elif crime == "average":
                                    if destination.get_crime() == "low" or crime:
                                        destination_list.append(destination)
                                elif crime == "low":
                                    if destination.get_crime() == crime:
                                        destination_list.append(destination)

    if destination_list == []:
        print("None")

    else:
        final_destination = destination_list[0]
        final_destination_season_score = compare_season_score(final_destination, list_season)

        final_destination_score = calculate_score(final_destination, final_destination_season_score, sports, wildlife, nature, historical, fine_dining, adventure, beach)

        for destinations in destination_list:

            destination_season_score = compare_season_score(destinations, list_season)

            destination_score = calculate_score(destinations, destination_season_score, sports, wildlife, nature, historical, fine_dining, adventure, beach)

            if final_destination_score < destination_score:
                final_destination = destinations
                final_destination_score = destination_score

        print(final_destination.get_name())


























if __name__ == "__main__":
    main()
