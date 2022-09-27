import re
import yaml, json

re_config_vdom = re.compile(r"^(config vdom) *$")
re_config = re.compile(r"^ *(config .*) *$")
re_edit = re.compile(r"^ *(edit .*) *$")
re_set = re.compile(r"^ *(set .*) *$")
re_next = re.compile(r"^ *(next)$")
re_end = re.compile(r"^ *(end)$")


class ConfigParser:
    def __init__(self):
        self.raw = []
        pass

    def load_config(self, config_file):
        with open(config_file, "r", encoding="utf-8-sig") as f:
            self.raw = f.readlines()

        self._parse_to_yaml_raw()
        self.json_str = json.dumps(self.conf)

    def _parse_to_yaml_raw(self):
        str = ""
        indent_lv = 0

        config_count = 0
        edit_count = 0
        next_count = 0
        end_count = 0

        for line in self.raw:
            if re_config_vdom.match(line):
                indent_lv = 0
                str += f"{'    ' * indent_lv}- {line.strip()}:\n"
                indent_lv = indent_lv + 1

            elif re_config.match(line):
                str += f"{'    ' * indent_lv}- {line.strip()}:\n"

                indent_lv = indent_lv + 1
                config_count += 1

            elif re_edit.match(line):
                str += f"{'    ' * indent_lv}- {line.strip()}:\n"
                indent_lv = indent_lv + 1
                edit_count += 1

            elif re_set.match(line):
                str += f"{'    ' * indent_lv}- {line.strip()}\n"

            elif re_next.match(line):
                indent_lv = indent_lv - 1

                next_count += 1

            elif re_end.match(line):
                indent_lv = indent_lv - 1

                end_count += 1

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
    cp.load_config("tmp/test2.conf")
    # print(cp.to_json())
    # with open("tmp/chk.yaml", "w", encoding="utf8") as f:
    #     f.write(cp.to_yaml())
    # print(cp.to_dict())

    for i in cp.to_dict():
        print(i.keys())
