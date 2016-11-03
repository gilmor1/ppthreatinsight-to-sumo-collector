# ppthreatinsight-to-sumo-collector
Proofpoint Threat Insight to Sumologic Collector script in Python

Required Libs:
Requests (To install: pip install requests)

Trigger/cron/schedule to run every 5 mins. This can be changed in the code by updating the "sinceSeconds=300" to whatever you want. Maximum is seconds 3600 it seems.

Tested on AWS Lambda and works with small modifications
- Requires basic execution role
- Turn everything under "import requests" into a function e.g. "def collector(event,context):" and indent

To create Sumologic magic url
- Create a hosted collector
- Create a HTTP source
- Get private URL aka magic url

To create your Proofpoint Threat Insight keys
- Look in the threat insights console (more to come)

