import gym
from gym.spaces import Discrete, Box
import random

class WuerfelpokerEnv(gym.Env):
    def __init__(self):
        self.MAX_REROLLS = 3
        self.current_round = 1
        self.saved_dices = []
        # Dice
        # 1 = 9
        # 2 = 10
        # 3 = Jack
        # 4 = Queen
        # 5 = King
        # 6 = Ass
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        self.dice3 = random.randint(1,6)
        self.dice4 = random.randint(1,6)
        self.dice5 = random.randint(1,6)
        
        # every round starts with results of 5 dices
        # Action Space:
        # - reroll 5 dices = 0, 
        # - save dice 0, reroll rest = 1
        # - save dice 1, reroll rest = 2
        # - save dice 2, reroll rest = 3
        # - save dice 3, reroll rest = 4
        # - save dice 4, reroll rest = 5
        # - save dice 0+1, reroll rest = 6
        # - save dice 0+2, reroll rest = 7
        # - save dice 0+3, reroll rest = 8
        # - save dice 0+4, reroll rest = 9
        # - save dice 1+2, reroll rest = 10
        # - save dice 1+3, reroll rest = 11
        # - save dice 1+4, reroll rest = 12
        # - save dice 2+3, reroll rest = 13
        # - save dice 2+4, reroll rest = 14
        # - save dice 3+4, reroll rest = 15
        # - save dice 0+1+2, reroll rest = 16
        # - save dice 0+1+3, reroll rest = 17
        # - save dice 0+1+4, reroll rest = 18
        # - save dice 0+2+3, reroll rest = 19
        # - save dice 0+2+4, reroll rest = 20
        # - save dice 0+3+4, reroll rest = 21
        # - save dice 1+2+3, reroll rest = 22
        # - save dice 1+2+4, reroll rest = 23
        # - save dice 1+3+4, reroll rest = 24
        # - save dice 2+3+4, reroll rest = 25
        # - save dice 0+1+2+3, reroll rest = 26
        # - save dice 0+1+2+4, reroll rest = 27
        # - save dice 0+1+3+4, reroll rest = 28
        # - save dice 0+2+3+4, reroll rest = 29
        # - save dice 1+2+3+4, reroll rest = 30
        # insert 9s into scorecard = 31
        # insert 10s into scorecard = 32
        # insert jacks into scorecard = 33
        # insert queens into scorecard = 34
        # insert kings into scorecard = 35
        # insert asses into scorecard = 36
        # insert streets into scorecard = 37
        # insert full houses into scorecard = 38
        # insert pokers (4 of a kind) into scorecard = 39
        # insert grandes (5 of a kind) into scorecard = 40
        
        
        self.action_space = Discrete(40)
        
        # Observation space:
        # - how many rerolls
        # - current filled scorecard
        # - current dices which are not rerolled
        self.observation_space = None
        
    def step(self, action: int):
        observation = None
        reward = None # currently total points
        done = False
        return observation, reward, done, {}
    
    def reset(self):
        observation = None
        return observation
    
    def close(self):
        pass
    
    def render(self):
        pass