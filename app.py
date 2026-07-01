from flask import Flask, jsonify
import os

app = Flask(__name__)

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return str(e)

@app.route("/")
def index():

    hostname = read_file("/mnt/etc/hostname")
    os_release = read_file("/mnt/etc/os-release")

    try:
        files = os.listdir("/mnt/tmp")
    except Exception as e:
        files = [str(e)]

    return jsonify({
        "Host Hostname": hostname,
        "Host OS": os_release,
        "Files in /mnt/tmp": files
    })

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=80)
