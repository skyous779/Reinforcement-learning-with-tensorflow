"""
A simple example for Reinforcement Learning using table lookup Q-learning method.
An agent "o" is on the left of a 1 dimensional world, the treasure is on the rightmost location.
Run this program and to see how the agent will improve its strategy of finding the treasure.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

import numpy as np
import pandas as pd
import time

<<<<<<< HEAD
np.random.seed(2)  # reproducible   生成一样的随机数
=======
np.random.seed(2)  # reproducible
>>>>>>> 925f044b7cadb8d60e86e29c4b636d30eb059729


N_STATES = 6   # the length of the 1 dimensional world
ACTIONS = ['left', 'right']     # available actions
EPSILON = 0.9   # greedy police
ALPHA = 0.1     # learning rate
GAMMA = 0.9    # discount factor
MAX_EPISODES = 13   # maximum episodes
<<<<<<< HEAD
FRESH_TIME = 0.1    # fresh time for one move


def build_q_table(n_states, actions):
    table = pd.DataFrame(                                    #pandas用法
        np.zeros((n_states, len(actions))),     # q_table initial values
        columns=actions,    # actions's name
    )
    #print(table)    # show table
=======
FRESH_TIME = 0.3    # fresh time for one move


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table initial values
        columns=actions,    # actions's name
    )
    # print(table)    # show table
>>>>>>> 925f044b7cadb8d60e86e29c4b636d30eb059729
    return table


def choose_action(state, q_table):
    # This is how to choose an action
    state_actions = q_table.iloc[state, :]
    if (np.random.uniform() > EPSILON) or ((state_actions == 0).all()):  # act non-greedy or state-action have no value
        action_name = np.random.choice(ACTIONS)
    else:   # act greedy
        action_name = state_actions.idxmax()    # replace argmax to idxmax as argmax means a different function in newer version of pandas
    return action_name


def get_env_feedback(S, A):
    # This is how agent will interact with the environment
    if A == 'right':    # move right
        if S == N_STATES - 2:   # terminate
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:   # move left
        R = 0
        if S == 0:
            S_ = S  # reach the wall
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    # main part of RL loop
<<<<<<< HEAD
    q_table = build_q_table(N_STATES, ACTIONS)    #建立一个Q-table
    for episode in range(MAX_EPISODES):          #每个回合
        step_counter = 0                        #用于计步
        S = 0                                   #第0步
        is_terminated = False                   #终止标志
        update_env(S, episode, step_counter)     #环境初始化？还是更新？       
        while not is_terminated:    

            A = choose_action(S, q_table)          #选一个动作：左还是右
            S_, R = get_env_feedback(S, A)  # take action & get next state and reward     得到下一个S_和奖励值R
            q_predict = q_table.loc[S, A]               #定位出当前的Q表的值
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   # next state is not terminal       公式得出目标值
            else:
                q_target = R     # next state is terminal                
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  # update更新Q表
=======
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:

            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A)  # take action & get next state and reward
            q_predict = q_table.loc[S, A]
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   # next state is not terminal
            else:
                q_target = R     # next state is terminal
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  # update
>>>>>>> 925f044b7cadb8d60e86e29c4b636d30eb059729
            S = S_  # move to next state

            update_env(S, episode, step_counter+1)
            step_counter += 1
<<<<<<< HEAD
        #print(q_table)    
=======
>>>>>>> 925f044b7cadb8d60e86e29c4b636d30eb059729
    return q_table


if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)
