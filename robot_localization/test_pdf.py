import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
 
mu, sigma = 0, 0.33  # Mean and standard deviation
# x = np.linspace(0, 1, 1000)
pdf = norm.rvs(mu, sigma, 1000)
 
plt.hist(pdf, label='Distribuzione Normale')
plt.title('PDF of the Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()
plt.show()