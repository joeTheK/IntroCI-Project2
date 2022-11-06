# Joseph Kelley
# Graphs the relations in Iris dataset. Used to analytically come up
# with ruleset for iris fis

from sklearn import datasets
import matplotlib.pyplot as plt

#The rows being the x_petalLen and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.
iris = datasets.load_iris()

sepalLen_data = iris.data[:, 0]
sepalWid_data = iris.data[:, 1]
petalLen_data = iris.data[:, 2]
petalWid_data = iris.data[:, 3]

dataToPlot = [sepalLen_data, sepalWid_data, petalLen_data, petalWid_data]
axisLabels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
classData = iris.target
irisNames = ["Setosa", "Versicolour", "Virginica"]

# Create 4x4 grid of graphs. Graphs each indentifier against each other

fig, ax = plt.subplots(4,4)

for i in range(4):
    for j in range(4):
        if i != 3:
            ax[i][j].tick_params(bottom=False, labelbottom=False)
        if j != 0:
            ax[i][j].tick_params(left=False, labelleft=False)
        if i == j:
            ax[i][j].text(0, 0, axisLabels[i])
            if i == 0:
                ax[i][j].axis(ymin = 0, ymax=max(dataToPlot[i]))
            if i == 3:
                ax[i][j].axis(xmin = 0, xmax=max(dataToPlot[i]))
            continue

        ax[i][j].scatter(dataToPlot[j], dataToPlot[i], c=classData, s=5)

#plt.savefig('iris4x4')
plt.show()

# Graphs a 3D projection of three identifiers

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(dataToPlot[0], dataToPlot[1], dataToPlot[3], c=classData)
ax.set_xlabel(axisLabels[0])
ax.set_ylabel(axisLabels[1])
ax.set_zlabel(axisLabels[3])
#plt.savefig('iris3DSepLSepWPetW')
plt.show()
