"""
Python script to query Connected Mobile Experiences (CMX) Mobility Services as a data for the names of available access
points and display them as a simple list.
"""

### IMPORTS ###
from urllib.request import Request, urlopen
import json

# Create CMX request
req = Request('https://cmxlocationsandbox.cisco.com/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')

# Return response
response = urlopen(req)
response_string = response.read().decode('utf-8')

# Format response to JSON
json_response = json.loads(response_string)

# Use JSON to print response, Formatting is better
#print(response_string)
#print(json.dumps(json_response, sort_keys=True, indent=4))

# Loop through the JSON response and retrieve the Access Points
access_points = json_response['accessPoints']
for ap in access_points:
    # Print results (for testing)
    print('Access Point: ' + ap['name'] + '\t mac: ' + ap['radioMacAddress'])

### END ###
response.close()
