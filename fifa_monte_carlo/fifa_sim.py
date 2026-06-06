
import random
import math
import matplotlib.pyplot as plt

# Global variable containing the country,elo , and year change in elo
# .... as a dictionary data structure
"""
  TO DO - Add update elo functionality after every match that is dynamic
  elo values
"""
elo_ratings_dict = {
        "canada" : {"elo" : 1784 ,"one_year_change" : 6},
        "usa"    : {"elo" : 1733 , "one_year_change" : 11},
        "mexico" : {"elo" : 1868 , "one_year_change" : 51},
        "algeria": {"elo" : 1743 , "one_year_change" : 35},
        "argentina" : {"elo": 2113 , "one_year_change" : -28},
        "australia" : {"elo" : 1775 , "one_year_change" : 38},
        "austria"  : {"elo" : 1827 ,"one_year_change" : -10},
        "belgium" : {"elo" : 1867 , "one_year_change" : 23},
        "bosnia" : {"elo" : 1591  , "one_year_change" : 65},
        "brazil" : {"elo" : 1988 , "one_year_change" : -5},
        "caboverde" : {"elo" : 1576 , "one_year_change" : 76},
        "colombia"  : {"elo" : 1975 , "one_year_change" : 24},
        "congo_dr"  : {"elo" : 1655 , "one_year_change" : 89},
        "ivory_coast" : {"elo" : 1676 , "one_year_change": 85},
        "croatia"   : {"elo" :1930 , "one_year_change": 19},
        "curacao": {"elo" : 1433 , "one_year_change" : 110},
        "czechia" : {"elo" : 1733 , "one_year_change" : -22},
        "ecuador" : {"elo": 1953  , "one_year_change" : 24},
        "egypt"   : {"elo" : 1699 , "one_year_change" : 33},
        "england" : {"elo" : 2020 , "one_year_change" : 9},
        "france"  :{"elo" : 2081  , "one_year_change" : 51},
        "germany" :{"elo" : 1925  , "one_year_change" : -62},
        "ghana"   :{"elo" : 1503 , "one_year_change" : 26},
        "haiti"   :{"elo": 1532 , "one_year_change" : -21},
        "iran"     :{"elo": 1764 , "one_year_change" : -66},
        "iraq"     :{"elo": 1608 , "one_year_change" : 69},
        "japan"    :{"elo": 1906 , "one_year_change" : -30},
        "jordan"   :{"elo": 1685 , "one_year_change" : 66},
        "korea"   :{"elo": 1756 , "one_year_change" : 10},
        "morocco"    :{"elo": 1822 , "one_year_change" : 16},
        "netherlands" :{"elo": 1961 , "one_year_change" : -5},
        "newzealand"  :{"elo": 1585 , "one_year_change" : -10},
        "norway"   :{"elo": 1912, "one_year_change" : 83},
        "panama"   :{"elo": 1733 , "one_year_change" : 10},
        "paraguay"  :{"elo": 1833 , "one_year_change" : 33},
        "portugal"  :{"elo": 1984 , "one_year_change" : -4},
        "qatar"  :{"elo": 1423 , "one_year_change" : -75},
        "saudi"   :{"elo": 1566 , "one_year_change" : -10},
        "scotland"  :{"elo": 1770 , "one_year_change" : 28},
        "senegal"   :{"elo": 1866 , "one_year_change" : 107},
        "south_africa"   :{"elo": 1517 , "one_year_change" : -81},
        "spain"  :{"elo": 2165, "one_year_change" : 15},
        "sweden"  :{"elo": 1719 , "one_year_change" : -17},
        "switzerland"  :{"elo": 1894 , "one_year_change" : 82},
        "tunisia"  :{"elo": 1636 , "one_year_change" : 25},
        "turkey"  :{"elo": 1902 , "one_year_change" : 65},
        "uruguay"  :{"elo": 1892 , "one_year_change" : -29},
        "uzbekistan"  :{"elo": 1727 , "one_year_change" : 30},
        }

"""
    Main description : The program uses the global dictionary which contains
    the data on which the  simulations  run.
    
    Basic Flow of the program:
    1)Create a dictionary containing the groups from the global data dictionary
    
    2)Play the teams in each group against each other so that every team plays
      each other at leat once using simulate match logic
      
    3)Using the results create a list of teams that will go to the round of 32
    
    4)Simulate Round of 32 ,16,quarters,semi and then the final
    
    5)Create a dictionary in main for keeping count of the number of times a 
     country wins the world cup for a iteration and divide the count values to 
     the total number of iterations to get win probability
     
    6)Plot the histograms of the top 10 countries with the highest probabilites
      and their probability of winning after accounting for all iterations
     
    
"""
def main():
    iterations = int(input("Enter the number of iterations for the simulation: "))
    result_tracker = result_dictionary()
    for i in range(iterations):
        winner = simulate_tournament()
        # Dictionary expects a string not a list so winner[0]
        result_tracker[winner[0]] += 1
    # changing the values to the probability of winning the tournament
    result_tracker = {k:v/iterations for k,v in result_tracker.items()}
    sorted_dict = dict(sorted(result_tracker.items() , key=lambda item:item[1],reverse = True))
    for key,value in sorted_dict.items():
        print(f"{key}: win probability after {iterations} iterations = {value}")
    plot_data(sorted_dict)

