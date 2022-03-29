# aws-lambda-with-api-gateway-using-sam

## Description

Simple AWS Lambda with API Gateway deployed using AWS SAM (Serverless Application Model)

   ![FLOW_DIAGRAM GET](./docs/images/Flow_Diagram.png?raw=true)

## Installation

1. Clone this repo. Install dependencies by running `pip install -r requirements.txt`.
2. In order to run tests, install `pytest`.
3. For deployment of the service to AWS Cloud, `aws` and `sam` CLI(s) should be installed and configured.

## Usage

- Run `run.py` to deploy the service to AWS Cloud.

- Check in `Cloudformation` is the stack is deployed or not.

  ![CFN GET](./docs/images/CFN.png?raw=true)

- After successfull deployment, send requests to the service using deployed `API Gateway`.
  The API also supports a queryParameter `timezone` if user wants to get time in a different timezone.

## Local Usage
- Install Docker (https://docs.docker.com/get-docker/)
- After successful installation, run command `sam local start-api`

  ![sam_local](./docs/images/sam_api_local.png?raw=true)

- You will be able to hit the API Endpoint(s) locally from your localhost.
  
  ![localhost_api](./docs/images/getTime_local.png?raw=true)

## API Endpoint(s)

### /getTime
 - GET without query parameter `timezone`

   ![getTime_without_param GET](./docs/images/getTime_without_param.png?raw=true)

 - GET with query parameter `timezone`

   ![getTime_with_param GET](./docs/images/getTime_with_param.png?raw=true)


## References
![Running API Gateway Locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html)
