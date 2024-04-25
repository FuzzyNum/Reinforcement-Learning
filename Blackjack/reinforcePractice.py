import gymnasium as gym
import numpy as np
import seaborn
from tqdm import tqdm #progress bar

from collections import defaultdict
import matplotlib.pyplot as plt #drawing plots
from matplotlib.patches import Patch #draw shapes
from IPython.display import clear_output

env=gym.make("Blackjack-v1", sab=True, render_mode="rgb_array")
#Observing the environment

#Resetting env to get first observation.
done=False
observation, info=env.reset()
#3-tuple consisting of our current sum, dealer's visible card, and whether there is a usable ace (11) without busting.

#sample action
action =env.action_space.sample()
observation,reward,terminated,truncated,info =env.step(action)

class BlackJackAgent:
    def __init__(self, learning_rate:float,initial_epsilon:float,epsilon_decay:float,final_epsilon:float,discount_factor:float = 0.95):
        #Initialize RL agent with empty dictionary of state-action values, learning rate, epsilon.
        #discount_factor: the discount factor for computing the Q-value.
        self.q_values= defaultdict(lambda:np.zeros(env.action_space.n))
        self.lr=learning_rate
        self.discount_factor=discount_factor
        self.epsilon=initial_epsilon
        self.epsilon_decay=epsilon_decay
        self.final_epsilon=final_epsilon
        self.training_error=[]

    def get_action(self,obs:tuple[int,int,bool])->int:
        #Returns the best action with probability of epsilon, accounting for Explore-Exploit.
        if np.random.random()<self.epsilon:
            return self.env.action_space.sample()
        else:
            return int(np.argmax(self.q_values[obs]))
    
    def update(self, obs:tuple[int,int,bool], action:int, reward:float, termianted:bool, next_obs:tuple[int,int,bool])->int:
        """ Updates the Q-Value of a function."""
        future_q_value= (not terminated)* np.max(self.q_values[next_obs])
        temporal_difference= (reward+self.discount_factor*future_q_value - self.q_values[obs][action])
        self.q_values[obs][action]=(self.q_values[obs][action]+self.lr*temporal_difference)
        self.training_error.append(temporal_difference)

    def decay_epsilon(self):
        self.epsilon = max(self.final_epsilon, self.epsilon-self.epsilon_decay)
    

learning_rate=0.01
n_episodes=10000
start_epsilon=1.0
epsilon_decay= start_epsilon/(n_episodes/2)
final_epsilon=0.1

agent = BlackJackAgent(
    learning_rate=learning_rate,
    initial_epsilon=start_epsilon,
    epsilon_decay=epsilon_decay,
    final_epsilon=final_epsilon
)

env= gym.wrappers.RecordEpisodeStatistics(env, deque_size=n_episodes)
for episode in tqdm(range(n_episodes)):
    obs,info=env.reset()
    done=False
    clear_output()

    while not done:
        action= agent.get_action(obs)
        next_obs, reward, terminated, truncated, info= env.step(action)

        agent.update(obs, action, reward, terminated, next_obs)
        done=terminated or truncated
        obs=next_obs
    agent.decay_epsilon()

rolling_length=500
fig, axs= plt.subplots(ncols=3, figsize=(12,5))
axs[0].set_title("Episode rewards")
reward_moving_average=(np.convolve(np.array(env.return_queue).flatten(), np.ones(rolling_length), mode="same")/rolling_length)
axs[0].plot(range(len(reward_moving_average)), reward_moving_average)
axs[1].set_title("Episode Lengths")
length_moving_average=(np.convolve(np.array(env.length_queue).flatten(), np.ones(rolling_length), mode="same")/rolling_length)
axs[1].plot(range(len(length_moving_average)),length_moving_average)
training_error_moving_average=(np.convolve(np.array(agent.training_error).flatten(), np.ones(rolling_length), mode="same")/rolling_length)
axs[2].plot(range(len(training_error_moving_average)), training_error_moving_average)
plt.tight_layout()
plt.show()









