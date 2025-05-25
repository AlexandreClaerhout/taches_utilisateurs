from io import TextIOWrapper
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
from sqlalchemy import URL, create_engine, engine_from_config, text
import os, inspect

config_obj:ConfigParser = ConfigParser()
script_dir:str = os.path.dirname(__file__)
rel_path:str = "config/config.ini"
options:list = inspect.getfullargspec(URL.create).args

try:
    abs_file_path:str = os.path.join(script_dir, rel_path)

    ini_file:TextIOWrapper = open(abs_file_path,'r')

    config_obj.read_file(ini_file)

    config_raw:dict = dict(config_obj.items(section="connection"))
    config_raw.update({"drivername":'+'.join(filter(None, [config_raw[x] for x in ["dialect","driver"]]))})

    config:dict = {key:val for key, val in config_raw.items() if key in options}

    connection_string:URL = URL.create(**config)

    engine = create_engine(url=connection_string, echo=config_raw.get("debug")=='1')

    connection = engine.connect()

    # rows = connection.execute(text("SELECT * FROM pg_catalog.pg_tables where schemaname != 'information_schema' and schemaname != 'pg_catalog';"))
    # for row in rows:
    #     print(row)

except Exception as e:
    print(e)
finally:
    pass

