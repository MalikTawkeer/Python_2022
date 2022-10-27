#all about matplot
import matplotlib.pyplot as plt
import numpy as np
#diplaying version
#print(matplotlib.__version__)

#draw a line diagram from position (0,0) to position (6,250)
xpoints = np.array([0,6])
ypoints = np.array([0,250])
plt.plot(xpoints,ypoints)
plt.show()