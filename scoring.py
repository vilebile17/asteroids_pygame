# 1 point per second alive
# 3 points per asteroid killed

from constants import FPS,COIN_SCORE

def total_score(total_frames, kill_count,num_coins):
    alive_score = total_frames // FPS
    kill_score = kill_count * 3
    coin_score = num_coins * COIN_SCORE
    return kill_score + alive_score + coin_score


    

