# AWS EC2 Instance Provisioning Script

This Python script uses the `boto3` library to provision an EC2 instance on AWS. It demonstrates how to securely manage AWS credentials and key pair information.

## Features

- Creates an EC2 instance with specified parameters.
- Retrieves AWS credentials from a configuration file.
- Utilizes the `configparser` module to manage sensitive information.

## Prerequisites

Before using the script, ensure you have the following:

- Python installed on your system.
- `boto3` library installed:

  ```bash
  pip install boto3

## Usage
Clone the Repository:

git clone https://github.com/yourusername/Python_Script_for_Provision_ec2-Instance_with_Secured_Key-Pair.git
  
cd Python_Script_for_Provision_ec2-Instance_with_Secured_Key-Pair

## Configure AWS Credentials:

Create a configuration file named aws_config.ini in the project directory:

[aws_credentials]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key

Replace your_access_key_id and your_secret_access_key with your actual AWS credentials.

## Run the Script:

Execute the script using Python:
python create_ec2_instance.py

## Review Output:
The script will create an EC2 instance and display the instance ID upon success.

## Security Considerations
AWS Credentials:
Never expose AWS credentials directly in the script.
Use environment variables or external configuration files for credential management.

## Configuration File (aws_config.ini):
Protect the configuration file from unauthorized access.
Do not share sensitive information.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.












