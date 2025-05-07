from arcgis.gis import GIS
import json

# Sign in using your ArcGIS credentials
gis = GIS("home")
item = gis.content.get("8297c87ecaa7441394172e5aee97b4ef")

# Fetch and save the web map JSON
webmap_json = item.get_data()
with open("boston_canopy_equity_webmap.json", "w") as f:
    json.dump(webmap_json, f, indent=2)

print("Saved web map JSON to boston_canopy_equity_webmap.json")
