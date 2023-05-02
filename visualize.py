import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the cube vertices
vertices = np.array([[-1,-1,-1], [-1,-1,1], [-1,1,-1], [-1,1,1], [1,-1,-1], [1,-1,1], [1,1,-1], [1,1,1]])

# Define the edges between vertices
edges = [(0,1), (0,2), (0,4), (1,3), (1,5), (2,3), (2,6), (3,7), (4,5), (4,6), (5,7), (6,7)]

# Define the colors of each face
colors = ['white', 'red', 'orange', 'yellow', 'green', 'blue']

# Define the faces
faces = [(0,1,3,2), (0,2,6,4), (0,4,5,1), (1,5,7,3), (2,3,7,6), (4,6,7,5)]

# Plot the cube
for face in faces:
    ax.add_collection3d(
        plt.fill_between(vertices[face][:,0], vertices[face][:,1], vertices[face][:,2], color=colors[faces.index(face)], alpha=0.7))

# Plot the edges
for edge in edges:
    ax.plot(vertices[edge][:,0], vertices[edge][:,1], vertices[edge][:,2], 'k-', lw=2)

# Set the axis limits and labels
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
