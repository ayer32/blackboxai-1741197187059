from flask import Flask, request, jsonify
from modules.database import Database
from modules.external_tool_integration import run_nmap_scan, run_wireshark
from modules.api_integration import start_scan, get_scan_results

app = Flask(__name__)
db = Database()

@app.route('/nmap', methods=['POST'])
def nmap_scan():
    target = request.json.get('target')
    result = run_nmap_scan(target)
    db.insert_scan(target, result)
    return jsonify({"result": result})

@app.route('/nessus/start', methods=['POST'])
def nessus_start_scan():
    scan_id = request.json.get('scan_id')
    result = start_scan(scan_id)
    return jsonify({"result": result})

@app.route('/nessus/results/<int:scan_id>', methods=['GET'])
def nessus_get_results(scan_id):
    results = get_scan_results(scan_id)
    return jsonify({"results": results})

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = db.get_incidents()
    return jsonify({"incidents": incidents})

@app.route('/scans', methods=['GET'])
def get_scans():
    scans = db.get_scans()
    return jsonify({"scans": scans})

if __name__ == "__main__":
    app.run(debug=True)
