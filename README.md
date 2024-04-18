Implementation of Q-Learning Solution for Blackjack

Example Results:
<img width="1199" alt="Screenshot 2024-04-17 at 8 49 20 PM" src="https://github.com/FuzzyNum/BlackJackQLearning/assets/96802442/1c980c35-1ade-4814-8c41-d3832ae2dbfb">

Just me messing around with reinforcement learning to better understand Q-learning.

Blackjack is a relatively simple game with small observation and action space. The agent can Hit or Stay, implying they acquire another card. 
Rewards are derived from victory/loss over the dealer, and observations include the dealer’s visible card, the agent’s hand, and whether the agent’s hand contains a “usable” ace (counts as 11 without busting).