"""
    Description- Function for simulating a match between two teams on the basis
    of their elo ratings. We use the basic formula for calculating the probability
    of Player A winning against Player B based on their elo rating.
    We also use the probability of the teams resulting in a draw based on their elo
    rating rather than hardcoding 0.25 ,ie, if elo ratings are equal ,probability of draw
    is very high and if different then the probabiliyt of a draw is very low
    
    Parameters - Name of the teams as a string that are stored in the dictionary
    
    Returns - The name of the team that wins or if a draw then draw
"""

def simulate_match(team_a , team_b):



    ## Checking logic with two teams
    base_elo_a = elo_ratings_dict[team_a]["elo"]
    base_elo_b = elo_ratings_dict[team_b]["elo"]
    
    # Form integration: We treat 50% of the one-year change as a "momentum modifier" 
    # to find a middle ground between long-term skill and current hot/cold streaks.
    elo_rating_team_a = base_elo_a + (elo_ratings_dict[team_a]["one_year_change"] * 0.5)
    elo_rating_team_b = base_elo_b + (elo_ratings_dict[team_b]["one_year_change"] * 0.5)
    # Match logic based on elo ratings and one year change
    random_num = 0
    # Probability of team_a winning based on their elo ratings
    prob_of_team_a =round( 1/(1 + (10**((elo_rating_team_b - elo_rating_team_a)/400) )),4)
    # Probability of team_b winning based on their elo ratings
    prob_of_team_b = round(1/(1 + (10**((elo_rating_team_a - elo_rating_team_b)/400) )),4)
    # Calculating the draw probability based on the difference in the elo ratings of the teams
    elo_diff = abs(elo_rating_team_a - elo_rating_team_b)
    # Using a decaying exponential instead of logistic regression
    prob_of_draw = 0.10 + 0.20 * math.exp(-elo_diff / 200)
    # Accounting for the probability of draw based on the elo difference so we have to scale
    #... the probability of the team winning with the factor of 1 - prob_of_draw
    scale = 1 - prob_of_draw
    prob_of_team_b = round(prob_of_team_b * scale , 4)
    prob_of_team_a = round(prob_of_team_a * scale , 4)
                
    
    # Game result logic
    random_num = round(random.random(),4)
    if 0 <= random_num <= prob_of_team_a:
        win = team_a
        return win
    elif prob_of_team_a <= random_num <= prob_of_team_a + prob_of_draw:
        draw = "draw"
        return draw
    elif prob_of_team_a + prob_of_draw <= random_num <= 1:
        loss = team_b
        return loss

def create_groups():
    groups_dictionary = {
        "group_a" : ["mexico" , "south_africa" ,"korea", "czechia"],
        "group_b" : ["canada" ,"bosnia" ,"qatar","switzerland"],
        "group_c" : ["brazil","morocco","haiti","scotland"],
        "group_d" : ["usa","paraguay","australia","turkey"],
        "group_e" : ["germany","curacao","ivory_coast","ecuador"],
        "group_f" : ["netherlands","japan","sweden","tunisia"],
        "group_g" : ["belgium","egypt","iran","newzealand"],
        "group_h" : ["spain","caboverde","saudi","uruguay"],
        "group_i" : ["france","senegal","iraq","norway"],
        "group_j" : ["argentina","algeria","jordan","austria"],
        "group_k" : ["portugal","congo_dr","uzbekistan","colombia"],
        "group_l" : ["england","croatia","ghana","panama"]
        }
    return groups_dictionary   
"""
    Function for simulating the outcomes of a group playoff
    Parameter: The groups_dictionary and the group_key,ie,the group
    which we want to simulate
    Returns: Returns the list of the teams of the group after the play
    against each other sorted in a descending order on the basis of their
    points AND the a dictionary containing the team with their points
"""
def simulate_group(groups_dictionary , group_key):
    """
        Creating a dictionary for tracking the points
    """
    countries = groups_dictionary[group_key]
    points_dict = {}
    for i in range(len(countries)):
        country = countries[i]
        points_dict[country] = 0
    
    """
        Creating a list for all the matches that will be played
        within a group
    """
    pairs = []
    for i in range(len(countries)):
        # condition for removing double counting plus playing the team
        #... againts itself
        for j in range(i + 1 , len(countries)):
            if i != j:
                pair = (countries[i],countries[j])
                pairs.append(pair)
    # simulating matches
    """
        Simulating all the matches within the group
    """
    results = []
    for i in range(len(pairs)):
        element_at_i = pairs[i]
        # unpacking the tuple
        country1,country2 = element_at_i
        result = simulate_match(country1,country2)
        """
            Check the return lines of simulate_match for reference
        """
        if result == country1:
            points_dict[country1] += 3
        elif result == country2 :
            points_dict[country2] += 3   
            results.append(result)
        elif result == "draw":
            points_dict[country1] += 1
            points_dict[country2] += 1
    # Sorting point_dict to get the top two teams from the group(in descending order)
    sorted_point_dicts = dict(sorted(points_dict.items(),key = lambda item:item[1],reverse=True))
    # Getting the list of the teams and selecting the first and second element
    team_list = list(sorted_point_dicts)
    return team_list,points_dict
