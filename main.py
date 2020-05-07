# When '%pylab or % pylab inline' is not working

# Instead of matplotlib inline
import matplotlib.pyplot as pl
try:
  get_ipython().magic("matplotlib inline")
except:
  pl.ion()
import numpy as np

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
pl.plot(x,y)

# Create the figure object
fig = pl.figure(figsize=(12,8))




# Add first axes object (of a multi-panel plot with two rows and one column)
ax = fig.add_subplot(211)
pl.plot(x, np.sin(x))
pl.title("The Sinus Function")
pl.xlabel("This is my x-axis label")

#Add second axes object
ax = fig.add_subplot(212)
pl.plot(x, np.cos(x))
pl.title("The Cosinus Function")
pl.xlabel("This is my x-axis label")

# Make sure he elements of the plot are arranged properly
pl.tight_layout()
