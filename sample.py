from fg_config_parser import FgConfigParser
from rich import print, pretty
import numpy as np

pretty.install()

cp = FgConfigParser()

cp.load_config("tmp/test1.conf")
config = cp.to_dict()


use_vdom = False
if "config vdom" in config[0].keys():
    use_vdom = True

print(use_vdom)

if use_vdom:
    vdom_keys = []
    for c in config[0]["config vdom"]:
        vdom_keys.append(list(c.keys())[0])

    for i, c in enumerate(vdom_keys):
        print(c)
        for c in config[2 + i]["config vdom"][0][c]:
            if list(c.keys())[0] == "config firewall address":
                print(c["config firewall address"])

else:
    for c in config:
        if list(c.keys())[0] == "config firewall address":
            print(c["config firewall address"])

# with open("tmp/chk.txt", "w", encoding="utf8") as f:
#     print(config, file=f)

# config_list = {}
# for i, c in enumerate(config[2]["config vdom"][0]["edit root"]):
#     if list(c.keys())[0] == "config firewall address":
#         config_list = c["config firewall address"]
