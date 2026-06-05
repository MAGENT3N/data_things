
import random
import math

# Global variable containing the country,elo , and year change in elo
# .... as a dictionary data structure
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
def main():
    
    # one_year_elo = accessing_one_year_change()
    # print(one_year_elo)
    # results = []
    # for i in range(10):
    #     result = simulate_match("curacao", "argentina")
    #     results.append(result)
    # print(results)
    # print(create_groups())
    group_dict = create_groups()
    qual_teams,points = simulate_group(group_dict,"group_a")
    print(qual_teams,points)
    round_of_32()
    round_of_16()


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
"""
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
    elif prob_of_team_a + prob_of_draw <= random_num < 1:
        loss = team_b
        return loss

def create_groups():
    groups_dictionary = {
        "group_a" : ["mexico" , "south_africa" ,"korea", "czechia"],
        "group_b" : ["canada" ,"bosnia" ,"qatar","switzerland"],
        "group_c" : ["brazil","morocco","haiti","scotland"],
        "group_d" : ["usa","paraguay","australia","turkey"],
        "group_e" : ["germany","curacao","ivory_coast","ecuador"],
        "group_f" : ["netherlands","japan","netherlands","tunisia"],
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
    Function for creating playoffs against the winners of the group stage and
    returning the teams which pass two the round of 16
"""
def round_of_32():
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
    # Shuffling the teams in random order
    random.shuffle(teams_in_round_32)
    print(teams_in_round_32)
    # Creating a tuple for teams that will play against each other
    #... one takes the slices at odd indices other at even and then we zip
    paired_list = list(zip(teams_in_round_32[0::2],teams_in_round_32[1::2]))
    print(paired_list)
    # playing the teams against each other if the match results in a draw
    #... we are choosing one of the two teams randomly
    round_of_16_teams = []
    for pairs in paired_list:
        team_a,team_b = pairs
        result = simulate_match(team_a, team_b)
        if result == "draw":
            rand_num = random.randint(1,2)
            if rand_num == 1:
                result = team_a
            else :
                result = team_b
        round_of_16_teams.append(result)
    print(round_of_16_teams)
    return round_of_16_teams
"""
    Function for simulating the round of 16
"""
def round_of_16():
    # Getting the teams playing the round of 16
    teams_in_16 = round_of_32()
    quarter_final_teams = knockout(teams_in_16)
    # Shuffling the teams
    # random.shuffle(teams_in_16)
    # # Making pairs
    # paired_list = list(zip(teams_in_16[0::2],teams_in_16[1::2]))
    # quarter_final_teams = []
    # for pairs in paired_list:
    #     team_a , team_b = pairs
    #     result = simulate_match(team_a, team_b)
    #     if result == "draw":
    #         rand_num = random.randint(1,2)
    #         if rand_num == 1 :
    #             result = team_a
    #         else:
    #             result = team_b
    #     quarter_final_teams.append(result)
    # print(quarter_final_teams)
    return quarter_final_teams
def knockout(list_of_teams):
    random.shuffle(list_of_teams)
    paired_list = list(zip(list_of_teams[0::2],list_of_teams[1::2]))
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

# def round_of_16():
#     teams_playing = team

       
        

            
    # print(teams)
    
                
        
    
 
    
    

if __name__=="__main__":
    main()
    