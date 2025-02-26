import sys
import geopandas as gpd
from shapely.geometry import Point

def is_inside_geofence(shapefile_path, lat, lon):
    """
    Check if a given GPS point (latitude, longitude) is inside a geofence loaded from a shapefile.

    Usage:
        python geofence_check.py <shapefile_path> <latitude> <longitude>

    Arguments:
        shapefile_path (str): Path to the shapefile containing the geofence.
        lat (float): Latitude of the point to check.
        lon (float): Longitude of the point to check.

    Returns:
        bool: True if the point is inside the geofence, False otherwise.
    
    Example:
        is_inside_geofence("protected_area.shp", -12.593, -69.182)  # True/False
    """
    # Load the shapefile
    geofence = gpd.read_file(shapefile_path)

    # Create a Point object from input coordinates
    point = Point(lon, lat)  # Shapely uses (x, y) -> (lon, lat)

    # Check if the point is inside any polygon in the shapefile
    inside = geofence.contains(point).any()

    # Print the result
    print(f"Point ({lat}, {lon}) is {'INSIDE' if inside else 'OUTSIDE'} the geofence.")

    return inside

# Run from command line
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python geofence_check.py <shapefile_path> <latitude> <longitude>")
        sys.exit(1)

    shapefile_path = sys.argv[1]
    latitude = float(sys.argv[2])
    longitude = float(sys.argv[3])

    is_inside_geofence(shapefile_path, latitude, longitude)
