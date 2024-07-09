# Endpoint Status Checker

This Python script tests the status of endpoints specified in a JSON file and writes the results to a CSV file. It utilizes the `requests` library to make HTTP requests to the endpoints.

## Preparation

1. Ensure you have Python installed on your system.

2. (Optional) Prepare a virtual env:
```
python3 -m venv .python_venv
. .python_venv/bin/activate
```

3. Install the required dependencies using pip:
```
pip install requests
```

## Features

- Test multiple endpoints for availability.
- Timeout parameter to customize the wait time for each request.
- Generate a CSV report with the status of each tested endpoint.

## Dependencies

- Python 3.x
- `requests` HTTP library for making requests.

## Installation

Before running the script, ensure you have the `requests` library installed. You can install it using pip:

```
pip install requests
```

## Usage

Create a JSON file named `endpoints.json` with the following structure:
```json
[
    {
        "name": "Endpoint 1",
        "openmetrics_endpoint": "http://example.com/endpoint1"
    },
    {
        "name": "Endpoint 2",
        "openmetrics_endpoint": "http://example.com/endpoint2"
    },
    ...
]

```

Run the script by executing the following command:
```
python test_endpoints.py
```

This will test the endpoints specified in `endpoints.json` and generate a CSV file named `endpoint_status.csv` with the results.

If you see an OpenSSL warning, try:
```
pip install urllib3==1.26.15
```

## Output

The script generates a CSV file named `endpoint_status.csv` with the following columns:
- name: The name of the service as provided in the JSON file.
- endpoint: The endpoint URL that was tested.
- status: The status result, which can be "Good", "Bad", "Timeout", or an error message.