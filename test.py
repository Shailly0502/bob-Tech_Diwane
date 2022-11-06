import requests, uuid, json



# Add your key and endpoint
key = "f1c229e98aab4aadb05d9c37601d079a"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.

location = "eastus"

path = '/detect'
constructed_url = endpoint + path

params = {
    'api-version': '3.0'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
def detect_lang(ocr):
    # You can pass more than one object in body.
    body = [{
        'text': ocr
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    jsonString=json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    alist=json.loads(jsonString)
    # print(alist[0]['language'])
    return alist[0]['language']

