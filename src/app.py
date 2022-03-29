import json
import logging
from datetime import datetime
from dateutil import tz


# Logging config
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    """
    Lambda Handler
    """
    logger.debug(f"EVENT: {event}")
    logger.debug(f"CONTEXT: {vars(context)}")

    try:
        params = event.get('queryStringParameters')
        if not params:
            params = {'timezone': 'Europe/Berlin'}
        logger.info(f"PARAMS: {params}")

        UTC = tz.tzutc()
        LOCAL = tz.gettz(params.get('timezone'))

        response = {
            'statusCode': 200,
            'headers': {
                'content-type': 'application/json'
            },
            'body': json.dumps({
                'utc_time': datetime.now(tz=UTC).strftime("%m/%d/%Y, %H:%M:%S"),
                'local_time': datetime.now(tz=LOCAL).strftime("%m/%d/%Y, %H:%M:%S")
            })
        }
    except Exception as e:
        response = {
            'statusCode': 503,
            'body': json.dumps({
                'error': repr(e)
            })
        }
    return response
