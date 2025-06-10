import os
import boto3
import json

db = boto3.resource('dynamodb')
table_name = os.environ.get('SENSORS_TABLE_NAME')
table = db.Table(table_name)

def lambda_handler(event, context):
    try:
        # This is how the event looks like:
        #{
            #  "body": "{\"id\": \"sensor-001\", \"type\": \"fire\", \"location\": \"Living Room\"}"
        #}
        # Parse incoming request body
        body = json.loads(event['body'])

        sensor_id = body['id']
        sensor_type = body['type']
        location = body['location']
        # Store sensor data in DynamoDB
        table.put_item(
            Item={
                'id': sensor_id,
                'type': sensor_type,
                'location': location,
                'createdAt': datetime.datetime.now().isoformat() # Add a timestamp
            }
        )

        # For now, just echo back the data as confirmation
        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "Sensor registered successfully",
                "sensor": {
                    "id": sensor_id,
                    "type": sensor_type,
                    "location": location
                }
            })
        }
    except json.JSDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid json in request body"})

        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

