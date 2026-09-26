from flask import Flask, render_template, jsonify
import psutil
import platform
import socket
import time
from datetime import datetime

app = Flask(__name__)

START_TIME = time.time()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("index.html", show_services=True)


@app.route("/status")
def status():
    return render_template("status.html")


@app.route("/api/metrics")
def metrics():

    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    uptime_seconds = int(time.time() - START_TIME)

    days = uptime_seconds // 86400
    hours = (uptime_seconds % 86400) // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60

    uptime = f"{days}d {hours}h {minutes}m {seconds}s"

    return jsonify({
        "cpu": cpu,
        "memory": memory.percent,
        "memory_used": round(memory.used / (1024 ** 3), 2),
        "memory_total": round(memory.total / (1024 ** 3), 2),
        "disk": disk.percent,
        "disk_used": round(disk.used / (1024 ** 3), 2),
        "disk_total": round(disk.total / (1024 ** 3), 2),
        "uptime": uptime,
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.release(),
        "python": platform.python_version(),
        "status": "Operational",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)