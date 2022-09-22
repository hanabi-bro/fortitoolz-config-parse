from config_parse import ConfigParser
from rich import print, pretty

pretty.install()

cp = ConfigParser()

cp.load_config("tmp/test.conf")
config = cp.to_dict()

conf_fp = config["config firewall policy"]

print(conf_fp)
