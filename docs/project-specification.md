# Project Specification: Procedural Map Generation with Delaunay + Voronoi + MST

## 1. Programming language

Primary implementation language:

- **Python**

## 2. Problem being solved

The project solves the problem of generating a **small, viewable procedural map** for a simulation or game.

The map should look coherent by structure, devoid of sliver triangles or other strange artefacts while still being generated from input parameters. 
The generated output is based on geometric partitioning and graph algorithms:

- Delaunay triangulation for neighborhood structure,
- Voronoi diagram for chunk/region boundaries,
- Minimum Spanning Tree (MST) for a connected backbone between key regions.


## 3. Inputs and how they are used

Planned input parameters:

1. **Map size** (width and height with possible simulated height by voronoi chunk)
2. **Number of Voronoi chunks** (number of seed points / regions)

How inputs are used:

- Map size defines the 2D bounds where points are generated.
- Number of chunks defines how many seed points are sampled.
- Seed points are triangulated with Delaunay triangulation.
- Voronoi regions are derived from those points (or from the triangulation dual).
- A graph is formed from neighboring points/regions and an MST is computed to ensure connected structure for traversal/roads/rivers or similar map features.

## 4. Algorithms and data structures

### Algorithms

- **Delaunay triangulation** (core geometric structure)
- **Voronoi diagram construction** (region partitioning)
- **Minimum Spanning Tree** (Kruskal or Prim on region-neighbor graph)

### Data structures

- 2D point list/array for seed points
- Edge list for triangulation graph
- Adjacency list for region-neighbor graph
- Disjoint Set Union (Union-Find), if Kruskal is used
- Priority queue, if Prim is used

## 5. Target time and space complexity

Let \(n\) be the number of Voronoi chunks (seed points).

### Delaunay triangulation

- Typical target complexity from standard algorithms: **\(O(n \log n)\)**
- Worst-case behavior can be higher for some implementations/input orders, but design target is \(O(n \log n)\).

### Voronoi generation

- If constructed as the dual of Delaunay, additional processing is typically **\(O(n)\)** to **\(O(n \log n)\)** depending on representation details.

### MST on Delaunay-based graph

- For planar Delaunay graphs, number of edges is linear (\(E = O(n)\)).
- Kruskal: \(O(E \log E) = O(n \log n)\)
- Prim (binary heap): \(O(E \log V) = O(n \log n)\)

### Overall target

- **Time:** \(O(n \log n)\) dominant term
- **Space:** \(O(n)\) to \(O(n + E)\), which is \(O(n)\) for planar sparse graphs

## 6. Core of the project (Harjoitustyön ydin)

The core of this project is the **algorithmic generation pipeline**:

1. generate points inside map bounds,
2. build Delaunay triangulation,
3. derive Voronoi regions,
4. build and process the neighbor graph with MST.


## 7. Planned sources

I'm initially planning to use

Lee, D. & Schachter, B.. (1980). 
Two algorithms for constructing a Delaunay triangulation. International Journal of Computer & Information Sciences. 9. 219-242. 10.1007/BF00977785. 

Or some available online resource to build the delaunay triangulation without resorting to existing libraries.
