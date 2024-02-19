import matplotlib.pyplot as plt

x = [2, 4, 5, 6]
y = [2, 3, 6, 7]

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)

# x2 = [1, 2, 3, 4]
# y2 = [1, 2, 3, 4]

plt.ylim(1, 8)
plt.xlim(1, 8)

# plt.plot(x2, y2, label = 'line 2')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Two Lines')

# plt.legend()

plt.show()