# Function :-
Run a monte carlo simulation of the 2026 fifa world cup based on the ELO ratings and the change in the one year elo ratings of the countries in the fifa world cup.
**Main approach**:-
- Create data structure with elo data and country name
- Create data structure for all the groups
- Create a function for simulating a single match between team A and team B
- Select the individual combinations of teams in a group and simulate the matches and advance the top 2 teams to the next stage and ranking the
  the third team of each group and selecting the top 8 teams out of them for the round of 32
- Update the elo ratings based on the matches played , now the new elo ratings of the teams are the update elo ratings after playing the matches
- Repeat this process for the next stages like round of 16 , quarter , semi and finals
Run this block a thousand times and see the results.

## Mathematical concepts learned-
- 1) Min-Max normalization- Normalizing the data points using min max like subtracting the min from the point and dividing it by max-min but is it really necessary in this case or can I use a fraction? Plus it does not reflect the drops in the elo ratings so that is a problem.
- 2) Elo ratings - This is the heart of the simulation specifically the formula that eduardo wrote on the window of the dorm room.
  $$E_A = \frac{1}{1 + 10^{(R_B - R_A) / 400}}$$
  and the rating update formula :-
  $$R'_A = R_A + K(S_A - E_A)$$
  Rb is the rating of b , Ra is the rating of A and Ea is the prob of A winning

- 3) Logistic function - The elo rating is itself based on the logistic function ,the core logic being,
  if two teams are closely matched we want the probability to be 50 50 , mathematicall, the range of the function should be between 0 to 1 and the function should be strictly increasing.
  This logic can also be used for estimating the draw probability,if two teams are evenly matched the probability of the match ending in a draw is higher.

- 4) Modelling the draw probability - This turned out to be a problem. Like if we dynamically fix the draw probability to 0.25 then it is easy but I wanted to account for the difference in elo ratings of the teams. After doing mental gymnastics and bouncing ideas off of claude I used a complicated looking logistics regression formula which didnt work so in the end I just used the difference mapped to a decaying exponenetial which was my initial idea.
  ```python
	  prob_of_draw = 0.10 + 0.20 * math.exp(-elo_diff / 200)
	  # IF teams are equally matched elo diff = 0 which implies
	  #... prob of draw = 0.30(higher than 0.25) else on the other extreme
	  #... it is 0.10
  ```
