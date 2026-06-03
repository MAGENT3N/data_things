
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
        "morroco"    :{"elo": 1822 , "one_year_change" : 16},
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
    simulate_group(group_dict)
        
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
    print(prob_of_draw)
                
    
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
        "group_a" : {"mexico" , "south_africa" ,"korea", "czechia"},
        "group_b" : {"canada" ,"bosnia" ," qatar","switzerland"},
        "group_c" : {"brazil","morocco","haiti","scotland"},
        "group_d" : {"usa","paraguay","australia","turkey"},
        "group_e" : {"germany","curacao","ivory_coast","ecudaor"},
        "group_f" : {"netherlands","japan","netherlands","tunisia"},
        "group_g" : {"belgium","egypt","iran","newzealand"},
        "group_h" : {"spain","caboverde","saudi","uruguay"},
        "group_i" : {"france","senegal","iraq","norway"},
        "group_j" : {"argentina","algeria","jordan","austria"},
        "group_k" : {"portugal","congo_dr","uzbekistan","colombia"},
        "group_l" : {"england","croatia","ghana","panama"}
        }
    return groups_dictionary   

def simulate_group(groups_dictionary):
    # Creating a list of all the groups
    group_list = []
    for key in groups_dictionary:
        group_name = groups_dictionary[key]
        group_list.append(group_name)
    #print(group_list)
    # Finding all the pairs of matches that will be playes in a group
    
    pairs = []
    for i in range(len(group_list)):
        for j in range(i + 1 ,len(group_list)):
            if i != j :
                pair = (group_list[i],group_list[j])
                pairs.append(pair)
    print(pairs)
                
        
    
 
    
    

if __name__=="__main__":
    main()
    