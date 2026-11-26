# Python GIS & Mapping Learning Guide

Covers GeoPandas, Shapely, and Folium. Uses the [TindaHub Orders](../datasets/tindahub-orders/) dataset as its running example throughout.

## Files

| File | Use |
|---|---|
| `python-gis-mapping_learning_guide.html` | The guide itself. Open in a browser and start at Module 1.1, or use the Placement Quiz. |
| `tindahub_city_coords.csv` | City-level lat/lon lookup (`City, Province, Region, Lat, Lon`) for the 17 cities that appear in TindaHub Orders. Bundled so every exercise can build real Shapely/GeoPandas geometries without needing a live geocoding call. Coordinates are approximate city-hall/city-center reference points, not survey-grade — sufficient for teaching CRS, joins, and mapping, not for production-grade spatial analysis. |

For a real (non-teaching) Philippine choropleth, replace this guide's convex-hull province approximation with the authoritative PSA/NAMRIA-sourced boundaries at [HDX: Philippines Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-phl), as noted in the guide's Resources section.
