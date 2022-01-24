# LambdaWorkshop
Example code for the AWS Serverless Lambda Workshop

# Following are the steps/commands to install Serverless framework. Node.Js need to be installed for executing the npm commands.
# Can go through the given link for more details, https://www.serverless.com/framework/docs/getting-started
#!/bin/bash

# Step 1: Install Node:
# Go to: https://nodejs.org/en/download/package-manager/

# Step 2: Install serverless
npm install -g serverless

# Step 3: Setup serverless
serverless config credentials --provider aws --key <Key_ID> --secret <secret_value> --profile serverless-admin

# Create project using Serverless
sls create --template aws-python --path hello-world-py

# Deploy using Serverless
sls deploy -v
