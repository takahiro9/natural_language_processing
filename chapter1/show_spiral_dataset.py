import sys
sys.path.append('..')
from dataset import spiral
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure()
x, t = spiral.load_data()