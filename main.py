import numpy as np

S_value = 100        #price of asset in GBP
mu = 0.05            #annual drift (return expected)
sigma = 0.2          #annual volatility
T = 1.0              #total time in yrs
steps = 252          #steps in simulation (days in year when market open- trading year)
paths = 10000        #no. of independent price paths to simulate


