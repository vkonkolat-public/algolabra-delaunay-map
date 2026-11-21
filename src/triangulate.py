# def get_orientation(a:tuple[float, float], b:tuple[float, float], c:tuple[float, float]) -> int:
#     # Calculate the orientation of the triangle formed by points a, b, and c
#     # Returns 1 if counterclockwise, -1 if clockwise, and 0 if collinear
#     ax, ay = a
#     bx, by = b
#     cx, cy = c

#     # Calculate the determinant (cross product)
#     det = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

#     if det > 0:
#         return 1  # Counterclockwise
#     elif det < 0:
#         return -1  # Clockwise
#     else:
#         return 0  # Collinear

#Calculate whether point D is inside the circumcircle of triangle ABC
#Takes in four sets of coordinates and returns True or False
#In use the four first points should remain the same while the fourth one is the point wer test and cycle through
def is_point_in_circumcircle(a:tuple[float, float], b:tuple[float, float], c:tuple[float, float], d:tuple[float, float]) -> bool:
    ax, ay = a
    bx, by = b
    cx, cy = c
    dx, dy = d

    # Back to the drawing board, this didn't work:
    # det = ((ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) * (dx**2 + dy**2)
    # - (ax**2 + ay**2) * (by - cy)
    # - (bx**2 + by**2) * (cy - ay)
    # - (cx**2 + cy**2) * (ay - by))
    

    # https://ianthehenry.com/posts/delaunay/    
    # Calculate the coordinate differences between the points
    adx = ax - dx
    ady = ay - dy

    bdx = bx - dx
    bdy = by - dy

    cdx = cx - dx
    cdy = cy - dy

    # By taking the square root of these we could get the distances between the points and point D.
    # But by by using the squared distances the algorithm avoids costful square root calculations (I am told)
    # and also avoids floating point inaccuracies
    # Full disclosure: math is lifted from : https://en.wikipedia.org/wiki/Delaunay_triangulation#algorithms
    ads = adx**2 + ady**2
    bds = bdx**2 + bdy**2
    cds = cdx**2 + cdy**2

    det = (
        adx * (bdy * cds - bds * cdy)
        - ady * (bdx * cds - bds * cdx)
        + ads * (bdx * cdy - bdy * cdx)
    )

    # get_orientation(a,b,c) returns 1 if the points are in counterclockwise order, -1 if clockwise, and 0 if collinear

    # inside = det * orientation > 0

    # When A, B, C are sorted in a counterclockwise order, this determinant is positive only if D lies inside the circumcircle.
    # If the point D is exactly on the circumcircle, det will be zero alongside other kind of nasty behaviour.
    if __name__ == "__main__":
        print(f"Determinant: {det}")
    return det > 0

#TODO: Cough up something that produces the circumcenter and radius of the circumcircle, but can it be done without square roots?


# Bunch of tests
# C
# |\
# | \
# |  \
# | D \
# |    \
# A-----B
if __name__ == "__main__":
    A = (0, 0)
    B = (1, 0)
    C = (0, 1)
    D = (0.5, 0.5)  # This point is inside the circumcircle of triangle ABC
    print(f"\nUsed tuples: A={A}, B={B}, C={C}, D={D}, should return True")

    if is_point_in_circumcircle(A, B, C, D):
        print("True, Point D is inside the circumcircle of triangle ABC.")
    else:
        print("False, Point D is outside the circumcircle of triangle ABC.")

    print()

    E = (0, 0)
    F = (1, 0)
    G = (0, 1)
    H = (0.5, 2.5)  # This point is outside ABC
    print(f"Used tuples: E={E}, F={F}, G={G}, H={H}, should return False")

    if is_point_in_circumcircle(E, F, G, H):
        print("True, Point H is inside the circumcircle of triangle EFG.")
    else:
        print("False, Point H is outside the circumcircle of triangle EFG.")

    print()

    #Now let's flip the triangle so that the points are in clockwise order and see if the function still works, it should return False
    I = (0, 0)
    J = (0, 1)
    K = (1, 0)
    L = (0.5, 0.5)  # This point is inside the circumcircle of triangle IJK
    print(f"Used tuples: I={I}, J={J}, K={K}, L={L}, should return False because the triangle is in clockwise order")

    if is_point_in_circumcircle(I, J, K, L):
        print("True, Point L is inside the circumcircle of triangle IJK.")
    else:
        print("False, Point L is outside the circumcircle of triangle IJK.")
    print()