from konkomesh import KonkoMesh
from triangulate import is_point_in_circumcircle
from matplotlib import pyplot as plt
from math import hypot
import random

# Let us visualise a simple example of a triangle and it's circumcircle, and a randomly generated point to see 
# if it is inside the circumcircle or not.


# Mostly AI generated test
def plot_circumcircle(A, B, C, D):
    plt.figure(figsize=(8, 8))

    # Calculate the intersection of the perpendicular bisectors.
    ax, ay = A
    bx, by = B
    cx, cy = C
    denominator = 2 * (
        ax * (by - cy)
        + bx * (cy - ay)
        + cx * (ay - by)
    )
    if denominator == 0:
        raise ValueError("A degenerate triangle has no circumcircle")

    a_squared = ax**2 + ay**2
    b_squared = bx**2 + by**2
    c_squared = cx**2 + cy**2
    center_x = (
        a_squared * (by - cy)
        + b_squared * (cy - ay)
        + c_squared * (ay - by)
    ) / denominator
    center_y = (
        a_squared * (cx - bx)
        + b_squared * (ax - cx)
        + c_squared * (bx - ax)
    ) / denominator
    circumcenter = (center_x, center_y)

    # This next step is pretty costly and used for visualisation. Don't want to run this 100 000 times for every point.
    radius = hypot(A[0] - center_x, A[1] - center_y)

    # Create a circle for the circumcircle
    circle = plt.Circle(circumcenter, radius, color='blue', fill=False, linestyle='--', label='Circumcircle')

    # Plot triangle ABC
    triangle_x = [A[0], B[0], C[0], A[0]]
    triangle_y = [A[1], B[1], C[1], A[1]]
    plt.plot(triangle_x, triangle_y, 'g-', label='Triangle ABC')

    # Plot point D
    plt.plot(D[0], D[1], 'ro', label='Point D')

    # Add circumcircle to plot
    plt.gca().add_artist(circle)

    # Set equal aspect ratio and grid
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.title('Triangle ABC and Circumcircle with Point D')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # Show plot
    plt.show()

if __name__ == "__main__":
    A = (0, 0)
    B = (1, 0)
    C = (0, 1)

    D = (random.random()*2, random.random()*2)  # Random point [0, 2] x [0, 1]
    print(f"\nUsed tuples: A={A}, B={B}, C={C}, D={D}")

    if is_point_in_circumcircle(A, B, C, D):
        print("True, Point D is inside the circumcircle of triangle ABC.")
    else:
        print("False, Point D is outside the circumcircle of triangle ABC.")

    plot_circumcircle(A, B, C, D)
