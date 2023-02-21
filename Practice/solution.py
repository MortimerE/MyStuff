#solution.py

import json
import requests

MERGE_SERVICE_URL = "merger.example.com"
def process_issue_comment(webhook_body):
    """Process an issue_comment event from GitHub.
    Called whenever GitHub sends a webhook as a result of a comment on a pull request thread.
    """
    # TODO: Parse the JSON data from the webhook body, and if the issue comment is "#merge"
    # and the pull request is in the "Ableton" organization, call the merge service API
    # to request that the pull request is merged.

    body = json.loads(webhook_body) #based on the github docs, this should result in a DICT 
    if len(body) < 1:
        return None

    if (body.get('comment').get('body') == "#merge") and (body.get('organization').get('name') == "Ableton"): #this assumes the flag is the entire comment body
        #merge API request 
        owner = body.get('repository').get('owner').get('login') #repository owner username
        name = body.get('repository').get('full_name') #repo name, I opted for the full path in this case
        num = body.get('issue').get('number') #pull request #
        url =  f"{MERGE_SERVICE_URL}/api/v4/repos/{owner}/{name}/pulls/{num}/merge" #endpoint URL as a string 
        j_load = { #request data as a DICT
            'pull':{
                'base_ref': body.get('issue').get('base').get('ref'), #pull target 
                'head_sha': body.get('issue').get('head').get('sha') #current branch sha
            },
            'requester':body.get('issue').get('user').get('login') #username of merge requester
        }

        requests.post(url, json = j_load) #POST request definition, ignoring auth/oauth headers
        #as the prompt did not specify headers, I am leaving them out under the scope of this exercise