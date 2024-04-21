import requests
import csv
import json

def test_endpoints(endpoints, timeout=10):  # Added timeout parameter with a default of 10 seconds
    results = []
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint['openmetrics_endpoint'], timeout=timeout)
            if response.status_code == 200 and response.text:
                status = "Good"
            else:
                status = "Bad"
        except requests.exceptions.Timeout:
            status = "Timeout"  # Specific status for timeout
        except Exception as e:
            status = f"Error: {str(e)}"  # Include error message in the status
        
        results.append({
            "name": endpoint['name'],
            "endpoint": endpoint['openmetrics_endpoint'],
            "status": status
        })
    
    return results

def write_results_to_csv(results, filename):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['name', 'endpoint', 'status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)

if __name__ == "__main__":
    # Read endpoints from JSON file
    with open("endpoints.json", "r") as file:
        endpoints = json.load(file)
    
    results = test_endpoints(endpoints)
    write_results_to_csv(results, "endpoint_status.csv")