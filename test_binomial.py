import numpy as np
import matplotlib.pyplot as plt
import random

def simpmarket(win_rate, play_cnt=1000, stock_num=9, position=0.01, commission=0.01, lever=False):
    my_money = np.zeros(play_cnt)
    my_money[0] = 1000
    lose_count = 1
    binomial = np.random.binomial(stock_num, win_rate, play_cnt)
    for i in range(1, play_cnt):
        if my_money[i-1] * position * lose_count <= my_money[i-1]:
            once_chip = my_money[i-1] * position * lose_count
        else:
            print(my_money[i-1])
            break
        if binomial[i] > stock_num//2:
            my_money[i] = my_money[i-1] + once_chip if lever == False else my_money[i-1] + once_chip * lose_count
            lose_count = 1
        else:
            my_money[i] = my_money[i-1] - once_chip if lever == False else my_money[i-1] - once_chip * lose_count
            lose_count = 1 if lever == False else lose_count + 1 

        my_money[i] -= commission
        if my_money[i] <= 0:
            break
    
    return my_money

def positmanage(play_cnt=1000, stock_num=9, commission=0.01):
    my_money = np.zeros(play_cnt)
    my_money[0] = 1000
    #赢率0.5-1随机
    win_rate = random.uniform(0.5, 1)
    binomial = np.random.binomial(stock_num, win_rate, play_cnt)
    for i in range(1, play_cnt):
        
        once_chip = my_money[i-1] * (win_rate * 1 - (1 - win_rate))/1
        
        if binomial[i] > stock_num//2:
            my_money[i] = my_money[i-1] + once_chip
            lose_count = 1
        else:
            my_money[i] = my_money[i-1] - once_chip

        my_money[i] -= commission
        if my_money[i] <= 0:
            break

    return my_money

if __name__ == "__main__":
    print("test")
    trader = 50
    
    #_ = [plt.plot(np.arange(1000), simpmarket(0.5, play_cnt=1000, stock_num=9, commission=0)) for _ in np.arange(0, trader)]
    #_ = plt.hist([simpmarket(0.5, play_cnt=1000, stock_num=9, commission=0)[-1] for _ in np.arange(0, trader)], bins=30)
    
    #_ = [plt.plot(np.arange(100000), simpmarket(0.5, play_cnt=100000, stock_num=9, commission=0.01)) for _ in np.arange(0, trader)]
    #_ = plt.hist([simpmarket(0.5, play_cnt=500000, stock_num=9, commission=0.01)[-1] for _ in np.arange(0, trader)], bins=30)
    
    #_ = [plt.plot(np.arange(1000), simpmarket(0.5, play_cnt=1000, stock_num=9, commission=0.01, lever=True)) for _ in np.arange(0, trader)]
    #_ = plt.hist([simpmarket(0.5, play_cnt=1000, stock_num=9, commission=0.01, lever=True)[-1] for _ in np.arange(0, trader)], bins=30)
    
    _ = [plt.plot(np.arange(50), positmanage(play_cnt=50, stock_num=9, commission=0.01)) for _ in np.arange(0, trader)]
    #_ = plt.hist([positmanage(play_cnt=50, stock_num=9, commission=0.01)[-1] for _ in np.arange(0, trader)], bins=30)
    
    