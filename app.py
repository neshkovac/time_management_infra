import os
from stacks.persistance.dynamo_stack import DynamoDBStack
from stacks.lambda_stack import LambdaStack
from stacks.apigw_stack import ApiGatewayStack
from aws_cdk import core
app = core.App()

dynamo_stack = DynamoDBStack(app,"DynamoDB-Stack")
lambda_stack = LambdaStack(app, "Lambda-Stack")
apigw_stack = ApiGatewayStack(app, "APIGW-Stack", lambda_stack.handlers)

dynamo_stack.tables['user-table'].grant_write_data(lambda_stack.handlers['create_user_handler'])
dynamo_stack.tables['user-table'].grant_read_data(lambda_stack.handlers['get_users_handler'])
dynamo_stack.tables['user-table'].grant_read_data(lambda_stack.handlers['create_schedule_handler'])
dynamo_stack.tables['user-table'].grant_read_data(lambda_stack.handlers['update_schedule_handler'])
dynamo_stack.tables['user-table'].grant_read_data(lambda_stack.handlers['get_user_handler'])
dynamo_stack.tables['user-table'].grant_read_write_data(lambda_stack.handlers['update_user_handler'])
dynamo_stack.tables['user-table'].grant_read_write_data(lambda_stack.handlers['delete_user_handler'])

dynamo_stack.tables['schedule-table'].grant_read_data(lambda_stack.handlers['get_schedules_handler'])
dynamo_stack.tables['schedule-table'].grant_read_data(lambda_stack.handlers['get_schedule_handler'])
dynamo_stack.tables['schedule-table'].grant_read_write_data(lambda_stack.handlers['create_schedule_handler'])
dynamo_stack.tables['schedule-table'].grant_read_write_data(lambda_stack.handlers['update_schedule_handler'])
dynamo_stack.tables['schedule-table'].grant_read_write_data(lambda_stack.handlers['delete_schedule_handler'])

app.synth()
