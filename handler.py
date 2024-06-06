import json
from padel_availability import *
from datetime import datetime, timedelta

def check_availability(event, context):
    today = datetime.now().date()
    availability = getAvailability(today + timedelta(1))
    return {"statusCode": 200, "body": json.dumps(list(availability))}

print(check_availability("", ""))
