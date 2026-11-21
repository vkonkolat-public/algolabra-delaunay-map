from matplotlib import pyplot as plt
from math import hypot
import random
import time

# Local imports
from src.konkomesh import KonkoMesh
from src.triangulate import is_point_in_circumcircle

# Let us visualise a simple example of a triangle and it's circumcircle, and a randomly generated point to see 
# if it is inside the circumcircle or not.


# Mostly AI generated test
def plot_circumcircle(A, B, C, list_of_points: list[tuple[float, float]]):
    # plt.figure(figsize=(8, 8))

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

    # Plot test points and label them with their expected circumcircle status.
    inside_label_added = False
    outside_label_added = False
    for index, point in enumerate(list_of_points, start=1):
        is_inside = is_point_in_circumcircle(A, B, C, point)
        color = 'green' if is_inside else 'red'
        status = 'inside' if is_inside else 'outside'

        if is_inside:
            label = 'Inside circumcircle' if not inside_label_added else None
            inside_label_added = True
        else:
            label = 'Outside circumcircle' if not outside_label_added else None
            outside_label_added = True

        plt.plot(point[0], point[1], 'o', color=color, label=label)
        plt.annotate(
            f"D{index}: {status}",
            (point[0], point[1]),
            xytext=(6, 6),
            textcoords='offset points',
        )

    # Add circumcircle to plot
    plt.gca().add_artist(circle)

    # Set equal aspect ratio and grid
    plt.axis('equal')
    plt.xlim(-2, 5)
    plt.ylim(-2, 5)
    plt.grid()
    plt.legend()
    plt.title('Triangle ABC and Circumcircle with Point D')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # Render the plot without waiting for the window to close.
    plt.show(block=False)
    plt.pause(0.001)

def get_random_point():
    return (random.uniform(-2, 5), random.uniform(-2, 5))

if __name__ == "__main__":
    timestart = time.perf_counter()
    A = (0, 0)
    B = (3, 0)
    C = (0, 3)

    # Five test points with randomised values starting from D
    test_points : list = [get_random_point() for _ in range(50)]

    for D in test_points:
        print(f"\nUsed tuples: A={A}, B={B}, C={C}, D={D}")

        if is_point_in_circumcircle(A, B, C, D):
            print("True, Point D is inside the circumcircle of triangle ABC.")
        else:
            print("False, Point D is outside the circumcircle of triangle ABC.")
        print()

    plot_circumcircle(A, B, C, test_points)
    timeend = time.perf_counter()
    print(f"Execution time: {timeend - timestart:.4f} seconds")
    input("Press Enter to exit...")