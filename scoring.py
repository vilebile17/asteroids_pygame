# 1 point per second alive
# 3 points per asteroid killed

from constants import FPS

def total_score(total_frames, kill_count):
    alive_score = total_frames // FPS
    kill_score = kill_count * 3
    return kill_score + alive_score


    

