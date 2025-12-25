import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

import gymnasium as gym
env = gym.make("LunarLander-v3", render_mode="human")
observation, info = env.reset()
x = observation[0]
y = observation[1]
vx = observation[2]
vy = observation[3]
angle =observation[4]
print("Initial Observation:", observation)
run = True
total_reward = 0
while(run):
    if vy<-0.25 :
        action = 2 
    elif angle>0.03 :
        action = 1
    elif angle<-0.03 :
        action = 3 
    elif x< -0.1 or vx<-0.25:
        action = 1 
    elif x> 0.1 or vx>0.25:
        action = 3  
    if y< 0.8 and vy<-0.15:
        action = 2 
    else :    
        action = 0  

    observation, reward, terminated, truncated, info = env.step(action)
    x = observation[0]
    y = observation[1]
    vx = observation[2]
    vy = observation[3]
    angle = observation[4]
    total_reward += reward
    if terminated or truncated:
        observation, info = env.reset()
        run = False

print("Total Reward:", total_reward)
env.close()

