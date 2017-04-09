import matplotlib.pyplot as plt
import vibration_toolbox as vtb
vtb.free_response()[1][:5] # get the first five values of x
# array([[ 1.        ],
# [ 0.99591926],
# [ 0.9916807 ],
# [ 0.98728508],
# [ 0.98273317]])
t, x, *_ = vtb.free_response() # *_ ignores all other returns
plt.plot(t,x)
