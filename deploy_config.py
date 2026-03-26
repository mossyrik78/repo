import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def render_template(template_name, context):
    env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_name)
    return template.render(**context)


def push_config(device, config_text):
    with ConnectHandler(**device) as conn:
        print(f"Connected to {device['host']}")
        if device["device_type"].startswith("cisco"):
            return conn.send_config_set(config_text.splitlines())
        return conn.send_config_set(config_text)


def main():
    data = load_yaml("devices.yml")
    template_name = "template.j2"

    for host in data.get("devices", []):
        context = host.get("template_vars", {})
        config = render_template(template_name, context)
        print("--- render for", host["host"])
        print(config)

        # Uncomment to push to real devices
        # output = push_config(host, config)
        # print(output)


if __name__ == "__main__":
    main()
