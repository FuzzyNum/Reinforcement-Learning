Implementation of Q-Learning Solution for Blackjack:

Blackjack Example Results:
<img width="1199" alt="Screenshot 2024-04-17 at 8 49 20 PM" src="https://github.com/FuzzyNum/BlackJackQLearning/assets/96802442/1c980c35-1ade-4814-8c41-d3832ae2dbfb">

Blackjack is a relatively simple game with small observation and action space. The agent can Hit or Stay, implying they acquire another card. 
Rewards are derived from victory/loss over the dealer, and observations include the dealer’s visible card, the agent’s hand, and whether the agent’s hand contains a “usable” ace (counts as 11 without busting).

Implementation of Q-Learning Solution for Gymnasium Taxi:

Taxi Example Results:
<img width="889" alt="Screenshot 2024-04-24 at 10 21 37 AM" src="https://github.com/FuzzyNum/Reinforcement-Learning/assets/96802442/6e88bbd0-7f77-4892-8c82-2fb63ac7a0e3">

Taxi is a Gymnasium environment in which the taxi agent must drop off the passenger at one of four locations. 
"The player receives positive rewards for successfully dropping-off the passenger at the correct location. Negative rewards for incorrect attempts to pick-up/drop-off passenger and for each step where another reward is not received."
Actions include movement in all four directions, in addition to picking up and dropping off the passenger.


