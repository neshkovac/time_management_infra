import os
from stacks.persistance.dynamo_stack import DynamoDBStack
from stacks.lambda_stack import LambdaStack
from aws_cdk import core
app = core.App()

DynamoDBStack(app,"DynamoDB-Stack")
LambdaStack(app, "Lambda-Stack")

app.synth()
