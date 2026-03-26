from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

def render_config(template_name, context):
    env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_name)
    return template.render(**context)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        context = {
            "hostname": request.form.get("hostname", "R1-Edge-London"),
            "domain_name": request.form.get("domain_name", "corp.internal"),
            "enable_secret": request.form.get("enable_secret", "") ,
            "admin_user": request.form.get("admin_user", "admin"),
            "admin_password": request.form.get("admin_password", "adminpass"),
            "banner": request.form.get("banner", "Unauthorized access is prohibited."),

            "console_password": request.form.get("console_password", "consPass"),
            "vty_password": request.form.get("vty_password", "vtyPass"),
            "ssh_version": request.form.get("ssh_version", "2"),
            "crypto_key_size": request.form.get("crypto_key_size", "2048"),
            "syslog_server": request.form.get("syslog_server", "10.0.0.5"),
            "logging_level": request.form.get("logging_level", "informational"),

            "int1_id": request.form.get("int1_id", "GigabitEthernet0/0/0"),
            "int1_desc": request.form.get("int1_desc", "WAN / ISP Link"),
            "int1_ip": request.form.get("int1_ip", "192.0.2.2"),
            "int1_mask": request.form.get("int1_mask", "255.255.255.252"),
            "int1_vlan": request.form.get("int1_vlan", ""),

            "int2_id": request.form.get("int2_id", "GigabitEthernet0/0/1"),
            "int2_desc": request.form.get("int2_desc", "LAN / Core Switch"),
            "int2_ip": request.form.get("int2_ip", "10.0.0.1"),
            "int2_mask": request.form.get("int2_mask", "255.255.255.0"),
            "int2_vlan": request.form.get("int2_vlan", ""),

            "loopback_id": request.form.get("loopback_id", "Loopback0"),
            "loopback_ip": request.form.get("loopback_ip", "10.0.0.254"),
            "loopback_mask": request.form.get("loopback_mask", "255.255.255.255"),

            "default_route": request.form.get("default_route", "0.0.0.0 0.0.0.0 192.0.2.1"),
            "static_routes": request.form.get("static_routes", ""),
            "routing_protocol": request.form.get("routing_protocol", "ospf"),
            "ospf_process": request.form.get("ospf_process", "1"),
            "bgp_as": request.form.get("bgp_as", "65001"),
            "router_id": request.form.get("router_id", "10.0.0.254"),
            "passive_interfaces": request.form.get("passive_interfaces", "GigabitEthernet0/0/1"),

            "dns1": request.form.get("dns1", "8.8.8.8"),
            "dns2": request.form.get("dns2", "8.8.4.4"),
            "ntp1": request.form.get("ntp1", "192.168.1.10"),
            "ntp2": request.form.get("ntp2", "192.168.1.11"),

            "dhcp_excluded": request.form.get("dhcp_excluded", "10.0.0.1 10.0.0.10"),
            "dhcp_network": request.form.get("dhcp_network", "10.0.0.0 255.255.255.0"),
            "dhcp_default_router": request.form.get("dhcp_default_router", "10.0.0.1"),
            "dhcp_dns": request.form.get("dhcp_dns", "8.8.8.8"),

            "nat_inside": request.form.get("nat_inside", "GigabitEthernet0/0/1"),
            "nat_outside": request.form.get("nat_outside", "GigabitEthernet0/0/0"),
            "acl_nat": request.form.get("acl_nat", "101"),
            "acl_nat_network": request.form.get("acl_nat_network", "10.0.0.0 0.0.0.255"),
        }

        config_text = render_config("template.j2", context)
        return render_template("result.html", config_text=config_text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