"""
    Function for assembling the teams in the round of 32
    Description:
    1)We create the groups by calling the create_groups function.
    2)We add the top two teams of each group to the list of top 24 teams
    3)We create an empty dictionary for storing the values of the bottom
      two teams of each group along with their points
    4)We sort the dictionary containing all the bottom two teams along with
      their points and get the top 8 teams from them.
    5)We add the two lists to get the teams entering the round of 32
    
    Parameters: None
    Returns : A list of teams entering the round of 32
"""
def assemble_round_32_teams():
    group = create_groups()
    top_24 = [] 
    # Dictionary containing the 12 teams who were third in their group
    
    bottom_fraggers = {}
    # Getting the top 2 teams and creating a dictionary for remaining teams
    # Along with their points
    for key in group:
        elem,points = simulate_group(group, key)
        top_24.append(elem[0])
        top_24.append(elem[1])
        bottom_fraggers[elem[2]] = points[elem[2]]
    # Sorting the dictionary on the basis of their points
    sorted_bottom_fraggers = dict(sorted(bottom_fraggers.items(),key = lambda item:item[1],reverse = True))
    sorted_list = list(sorted_bottom_fraggers)
    
    # Getting the top 8 teams of the 12 teams who were not in the top 24
    top_8 = []
    for i in range(8):
        element = sorted_list[i]
        top_8.append(element)
    teams_in_round_32 = top_24 + top_8
    return teams_in_round_32
    
"""
    Function for creating playoffs against the winners of the group stage and
    returning the teams which pass two the round of 16
"""
def round_of_32():

    teams_in_round_32 = assemble_round_32_teams()
    teams_in_16 = knockout(teams_in_round_32)
    return teams_in_16
"""
    Function for simulating the round of 16
"""
def round_of_16(teams_in_16):
    # Getting the teams playing the round of 16
    quarter_final_teams = knockout(teams_in_16)
    return quarter_final_teams

"""
    Function for simulating the quarter finals
"""
def quarter_finals(teams_in_quarters):
    semi_finals_teams = knockout(teams_in_quarters)
    return semi_finals_teams
"""
    Function for simulating the semi-finals
"""
def semi_finals(teams_in_semi):
    teams_in_finals = knockout(teams_in_semi)
    return teams_in_finals
"""
    Function for simulating the finals
"""
def finals(final_teams):
    winner = knockout(final_teams)
    return winner
    
"""
    A helper function for simulating Knockouts after getting the teams
    in the round of 32
    Description:Algorithm
    1) Get the teams entering that round
    2)Shuffle the teams
    3)Pair the shuffled teams
    4)Simulate match between the teams
    4i) If match resulting in a draw choose one team randomly
    5) Return the resulting teams
    Parameter : A list of teams entering that round.
    Returns   : The list of teams that move to  the next round
"""
def knockout(list_of_teams):
    # Shuffling the teams in a random order
    random.shuffle(list_of_teams)
    # Pairing the list by creating one list of odd indices and other
    # ...of even indices and zipping them
    paired_list = list(zip(list_of_teams[0::2],list_of_teams[1::2]))
    # Simulating the matches
    next_round_teams = []
    for pairs in paired_list:
        team_a,team_b = pairs
        result = simulate_match(team_a, team_b)
        if result == "draw":
            rand_num = random.randint(1,2)
            if rand_num == 1:
                result = team_a
            else :
                result = team_b
        next_round_teams.append(result)
    return next_round_teams
"""
    Function for simulating the tournament by combining our functions
"""
def simulate_tournament():
    teams_in_16 = round_of_32()
    teams_in_quarters = round_of_16(teams_in_16)
    teams_in_semis = quarter_finals(teams_in_quarters)
    teams_in_finals = semi_finals(teams_in_semis)
    winner = finals(teams_in_finals)
    return winner
"""
    Function for creating a result dictionary which tracks the number
    of wins of a country for the total number of iterations for which we
    run the simulation
"""
def result_dictionary():
    result_dict = {key: 0 for key in elo_ratings_dict}
    return result_dict
"""
    Function for plotting historgram of win probabilities of the top 10
    teams
    Paramter : We will give to it the sorted result dictionary
    Output : Plots the histogram of the win probabilities of the 15 teams?
"""
def plot_data(sorted_result_dictionary):
    # get the probabilites of the top 10 arrays
    top_10_teams = list(sorted_result_dictionary.keys())[:10]
    top_10_probs = list(sorted_result_dictionary.values())[:10]
    plt.figure()
    plt.bar(top_10_teams,top_10_probs,color = 'red')
    plt.title('Probability of the teams winning ')
    plt.xlabel('Name of the teams')
    plt.ylabel('Probability of winning')
    plt.show()
    
               
            
        
    
if __name__=="__main__":
    main()
    