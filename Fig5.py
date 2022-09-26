#combin2
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
x = np.linspace(0, 0.2, 21)
y1 = [1.0, 0.996, 0.991, 0.991, 0.989, 0.978, 0.974, 0.965, 0.955, 0.945, 0.943, 0.92, 0.9, 0.89, 0.901, 0.893, 0.894,
      0.872, 0.859, 0.84, 0.817]
y2 = [1.0, 0.986, 0.984, 0.983, 0.964, 0.959, 0.948, 0.955, 0.936, 0.924, 0.906, 0.903, 0.898, 0.891, 0.887, 0.868, 0.883,
      0.842, 0.817, 0.836, 0.81]
y3 = [1.000, 1.000, 0.998, 0.996, 0.992, 0.992, 0.986, 0.977, 0.978, 0.980, 0.964, 0.952, 0.958, 0.938, 0.938, 0.929,
      0.916, 0.902, 0.894, 0.867, 0.871]
plt.plot(x, y1, '*-.', label='[[4,1,3;1]],$p_B=0.5p_A$')
plt.plot(x, y2, '^-', label='[[3,1,3;2]],$p_B=0.5p_A$')
plt.plot(x, y3, '8-', label='[5,2,3]+[[5,1,3]],$p_B=0.5p_A$')
plt.xlabel("depolarizing rate $p_A$", fontsize=12)
plt.ylabel("channel fidelity", fontsize=12)
plt.grid(ls='--')
plt.legend()
plt.show()
