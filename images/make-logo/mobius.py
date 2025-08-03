import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数设置
theta = np.linspace(0, 2 * np.pi, 200)
w = np.linspace(-0.3, 0.3, 30)
theta, w = np.meshgrid(theta, w)

# 莫比乌斯环参数方程
R = 1
x = (R + w * np.cos(theta / 2)) * np.cos(theta)
y = (R + w * np.cos(theta / 2)) * np.sin(theta)
z = w * np.sin(theta / 2)

# 创建图形
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 彩色映射
colors = np.sin(theta)
surf = ax.plot_surface(x, y, z, facecolors=plt.cm.viridis((colors + 1) / 2),
                       rstride=1, cstride=1, linewidth=0, antialiased=False)

# 视觉设置
ax.set_box_aspect([1, 1, 0.5])
ax.axis('off')
fig.patch.set_alpha(0.0)

# 保存为矢量图（SVG）
output_path = "images/make-logo/mobius_colored.svg"
plt.savefig(output_path, format='svg', bbox_inches='tight', transparent=True)
plt.close()

output_path
