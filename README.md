# EC2 Tagging 

## Tag EC2 Instances when they are created

This repository conisits of a Boto3 module for a lambda function in AWS.

### Description 

The lamda function triggers everytime a new EC2 instance is created and tags the instance with the owner name.
This module will be used to keep track of who created the EC2 instances and left it unused.
