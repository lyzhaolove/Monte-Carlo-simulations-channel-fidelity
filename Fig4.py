#combin1
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
x = np.linspace(0, 0.2, 21)
y1 = [1.0, 0.999, 0.994, 0.995, 0.991, 0.993, 0.987, 0.979, 0.985, 0.962, 0.96, 0.958, 0.938, 0.936, 0.936, 0.918, 0.918,
      0.918, 0.917, 0.906, 0.902]
y2 = [1.0, 0.998, 1.0, 0.992, 0.995, 0.995, 0.985, 0.982, 0.983, 0.982, 0.978, 0.968, 0.97, 0.957, 0.96, 0.956, 0.949,
      0.936, 0.936, 0.936, 0.926]
y3 = [1.000, 0.999, 0.999, 1.000, 0.997, 0.993, 0.988, 0.985, 0.986, 0.979, 0.977, 0.966, 0.961, 0.957, 0.940, 0.949,
      0.937, 0.941, 0.934, 0.921, 0.924]
plt.plot(x, y1, '*-.', label='[[4,1,3;1]],$p_B=0.1p_A$')
plt.plot(x, y2, '^-', label='[[3,1,3;2]],$p_B=0.1p_A$')
plt.plot(x, y3, '8-', label='[5,2,3]+[[5,1,3]], $p_B=0.1p_A$')
plt.xlabel("depolarizing rate $p_A$", fontsize=12)
plt.ylabel("channel fidelity", fontsize=12)
plt.grid(ls='--')
plt.legend()
plt.show()


