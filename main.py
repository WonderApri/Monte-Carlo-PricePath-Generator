import numpy as np

S_value = 100        #price of asset in GBP
mu = 0.05            #annual drift (return expected)
sigma = 0.2          #annual volatility
T = 1.0              #total time in yrs
steps = 252          #steps in simulation (days in year when market open- trading year)
paths = 10000        #no. of independent price paths to simulate

dt = T / steps           
Z = np.random.normal(0,1, (paths, steps))   #produces matrix 
#each row of matrix is one price path's random noises

S = np.zeros((paths, steps + 1))
S[:, 0] = S_value

