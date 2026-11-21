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

def check_degeneracy(a:tuple[float, float], b:tuple[float, float], c:tuple[float, float]):
    ax, ay = a
    bx, by = b
    cx, cy = c
    abc_determinant = (
        (bx - ax) * (cy - ay)
        - (by - ay) * (cx - ax)
    )
    if abc_determinant == 0:
        raise ValueError("A degenerate triangle has no circumcircle")

#Calculate whether point D is inside the circumcircle of triangle ABC
#Takes in four sets of coordinates and returns True or False
#In use the four first points should remain the same while the fourth one is the point wer test and cycle through
def is_point_in_circumcircle(a:tuple[float, float], b:tuple[float, float], c:tuple[float, float], d:tuple[float, float]) -> bool:
    ax, ay = a
    bx, by = b
    cx, cy = c
    dx, dy = d

    # TODO: What if it ends up checking the same triangle 1000 times? This needs to end up somewhere else.
    # Check for degenerate triangle
    try:
        check_degeneracy(a, b, c)
    except ValueError as e:
        raise ValueError("Degenerate triangle: " + str(e))

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
    return det > 0

#TODO: Cough up something that produces the circumcenter and radius of the circumcircle, but can it be done without square roots?