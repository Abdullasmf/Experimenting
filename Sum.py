import numpy as np
from multiprocessing import Process
import os
c=5+6+7+8+9
#this is master
#this is in the branch
def get_sum(a: np.array, b: np.array):
    return a+b