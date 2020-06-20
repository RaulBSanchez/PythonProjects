import matplotlib.pyplot as plt

sqaures = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('seaborn')

#fig represents the entire figure or collection of plots that are generated
# ax represents a single plot in the figure
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

#ax.plot(input_values, sqaures, linewidth =3)


# set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Square of Value," ,fontsize = 14)

#set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()