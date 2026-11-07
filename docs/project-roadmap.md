# Project Roadmap

The goal is to implement a 2D Delaunay triangulation with the Bowyer–Watson algorithm in Python, then use it as the basis for the map-generation pipeline. Implement the geometry and triangulation in this project rather than delegating triangulation to an existing library.

## Definition of done

- [ ] Given a valid set of 2D points, produce a triangulation that covers their convex hull.
- [ ] Ensure every output triangle is counterclockwise and no input point lies inside the circumcircle of any output triangle.
- [ ] Handle documented degenerate inputs consistently, including duplicates, collinear points, and cocircular points.
- [ ] Validate triangulation structure and behavior with automated tests, not only visual inspection.
- [ ] Document expected complexity, numerical limitations, and supported input cases.

## Phase 1 — Scope and design

- [ ] Keep the first implementation 2D and focused on Bowyer–Watson; defer 3D.
- [ ] Define a point type and a triangle representation, including how triangle edges are represented and compared.
- [ ] Decide and document the public input/output format and behavior for empty or invalid input.
- [ ] Decide how duplicate points are handled and how cocircular cases are resolved deterministically.
- [ ] Find and record reliable references for the algorithm and robust geometric predicates. Treat the existing Wikipedia pseudocode as an outline, not an implementation specification.
- [ ] Set up a small deterministic test dataset and make insertion order reproducible.

## Phase 2 — Geometry primitives

- [ ] Implement orientation (signed area) and use it to normalize triangles to counterclockwise order.
- [ ] Implement an in-circle predicate for testing whether a point lies inside a triangle's circumcircle.
- [ ] Define consistent behavior for points on an edge or circumcircle and for zero-area triangles.
- [ ] Add unit tests for each predicate, including reversed orientation, points on boundaries, and large and small coordinate values.
- [ ] Document the chosen numeric representation and known precision limitations; investigate more robust predicates if tests expose instability.

## Phase 3 — Bowyer–Watson baseline

- [ ] Calculate a super-triangle that contains every input point and document how its size is chosen.
- [ ] Start with the super-triangle and insert points one at a time.
- [ ] For each insertion, find the triangles whose circumcircles contain the point.
- [ ] Find the cavity boundary by counting undirected edges of the removed triangles; retain edges occurring exactly once.
- [ ] Remove the cavity triangles and connect each boundary edge to the inserted point, skipping zero-area triangles.
- [ ] Remove all triangles that contain a super-triangle vertex before returning the result.
- [ ] Add focused tests for one point, a triangle, interior points, hull points, and points inserted in different orders.

## Phase 4 — Correctness and edge cases

- [ ] Add a test helper that checks counterclockwise orientation, valid vertex references, and absence of duplicate triangles.
- [ ] Check that every input point is represented and every output triangle has no other input point strictly inside its circumcircle.
- [ ] Test empty, singleton, two-point, duplicate, collinear, nearly collinear, cocircular, and boundary-point inputs.
- [ ] Verify that the union of triangles covers the convex hull and that internal edges are shared by exactly two triangles.
- [ ] Define and test the behavior for inputs that cannot produce a 2D triangulation, such as fewer than three unique non-collinear points.
- [ ] Add regression tests for every bug found during development.

## Phase 5 — Performance and usability

- [ ] Measure runtime and memory on reproducible point sets of increasing sizes.
- [ ] Record the baseline complexity and identify the actual bottleneck before optimizing; the straightforward implementation may scan all triangles for each insertion.
- [ ] If needed, improve point location or cavity discovery while preserving the tested baseline behavior.
- [ ] Add input validation and useful error messages at the public API boundary.
- [ ] Document how to run tests and a small example of generating a triangulation.

## Phase 6 — Map-generation pipeline

- [ ] Generate deterministic seed points within map bounds from a configurable count and random seed.
- [ ] Derive Voronoi regions from the Delaunay triangulation and clip them to the map bounds.
- [ ] Build the region-neighbor graph and compute a minimum spanning tree (MST).
- [ ] Test that the generated graph is connected where expected and that the MST has the expected number of edges.
- [ ] Compare generated output across seeds and check that all geometry stays within the requested map bounds.

## Optional investigations

- [ ] Derive the Gabriel graph from Delaunay edges and compare its connectivity and edge count with the Delaunay graph.
- [ ] Compare MST results using the Delaunay graph and Gabriel graph; keep the chosen graph explicit in the project specification.
- [ ] Use MATLAB's divide-and-conquer triangulation only as an independent correctness or performance reference, not as the implementation.
- [ ] Explore a browser-based 2D/3D visualization after the core tests pass.
- [ ] Revisit 3D tetrahedralization only after the 2D pipeline is complete.

## Working notes

- Coding agents may be used to summarize and rewrite project documentation from notes.
- Keep the initial algorithm implementation independent of existing triangulation libraries.

## Initial Bowyer–Watson pseudocode


```
function BowyerWatson (pointList)
    // pointList is a set of coordinates defining the points to be triangulated
    triangulation := empty triangle mesh data structure
    add super-triangle to triangulation // must be large enough to completely contain all the points in pointList
    for each point in pointList do // add all the points one at a time to the triangulation
        badTriangles := empty set
        for each triangle in triangulation do // first find all the triangles that are no longer valid due to the insertion
            if point is inside circumcircle of triangle
                add triangle to badTriangles
        polygon := empty set
        for each triangle in badTriangles do // find the boundary of the polygonal hole
            for each edge in triangle do
                if edge is not shared by any other triangles in badTriangles
                    add edge to polygon
        for each triangle in badTriangles do // remove them from the data structure
            remove triangle from triangulation
        for each edge in polygon do // re-triangulate the polygonal hole
            newTri := form a triangle from edge to point
            add newTri to triangulation
    for each triangle in triangulation // done inserting points, now clean up
        if triangle contains a vertex from original super-triangle
            remove triangle from triangulation
    return triangulation
```

Initial outline courtesy of Wikipedia.
