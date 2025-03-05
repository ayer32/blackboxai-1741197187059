import json
import os
from datetime import datetime

INCIDENTS_FILE = "incidents.json"

def log_incident(incident_type, description):
    """Log a security incident."""
    incident = {
        "type": incident_type,
        "description": description,
        "timestamp": datetime.now().isoformat()
    }
    
    incidents = load_incidents()
    incidents.append(incident)
    
    with open(INCIDENTS_FILE, 'w') as file:
        json.dump(incidents, file, indent=4)
    
    return "Incident logged successfully."

def load_incidents():
    """Load incidents from the JSON file."""
    if not os.path.exists(INCIDENTS_FILE):
        return []
    
    with open(INCIDENTS_FILE, 'r') as file:
        return json.load(file)

def get_incidents():
    """Retrieve all logged incidents."""
    return load_incidents()

# Example usage
if __name__ == "__main__":
    print(log_incident("Unauthorized Access", "Detected unauthorized access attempt on server."))
    print(get_incidents())
