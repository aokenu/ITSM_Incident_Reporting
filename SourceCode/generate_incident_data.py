import csv
import random
from datetime import datetime, timedelta

# Reinitialize constants
file_paths = {
    "Incidents": "C:/Users/austi/OneDrive/Documents/DataProjects/data/incidents.csv",
    "Categories": "C:/Users/austi/OneDrive/Documents/DataProjects/data/categories.csv",
    "Services": "C:/Users/austi/OneDrive/Documents/DataProjects/data/services.csv",
    "Clients": "C:/Users/austi/OneDrive/Documents/DataProjects/data/clients.csv",
    "Incident_Types": "C:/Users/austi/OneDrive/Documents/DataProjects/data/incident_types.csv",
}


# Constants
statuses = ["Open", "In Progress", "Resolved", "Closed"]
priorities = ["Critical", "High", "Medium", "Low"]
sla_times = {"Critical": 4, "High": 24, "Medium": 72, "Low": 168}  # SLA times in hours

# Helper Functions
def random_datetime(start, end):
    """Generate a random datetime between two datetime objects."""
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randint(0, int_delta)
    return start + timedelta(seconds=random_second)

# 1. Services Table
services = [
    {"service_id": i, "name": name, "description": f"{name} service description"}
    for i, name in enumerate(
        ["Consent Management", "Bills Payment", "Instant Payment", "Identity Verification", "Cards"], start=1
    )
]

# 2. Categories Table
categories = [
    {"category_id": i, "name": name}
    for i, name in enumerate(["Network", "Hardware", "Application", "Others"], start=1)
]

# 3. Clients Table
client_names = [
    "Acme Corp", "Globex Corporation", "Initech", "Umbrella Corporation", 
    "Wayne Enterprises", "Stark Industries", "Hooli", "Wonka Industries", 
    "Dunder Mifflin", "Pied Piper", "Vandelay Industries", "Cyberdyne Systems",
    "Aperture Science", "Planet Express", "Black Mesa", "Tyrell Corporation",
    "Yoyodyne Propulsion", "Oceanic Airlines", "LexCorp", "Monarch Solutions",
    "Massive Dynamic", "Oscorp", "Devlin MacGregor", "OCP", "Virtucon"
]
clients = [
    {"client_id": i, "name": random.choice(client_names), "email": f"client{i}@example.com"}
    for i in range(1, 101)
]

# 4. Incident Types Table
incident_type_names = [
    "Network Downtime", "Server Overload", "Unauthorized Access", 
    "Data Corruption", "Login Failure", "Software Crash", 
    "Service Timeout", "Configuration Error", "Hardware Failure", 
    "Email Delivery Failure", "Database Connection Issue", 
    "Firewall Misconfiguration", "DNS Resolution Failure", 
    "API Latency", "Storage Capacity Exceeded"
]
incident_types = [
    {"type_id": i, "name": name, "description": f"{name} description"}
    for i, name in enumerate(incident_type_names, start=1)
]

# 5. Incidents Table
incidents = []
for i in range(1, 26571):
    created_date = random_datetime(datetime(2024, 1, 1), datetime(2024, 11, 1))
    priority = random.choice(priorities)
    status = random.choice(statuses)
    resolution_time = None
    resolved_date = None

    if status in ["Resolved", "Closed"]:
        resolution_time_limit = timedelta(hours=random.randint(1, sla_times[priority]))
        resolved_date = created_date + resolution_time_limit
        resolution_time = resolved_date - created_date

    incidents.append({
        "incident_id": i,
        "created_date": created_date.strftime("%Y-%m-%d %H:%M:%S"),
        "resolved_date": resolved_date.strftime("%Y-%m-%d %H:%M:%S") if resolved_date else None,
        "status": status,
        "priority": priority,
        "resolution_time": resolution_time.total_seconds() if resolution_time else None,
        "category_id": random.choice(categories)["category_id"],
        "service_id": random.choice(services)["service_id"],
        "client_id": random.choice(clients)["client_id"],
    })

# Save CSV files
datasets = {
    "Services": services,
    "Categories": categories,
    "Clients": clients,
    "Incident_Types": incident_types,
    "Incidents": incidents,
}

for table, data in datasets.items():
    with open(file_paths[table], mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

file_paths
