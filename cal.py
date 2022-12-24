import numpy as np
import gym
import random

def main(learning_rate,discount_rate,convergence_criteria):

    # create Taxi environment
    env = gym.make('Taxi-v3',render_mode="ansi")
    # initialize q-table
    state_size = env.observation_space.n
    action_size = env.action_space.n
    qtable = np.zeros((state_size, action_size))

    # hyperparameters
    # learning_rate = 0.5
    # discount_rate = 0.6
    epsilon = 1.0
    decay_rate= 0.005

    # training variables
    num_episodes = 1000
    max_steps = 99 # per episode
    # convergence_criteria=0.000000000001
    # training
    for episode in range(num_episodes):
        # reset the environment
        state = env.reset()[0]

        done = False
        maxDifForEpisode=0
        for s in range(max_steps):

            # exploration-exploitation tradeoff
            if random.uniform(0,1) < epsilon:
                # explore
                action = env.action_space.sample()
            else:
                # exploit
                action = np.argmax(qtable[state,:])

            # take action and observe reward
            new_state, reward, done, info = env.step(action)[:4]
            # Q-learning algorithm
            diff=learning_rate * (reward + discount_rate * np.max(qtable[new_state,:])-qtable[state,action])
            qtable[state,action] = qtable[state,action] + diff
            if (diff<0):
                diff=-diff
            maxDifForEpisode=max(maxDifForEpisode,diff)
            

            # Update to our new state
            state = new_state

            # if done, finish episode
            if done == True:
                break

        # Decrease epsilon
        epsilon = np.exp(-decay_rate*episode)
        if (maxDifForEpisode<convergence_criteria):
            # print(maxDifForEpisode)
            return episode+1
    return episode+1
    # print(f"Training completed over {episode+1} episodes")
    # input("Press Enter to watch trained agent...")

    # # watch trained agent
    # state = env.reset()[0]
    # done = False
    # rewards = 0
    # for s in range(max_steps):
    #     print(f"TRAINED AGENT")
    #     print("Step {}".format(s+1))

    #     action = np.argmax(qtable[state,:])
    #     new_state, reward, done, info = env.step(action)[:4]
    #     rewards += reward
    #     env.render()
    #     print(f"score: {rewards}")
    #     state = new_state

    #     if done == True:
    #         break
    env.close()
    