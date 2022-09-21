import re
import yaml
import json


class ConfigParser:
    def __init__(self):
        self.raw = []
        self.yaml_str = ""
        self.json_str = ""
        self.conf = None

    def load_config(self, file):
        with open(file, "r", encoding="utf-8-sig") as f:
            self.raw = f.readlines()

        self._parse()
        self.json_str = json.dumps(self.conf)

    def _parse(self):
        re_indent_root = re.compile(r"^((config|end).*)$")
        re_indent_config = re.compile(r"^(\s+)((config|edit) .*)$")
        re_indent = re.compile(r"^(\s+)(\w.*)$")
        re_cert = re.compile(r'(\s+)(set (private-key|certificate))( ".*)')
        re_cert_end = re.compile(r'(.*")$')

        str = ""

        cert_flg = False
        cert_indent = 0

        for line in self.raw:
            if cert_flg:
                if re_cert_end.match(line):
                    str = str + ((" " * (cert_indent + 4)) + line)
                    cert_flg = False
                    continue
                else:
                    str = str + ((" " * (cert_indent + 4)) + line)
                    continue

            if re_cert.match(line):
                cert_flg = True
                cert_indent = len(line) - len(line.lstrip(" "))
                str = str + re_cert.sub(r"\1- \2: |\n\1   \4", line)
                continue

            if re_indent_root.match(line):
                str = str + re_indent_root.sub(r"\1:", line)
            elif re_indent_config.match(line):
                str = str + re_indent_config.sub(r"\1- \2:", line)
            else:
                str = str + re_indent.sub(r"\1- \2", line)

        self.yaml_str = str
        self.conf = yaml.safe_load(str)

    def to_yaml(self):
        return self.yaml_str

    def to_json(self):
        return json.dumps(self.conf)

    def to_dict(self):
        return self.conf


if __name__ == "__main__":
    cp = ConfigParser()
    cp.load_config("tmp/test.conf")
    print(cp.to_json())
    print(cp.to_yaml())
    print(cp.to_dict())
