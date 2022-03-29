import os
import logging
from sam_cli import SAMCLI, SAMCLIException


# Deploy Config
S3_BUCKET_NAME = "lambda-files-bucket"
STACK_NAME = "aws-lambda-with-api-gateway-using-sam"
AWS_REGION = 'eu-central-1'
logging.basicConfig(level=logging.INFO)


# Main
sam_cli = SAMCLI()
try:
    # Step 0: Unit-Testing
    sam_cli.runUnitTests()

    # Step 1: sam_cli.build
    sam_cli.build(template_file='template.yaml',
                  build_dir='build',
                  aws_region=AWS_REGION,
                  manifest='requirements.txt')

    # Step 2: sam_cli.package
    sam_cli.package(template_file_path='build/template.yaml',
                    s3_bucket_name=S3_BUCKET_NAME,
                    output_template_file_path='build/deploy.yaml',
                    aws_region=AWS_REGION)

    # Step 3: sam_cli.deploy
    sam_cli.deploy(output_template_file_path='build/deploy.yaml',
                   stack_name=STACK_NAME,
                   s3_bucket=S3_BUCKET_NAME,
                   aws_region=AWS_REGION)

except SAMCLIException as err:
    logging.info(str(err))
    exit(-1)
