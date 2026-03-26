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
        hostname = request.form.get("hostname", "")
        mgmt_ip = request.form.get("mgmt_ip", "")
        gateway = request.form.get("gateway", "")

        context = {
            "hostname": hostname,
            "mgmt_ip": mgmt_ip,
            "gateway": gateway,
        }

        config_text = render_config("template.j2", context)

        return render_template("result.html", config_text=config_text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
