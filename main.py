import matplotlib.pyplot as plt
from fastapi import FastAPI, BackgroundTasks
from rosreestr2coord import Area
import osmnx as ox
import geopandas as gdf
# x - долгота
# y - широта
import time

start = time.time()
app = FastAPI()

@app.post("/reestr")
def something(data: str):
    global coord
    # try:
    area = Area(f"{data}", use_cache=True)
    # use_cache=True - использовать кэширование запросов
    geojson = area.to_geojson() # гегографические структуры данных
    poly = area.to_geojson_poly() # расширенные gejson
    coord = area.get_coord() # [[[area1_xy], [hole1_xy], [hole2_xy]], [[area2_xyl]]] координаты
    attrs = area.get_attrs()
    lat_center = attrs["center"]["y"]
    lng_center = attrs["center"]["x"]
    lat_1 = coord[0][0][0][1]
    lat_2 = coord[0][0][1][1]
    lng_1 = coord[0][0][0][0]
    lng_2 = coord[0][0][1][0]
    sheik_sayed_dubai = [lat_1, lat_2, lng_1, lng_2]
    l = (*coord[0][0][0], *coord[0][0][1], *coord[0][0][2], *coord[0][0][3])
    k = l
    polygon = wkt.loads("((89.80059530838025 55.33131506353899, 89.80054953023337 55.33125997891148,89.80119922777946 55.331097729200074,89.8012432452284 55.331147806342365))")
    location_coordinates = (lat_center, lng_center)
    G = ox.graph_from_bbox(*sheik_sayed_dubai, simplify=False, retain_all=True, network_type='all')
    geometry, u, v = ox.get_nearest_edge(G, location_coordinates)
    print(polygon)
    background_tasks.add_task(sim())
    end = time.time() - start ## собственно время работы программы

    print(end)
    return coord

def sim():
    location_point = (37.791427, -122.410018)
    bbox = ox.graph_from_point(location_point)
    G2 = ox.graph_from_point(location_point, network_type='drive')
    G3 = ox.graph_from_point(location_point)
    k = plt.plot(bbox)
    s = plt.show()

sim()



