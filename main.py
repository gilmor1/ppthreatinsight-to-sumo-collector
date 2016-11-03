import requests

#PP Threat Insight: API Key and Secret
serviceprinciple = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
secret = "<Secret goes here>"

#PP Threat Insight: Restful API for SIEM API
host = 'https://tap-api-v2.proofpoint.com'
path = '/v2/siem/all'
params = '?format=json&sinceSeconds=300'
url = host + path + params

#PP Threat Insight: Get logs from pp Threat Insight
ppti_response = requests.get(url, auth=(serviceprinciple, secret))
print("Response from PP Threat Insight")
print(ppti_response.content)



#Sumologic: Restful API for Sumologic HTTP Ingest
sumo_magic_url = '<Sumologic Hosted Collector HTTP Source, Magic URL goes here>'

#Sumologic: Send logs to Sumologic
sumo_response = requests.post(sumo_magic_url,data=ppti_response.content)
print(sumo_response)
