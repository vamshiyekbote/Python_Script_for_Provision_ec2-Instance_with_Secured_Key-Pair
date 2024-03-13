import os
import boto3
from botocore.exceptions import NoCredentialsError
import configparser

def load_aws_credentials():
    config = configparser.ConfigParser()
    config.read('aws_config.ini')  # Update the path if the config file is in a different location

    aws_access_key_id = config.get('aws_credentials', 'aws_access_key_id')
    aws_secret_access_key = config.get('aws_credentials', 'aws_secret_access_key')

    return aws_access_key_id, aws_secret_access_key

def create_ec2_instance(instance_name, ami_id, instance_type, key_pair_name):
    try:
        # Retrieve AWS credentials from external config file
        aws_access_key_id, aws_secret_access_key = load_aws_credentials()

        # Check if credentials are available
        if not aws_access_key_id or not aws_secret_access_key:
            raise NoCredentialsError("AWS credentials not available. Please check the configuration file.")

        # Create an EC2 resource
        ec2 = boto3.resource('ec2', region_name='us-east-1', aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key)

        # Create an EC2 instance
        instance = ec2.create_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            KeyName=key_pair_name,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': instance_name}]
            }]
        )

        print(f"Instance '{instance_name}' created successfully with ID: {instance[0].id}")

    except NoCredentialsError:
        print("AWS credentials not available. Please check the configuration file.")
        print("Make sure 'aws_config.ini' contains the correct values for 'aws_access_key_id' and 'aws_secret_access_key'.")

if __name__ == "__main__":
    # Replace the following values with your own
    instance_name = 'MyEC2Instance'
    ami_id = 'ami-xxxxxxxxxxxxxxxxx'  # Amazon Machine Image ID
    instance_type = 't2.micro'  # Instance type
    key_pair_name = 'YourKeyPair'  # Key pair name

    create_ec2_instance(instance_name, ami_id, instance_type, key_pair_name)
