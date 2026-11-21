# algolabra-delaunay-map
Aineopintojen harjoitustyö-repositorio

# Toiminta
Entrypointt- eli käynnistät ohjelman ajamalla main.py.

Toiminnallisuus 2026-11-21 rajoittuu ei trianguloidun pistesarjan pisteiden välille muodostettujen kolmioiden näyttämiseen.

# build and configuration

- %%the usual mumbojumbo, think about pip users too%%
- uv sync

# Testaus 
run "pytest src" at the root of the folder

## Manual visual testing
src\tests\circumcircle_test_visual to be run MANUALLY and visually appraised 
src\matlib_visualiser.py shows a visual when ran manually to indicate output behaviour
src\bowyer_watson.py for a visual check of a generated triangulated mesh.