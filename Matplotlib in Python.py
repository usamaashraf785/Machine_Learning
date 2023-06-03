import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

# random Data
x = np.linspace(0,10,1000)

# plot

plt.plot(x, np.cos(x) , label = 'Cosine')
# plt.show()

data = pd.DataFrame([[1,2],
                    [3,4],
                    [7,8],
                    [9.5],
                    [7.6]])
data.plot(kind = 'bar', stacked = True)
# plt.show()


#Seaborn Data Visualization

# import seaborn as sns
#
# sns.set()
#
# data= np.random.multivariate_normal([0,0],[[5.2],[2,2]], size=2000)
# data = pd.DataFrame(data, columns=['x','y'])
# for col in 'xy':
#     sns.kdeplot(data[col], shade=True)









