import pytz
import json
import logging
from datetime import datetime

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
        default_tz = {'timezone': 'Europe/Berlin'}
        params = event.get('queryStringParameters')
        if params is None:
            params = default_tz
        logger.info(f"PARAMS: {params}")

        UTC = pytz.utc
        LOCAL = pytz.timezone(params['timezone'])

        response = {
            'statusCode': 200,
            'headers': {
                'content-type': 'application/json'
            },
            'body': json.dumps({
                'utc_time': datetime.now(UTC).strftime("%m/%d/%Y, %H:%M:%S"),
                'local_time': datetime.now(LOCAL).strftime("%m/%d/%Y, %H:%M:%S")
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
