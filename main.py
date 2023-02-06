from fastapi import FastAPI
from pydantic import BaseModel
from rosreestr2coord import Area
from rosreestr2coord.console import console

app = FastAPI()

class User(BaseModel):
    registr: str



@app.post("/")
def post_reestr(registr:User):
    return registr

# print(User.registr)

if __name__ == "__main__":
    console()


@app.post("/reestr")
def something(register: User):
    # a = area
    area = Area("24:39:101001:369")
    # аргументы
    #   code='' - кадастровый номер участка
    #   area_type=1 - тип площади
    #   epsilon=5 - точность аппроксимации
    #   media_path='' - путь для временных файлов
    #   with_log=True - логирование
    #   coord_out='EPSG:4326' - или EPSG:3857 (будет удалена в последующих версиях)
    #   center_only=False - экспорт координат центров участка
    #   with_proxy=False - запросы через прокси
    #   use_cache=True - использовать кэширование запросов
    b = area.to_geojson()
    print(b)
    print(area.to_geojson_poly())
    print(area.get_coord()) # [[[area1_xy], [hole1_xy], [hole2_xy]], [[area2_xyl]]]
    print(area.get_attrs())
    return b, register