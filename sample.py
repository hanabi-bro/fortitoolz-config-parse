from config_paser import ConfigParser
from rich import print, pretty
import numpy as np

pretty.install()

cp = ConfigParser()

cp.load_config("tmp/test3.conf")
config = cp.to_dict()


# with open("tmp/chk.txt", "w", encoding="utf8") as f:
#     print(config, file=f)

for i in config[2]["config vdom"][0]["edit root"]:
    print(i.keys())
