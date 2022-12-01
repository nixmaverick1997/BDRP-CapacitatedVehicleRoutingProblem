import gym
from gym import spaces
#insert replacement for or_gym

import random
import numpy as np

class CVRP(gym.Env):
    """
    Capacitated Vehicle Routing Problem
    

    Observation:
        Type: Box
        State Vector: S = (l_0, l_i, l_t, q_i_t, Q_t)
        l_o = Location of depot i.e. node 0
        l_i =  location of each customer i
        l_t = location of truck at time t
        q_i_t = current demand of the customer i at time t
        Q_t = current capacity of truck at time t
        
    Action:
        Type: Discrete
        0 = Go to depot i.e. node 0
        n = Go to node n
        
        Action masking is available for this environment. Set mask=True
        in the env_config dictionary
        
    
    
    """