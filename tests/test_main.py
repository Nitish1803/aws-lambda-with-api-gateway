import json
import logging
import unittest
from src import app
from unittest.mock import Mock
from copy import deepcopy


# Logging config
logger = logging.getLogger()


# Sample Event
REST_API_EVENT = {
      "resource": "/",
      "path": "/",
      "httpMethod": "GET",
      "requestContext": {
          "resourcePath": "/",
          "httpMethod": "GET",
          "path": "/Prod/"
      },
      "headers": {
          "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "accept-encoding": "gzip, deflate, br",
          "Host": "70ixmpl4fl.execute-api.us-east-2.amazonaws.com",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
          "X-Amzn-Trace-Id": "Root=1-5e66d96f-7491f09xmpl79d18acf3d050"
      },
      "multiValueHeaders": {
          "accept": [
              "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
          ],
          "accept-encoding": [
              "gzip, deflate, br"
          ],
      },
      "queryStringParameters": None,
      "multiValueQueryStringParameters": None,
      "pathParameters": None,
      "stageVariables": None,
      "body": {},
      "isBase64Encoded": False
  }


class TestApp(unittest.TestCase):
    def setUp(self):
        self.context = Mock(aws_request_id='test_aws_request_id')

    def test_default_response(self):
        test_event = deepcopy(REST_API_EVENT)
        lambda_result = app.lambda_handler(REST_API_EVENT, self.context)
        logger.info(f"RESPONSE - {lambda_result}")
        assert lambda_result['statusCode'] == 200
        assert ['statusCode', 'headers', 'body'] == list(lambda_result.keys())

    def test_error_response(self):
        test_event = deepcopy(REST_API_EVENT)
        test_event['queryStringParameters'] = {'timezone': 'ABC'}
        lambda_result = app.lambda_handler(test_event, self.context)
        logger.info(f"RESPONSE - {lambda_result}")
        assert lambda_result['statusCode'] == 503
        assert 'error' in list(json.loads(lambda_result['body']).keys())

    def test_different_timezone_response(self):
        test_event = deepcopy(REST_API_EVENT)
        test_event['queryStringParameters'] = {'timezone': 'Asia/Kolkata'}
        lambda_result = app.lambda_handler(test_event, self.context)
        logger.info(f"RESPONSE - {lambda_result}")
        assert lambda_result['statusCode'] == 200
        assert ['statusCode', 'headers', 'body'] == list(lambda_result.keys())
