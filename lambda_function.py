import http.client
import json


def lambda_handler(event, context):
	
	conn = http.client.HTTPSConnection("www.cheapshark.com")
	payload = ''
	headers = {"Access-Control-Allow-Origin": "*"}
	gameName = str(event['gameName'])
	conn.request("GET", "/api/1.0/games?title=" + gameName + "&limit=1&exact=0", payload, headers)
	res = conn.getresponse()
	data = res.read()
	data_decoded = data.decode("utf-8")
	crawler = json.loads(data_decoded)[0]
	
	print(crawler)
	return {
	    'statusCode': 200,
	    'gameName': str(crawler['external']),
		'gamePrice': str(crawler['cheapest']),
		'steamID': str(crawler['steamAppID']),
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },		
	}