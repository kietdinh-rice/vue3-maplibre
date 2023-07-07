import geopandas as gpd
import json
import os

gdf = gpd.read_file("CTA.geojson")
#gdf.to_file("CTA.geojson", driver='GeoJSON')
my_local_file = os.path.join(os.path.dirname(__file__), 'CTA.geojson')

with open(my_local_file) as file:
    data = json.load(file)
    features = data['features']
    for i,v in enumerate(features):
        data['features'][i]['id'] = v['properties']['OBJECTID']

    print(data['features'][0])

    with open("CTA2.geojson", "w") as outfile:
        outfile.write(json.dumps(data))