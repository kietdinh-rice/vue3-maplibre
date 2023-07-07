import geopandas as gpd

#gdf = gpd.read_file("CTA2020_boundary_Projected_new.shp")
#gdf.to_file("CTA.geojson", driver='GeoJSON')

shp_file = "CTA2020_boundary_Projected_new.shp"
json_file = "CTA.geojson"

# Read in data
gdf = gpd.read_file(shp_file)
# Reproject to Lat/Long: http://epsg.io/4326
gdf_4326 = gdf.to_crs(epsg='4326')
# Write to file
gdf_4326.to_file(json_file, driver="GeoJSON")